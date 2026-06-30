# AgentOpsIQ Feature Catalog

## Shared Rule Engine

- One rule engine for scan mode and guard mode
- Reusable rule objects
- Static evaluation for readiness findings
- Runtime evaluation for allow / ask / block verdicts
- Policy-as-code rule packs later
- Custom organization rule packs later
- Critical/high/medium/low severity model
- 100-point readiness scoring

## AgentOpsIQ Scanner

- Kubernetes manifest scanning
- Helm values scanning
- Dockerfile scanning
- GitHub Actions workflow scanning
- OpenTelemetry configuration scanning
- Production readiness score
- Markdown, JSON, and future SARIF output
- CI/CD pass/fail gates

## Agent Trust Plane / Guard Mode

- Runtime wrapper, proxy, gateway, or MCP proxy
- Guard every important tool call, model call, and external action
- Return allow / ask-a-human / block verdicts
- Agent identity and least-privilege tool scopes
- Cost caps per task/day
- Retry budgets
- Rate limits
- Latency guards
- Kill switch
- High-risk tool blocking
- Human approval for risky actions

## Observability

- Agent step traces
- Tool-call traces
- Model-call traces
- Cost and token metadata
- Latency metrics
- Error metrics
- Retry metrics
- Kubernetes events
- Deployment metadata correlation

## Reliability

- Retry budget checks
- Latency SLO checks
- Error-rate SLO checks
- Agent loop detection
- Tool-call failure detection
- Model-call timeout detection
- Readiness/liveness probe checks
- Resource request and limit checks

## Incident Workbench

- Agent execution timeline
- Related traces, logs, metrics, and Kubernetes events
- Root-cause hypothesis ranking
- Local Ollama-powered incident summary
- Suggested remediation steps
- Markdown incident report export

## Policy And Governance

- Policy-as-code
- High-risk tool-call audit logs
- Runtime allow / ask / block decision log
- Human approval records
- Data-retention controls
- RBAC roadmap
- SSO roadmap
- Compliance report roadmap
- Customer-owned telemetry storage option
- BYOC deployment model

## Enterprise Integrations

- Azure Monitor
- OpenTelemetry Collector
- Grafana
- Prometheus
- Jaeger or Tempo
- OpenObserve
- GitHub Actions
- ArgoCD
- ServiceNow roadmap

## Human Approval Experience

- Web approval inbox first
- Approve / Block decision flow
- Context-rich risk explanation
- Desktop cockpit later
- Mobile approval app later

## Confidence Score

- Shareable agent reliability/safety score
- Starts from scanner readiness score
- Expands with runtime guard coverage
- Can become trust badge later
