# AgentOpsIQ Scanner CLI

## Purpose

The scanner is the first product wedge for AgentOpsIQ. It checks whether an AI agent deployment is production-ready for Kubernetes/AKS environments.

## Proposed Command

```bash
agentopsiq scan --path ./examples/sample-agent --output ./reports/readiness-report.md
```

## Initial Inputs

- Kubernetes YAML
- Helm values
- Dockerfile
- GitHub Actions workflow
- OpenTelemetry Collector config
- Optional policy file

## Initial Outputs

- Markdown report
- JSON report
- Exit code for CI

## CLI Options

```text
agentopsiq scan
  --path <folder>
  --format markdown|json|all
  --output <file-or-folder>
  --fail-on critical|high|medium|never
  --profile kubernetes|aks|generic
```

## Implementation Decision Pending

Options:

- Go: best for single binary, enterprise CLI distribution, GitHub Action packaging.
- Python: fastest for prototyping YAML scanning and report generation.

Recommendation: start with Python for prototype speed, then move to Go if distribution becomes important.

## Current Prototype Location

The first Python prototype lives in:

```text
src/agentopsiq/cli.py
```
