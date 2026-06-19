# Top Five AgentOpsIQ Product Priorities

This list is selected from the current README, product brief, roadmap, feature catalog, architecture, local lab test plan, and inspiration map.

## Selection Criteria

- Strong fit with AgentOpsIQ's locked tagline: "Production intelligence for reliable AI agents."
- Directly uses Ganesh's strengths: SRE, DevOps, Azure, Kubernetes, Terraform, GitHub Actions, OpenTelemetry, ArgoCD, DevSecOps, and enterprise architecture.
- Builds toward an enterprise-grade product without starting too broad.
- Can be tested locally with Docker Desktop, local Kubernetes, Ollama, and laptop GPU.
- Creates a path from local tool to GitHub Action to enterprise control plane.

## 1. AgentOpsIQ Scanner

Purpose: production-readiness scanner for AI agents running on Kubernetes/AKS.

Why this is first:

- It is the clearest MVP wedge.
- It can run locally and in CI.
- It produces an enterprise-readable readiness score.
- It does not require a hosted SaaS product on day one.

Core features:

- Kubernetes manifest scanner
- Helm values scanner
- OpenTelemetry config scanner
- GitHub Actions workflow scanner
- Agent reliability checklist
- JSON and Markdown report output
- 100-point readiness score
- Critical/high/medium/low finding severity

## 2. OpenTelemetry Agent Telemetry Pack

Purpose: standardize the telemetry AI agents must emit to be production-ready.

Core features:

- OTel Collector config
- Recommended agent span attributes
- Tool-call and model-call trace examples
- Deployment metadata correlation
- Export paths for Jaeger/Tempo, Prometheus, Grafana, OpenObserve, and Azure Monitor later

## 3. AgentOpsIQ AKS Enterprise Kit

Purpose: prove the product is enterprise/Azure/Kubernetes-ready.

Core features:

- AKS deployment reference
- Terraform skeleton
- Helm chart structure
- ArgoCD deployment example
- Managed identity notes
- Private network/BYOC deployment guidance
- Azure Monitor integration roadmap

## 4. AgentOpsIQ GitHub Action Gate

Purpose: make AgentOpsIQ usable in real engineering workflows.

Core features:

- Run scanner in CI
- Fail builds on critical production-readiness gaps
- Post PR comments
- Upload JSON/Markdown artifacts
- Add deployment metadata to telemetry

## 5. AgentOpsIQ Incident Workbench

Purpose: turn telemetry into SRE-friendly incident understanding.

Core features:

- Agent execution timeline
- Tool-call and model-call failure view
- Kubernetes event correlation
- Local Ollama-powered incident summary
- Root-cause hypothesis list
- Suggested remediation steps
- Markdown incident report export

## Recommended Build Order

1. AgentOpsIQ Scanner
2. OpenTelemetry Agent Telemetry Pack
3. Local lab and failure fixtures
4. GitHub Action Gate
5. AKS Enterprise Kit
6. Incident Workbench

The scanner remains the first build target because every later product module depends on the same readiness checks, severity model, and report format.
