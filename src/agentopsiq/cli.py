from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised only when dependency is missing
    raise SystemExit("PyYAML is required. Install with: pip install -r requirements.txt") from exc


SEVERITY_PENALTY = {
    "critical": 10,
    "high": 6,
    "medium": 3,
    "low": 1,
}


@dataclass
class Finding:
    id: str
    category: str
    severity: str
    message: str
    file: str
    resource: str
    recommendation: str


def load_yaml_documents(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if isinstance(document, dict):
                yield document


def iter_yaml_files(root: Path) -> Iterable[Path]:
    if root.is_file() and root.suffix.lower() in {".yaml", ".yml"}:
        yield root
        return
    for suffix in ("*.yaml", "*.yml"):
        yield from root.rglob(suffix)


def get_containers(document: dict[str, Any]) -> list[dict[str, Any]]:
    spec = document.get("spec", {})
    template = spec.get("template", {})
    pod_spec = template.get("spec", {})
    containers = pod_spec.get("containers", [])
    return containers if isinstance(containers, list) else []


def resource_name(document: dict[str, Any]) -> str:
    kind = document.get("kind", "Unknown")
    metadata = document.get("metadata", {})
    name = metadata.get("name", "unnamed")
    return f"{kind}/{name}"


def env_names(container: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for item in container.get("env", []) or []:
        if isinstance(item, dict) and item.get("name"):
            names.add(str(item["name"]))
    return names


def scan_document(document: dict[str, Any], path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    kind = document.get("kind")
    if kind not in {"Deployment", "StatefulSet", "DaemonSet", "Job", "CronJob"}:
        return findings

    rel_file = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    name = resource_name(document)

    for container in get_containers(document):
        container_name = container.get("name", "unnamed-container")
        resources = container.get("resources", {}) or {}
        requests = resources.get("requests", {}) or {}
        limits = resources.get("limits", {}) or {}
        env = env_names(container)
        label = f"{name}:{container_name}"

        if not requests.get("cpu"):
            findings.append(
                Finding(
                    "AOP-CHK-001",
                    "Kubernetes",
                    "high",
                    "Container is missing CPU requests.",
                    rel_file,
                    label,
                    "Set resources.requests.cpu in the deployment or Helm values.",
                )
            )
        if not requests.get("memory"):
            findings.append(
                Finding(
                    "AOP-CHK-002",
                    "Kubernetes",
                    "high",
                    "Container is missing memory requests.",
                    rel_file,
                    label,
                    "Set resources.requests.memory in the deployment or Helm values.",
                )
            )
        if not limits.get("cpu"):
            findings.append(
                Finding(
                    "AOP-CHK-003",
                    "Kubernetes",
                    "high",
                    "Container is missing CPU limits.",
                    rel_file,
                    label,
                    "Set resources.limits.cpu in the deployment or Helm values.",
                )
            )
        if not limits.get("memory"):
            findings.append(
                Finding(
                    "AOP-CHK-004",
                    "Kubernetes",
                    "high",
                    "Container is missing memory limits.",
                    rel_file,
                    label,
                    "Set resources.limits.memory in the deployment or Helm values.",
                )
            )
        if not container.get("livenessProbe"):
            findings.append(
                Finding(
                    "AOP-CHK-005",
                    "Kubernetes",
                    "high",
                    "Container is missing liveness probe.",
                    rel_file,
                    label,
                    "Add livenessProbe so Kubernetes can detect unhealthy agent workers.",
                )
            )
        if not container.get("readinessProbe"):
            findings.append(
                Finding(
                    "AOP-CHK-006",
                    "Kubernetes",
                    "high",
                    "Container is missing readiness probe.",
                    rel_file,
                    label,
                    "Add readinessProbe so traffic only reaches ready agent workers.",
                )
            )
        if "OTEL_EXPORTER_OTLP_ENDPOINT" not in env:
            findings.append(
                Finding(
                    "AOP-CHK-007",
                    "Observability",
                    "critical",
                    "OpenTelemetry OTLP exporter endpoint is not configured.",
                    rel_file,
                    label,
                    "Set OTEL_EXPORTER_OTLP_ENDPOINT or equivalent collector configuration.",
                )
            )
        if "OTEL_SERVICE_NAME" not in env:
            findings.append(
                Finding(
                    "AOP-CHK-008",
                    "Observability",
                    "high",
                    "OpenTelemetry service name is not configured.",
                    rel_file,
                    label,
                    "Set OTEL_SERVICE_NAME to a stable agent service name.",
                )
            )

    return findings


def scan_path(path: Path) -> dict[str, Any]:
    root = path if path.is_dir() else path.parent
    findings: list[Finding] = []
    scanned_files = 0

    for yaml_file in iter_yaml_files(path):
        scanned_files += 1
        for document in load_yaml_documents(yaml_file):
            findings.extend(scan_document(document, yaml_file, root))

    penalty = sum(SEVERITY_PENALTY.get(f.severity, 0) for f in findings)
    score = max(0, 100 - penalty)
    return {
        "product": "AgentOpsIQ Scanner",
        "score": score,
        "scanned_files": scanned_files,
        "finding_count": len(findings),
        "findings": [asdict(f) for f in findings],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# AgentOpsIQ Readiness Report",
        "",
        f"Readiness score: **{report['score']}/100**",
        f"Scanned files: **{report['scanned_files']}**",
        f"Findings: **{report['finding_count']}**",
        "",
        "## Findings",
        "",
    ]
    if not report["findings"]:
        lines.append("No findings. This sample passed the current scanner checks.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(["| ID | Severity | Category | Resource | Finding | Recommendation |", "|---|---|---|---|---|---|"])
    for finding in report["findings"]:
        lines.append(
            "| {id} | {severity} | {category} | {resource} | {message} | {recommendation} |".format(**finding)
        )
    lines.append("")
    return "\n".join(lines)


def write_report(report: dict[str, Any], output: Path, fmt: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "json":
        output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    elif fmt == "markdown":
        output.write_text(render_markdown(report), encoding="utf-8")
    else:
        raise ValueError(f"Unsupported format: {fmt}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="agentopsiq", description="Scan AI agent production readiness.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan = subparsers.add_parser("scan", help="Scan Kubernetes/AI agent readiness.")
    scan.add_argument("--path", required=True, help="File or folder to scan.")
    scan.add_argument("--format", choices=["markdown", "json"], default="markdown")
    scan.add_argument("--output", required=False, help="Report output file.")
    scan.add_argument("--fail-on", choices=["critical", "high", "medium", "never"], default="never")
    args = parser.parse_args(argv)

    if args.command == "scan":
        target = Path(args.path).resolve()
        report = scan_path(target)
        if args.output:
            write_report(report, Path(args.output), args.format)
        else:
            print(render_markdown(report) if args.format == "markdown" else json.dumps(report, indent=2))
        severities = {finding["severity"] for finding in report["findings"]}
        if args.fail_on != "never":
            order = ["critical", "high", "medium", "low"]
            threshold = order.index(args.fail_on)
            if any(order.index(severity) <= threshold for severity in severities if severity in order):
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
