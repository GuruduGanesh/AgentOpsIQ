# AgentOpsIQ Reference Architecture

## Local Development Architecture

```text
Developer Laptop
  |
  |-- Docker Desktop Kubernetes
  |-- Ollama with local model
  |-- Sample AI Agent Service
  |-- Sample Tool Services
  |-- OpenTelemetry Collector
  |-- Prometheus / Grafana
  |-- Jaeger or Tempo
  |-- AgentOpsIQ Scanner
```

## Enterprise Architecture

```text
GitHub Actions / CI
  |
  |-- AgentOpsIQ Scanner
  |-- Readiness Report
  |-- Policy Gate
  |
AKS / Kubernetes
  |
  |-- AI Agent Workloads
  |-- Tool Services
  |-- OpenTelemetry Collector
  |-- Kubernetes Event Collector
  |
Telemetry Backends
  |
  |-- Traces
  |-- Logs
  |-- Metrics
  |-- Deployment Metadata
  |
AgentOpsIQ Control Plane
  |
  |-- Reliability Scorecards
  |-- Incident Workbench
  |-- Policy Engine
  |-- Governance Reports
```

## Design Principles

- OpenTelemetry-first
- Kubernetes-native
- Azure/AKS enterprise-ready
- Local-first for privacy-sensitive testing
- BYOC-ready for regulated enterprises
- Scanner-first before full control plane
