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
  |-- Shared Rule Engine
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
  |-- Shared Rule Engine
  |-- Reliability Scorecards
  |-- Incident Workbench
  |-- Policy Engine
  |-- Governance Reports

Agent Trust Plane Runtime
  |
  |-- SDK Wrapper / Gateway / Proxy
  |-- Runtime Action Evaluator
  |-- Allow / Ask / Block Verdicts
  |-- Audit Log
  |-- Human Approval Inbox
```

## Design Principles

- OpenTelemetry-first
- Kubernetes-native
- Azure/AKS enterprise-ready
- Local-first for privacy-sensitive testing
- BYOC-ready for regulated enterprises
- Scanner-first before full control plane
- One shared rule engine for scan and guard modes
- Fail-safe defaults for high-risk runtime actions
