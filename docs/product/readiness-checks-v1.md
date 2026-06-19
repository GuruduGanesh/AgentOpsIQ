# AgentOpsIQ Readiness Checks v1

These checks define the first scanner scope. They are intentionally concrete, testable, and enterprise-readable.

## Scoring Model

Initial score: 100 points.

Categories:

- Observability coverage: 20 points
- Kubernetes production readiness: 20 points
- Agent reliability controls: 20 points
- Security and governance: 15 points
- CI/CD and deployment metadata: 15 points
- Cost and performance controls: 10 points

Severity levels:

- Critical: must fix before production
- High: should fix before pilot
- Medium: should fix before scale
- Low: improvement recommendation

## First 25 Checks

| ID | Category | Check | Severity | Initial Detection Source |
|---|---|---|---|---|
| AOP-CHK-001 | Kubernetes | Agent deployment has CPU requests | High | Kubernetes manifest / Helm values |
| AOP-CHK-002 | Kubernetes | Agent deployment has memory requests | High | Kubernetes manifest / Helm values |
| AOP-CHK-003 | Kubernetes | Agent deployment has CPU limits | High | Kubernetes manifest / Helm values |
| AOP-CHK-004 | Kubernetes | Agent deployment has memory limits | High | Kubernetes manifest / Helm values |
| AOP-CHK-005 | Kubernetes | Agent service has liveness probe | High | Kubernetes manifest / Helm values |
| AOP-CHK-006 | Kubernetes | Agent service has readiness probe | High | Kubernetes manifest / Helm values |
| AOP-CHK-007 | Observability | OpenTelemetry exporter is configured | Critical | Env vars / config |
| AOP-CHK-008 | Observability | Service name is configured for traces | High | Env vars / OTel resource attrs |
| AOP-CHK-009 | Observability | Deployment environment is attached to telemetry | Medium | Env vars / GitHub Actions |
| AOP-CHK-010 | Observability | Git SHA or deployment version is attached to telemetry | Medium | GitHub Actions / env vars |
| AOP-CHK-011 | Agent Reliability | Agent execution ID is represented in traces | High | OTel attributes |
| AOP-CHK-012 | Agent Reliability | Agent step/task ID is represented in traces | High | OTel attributes |
| AOP-CHK-013 | Agent Reliability | Tool calls are represented as child spans | Critical | OTel traces |
| AOP-CHK-014 | Agent Reliability | Model calls are represented as child spans | Critical | OTel traces |
| AOP-CHK-015 | Agent Reliability | Tool-call errors are captured | Critical | OTel traces/logs |
| AOP-CHK-016 | Agent Reliability | Retry count is captured | High | OTel attributes/logs |
| AOP-CHK-017 | Agent Reliability | Retry budget exists | High | Config / policy file |
| AOP-CHK-018 | Cost/Performance | Model latency is captured | High | OTel metrics/traces |
| AOP-CHK-019 | Cost/Performance | Token or cost metadata is captured | Medium | OTel attributes/logs |
| AOP-CHK-020 | Governance | High-risk tool calls are audit logged | Critical | Logs / policy file |
| AOP-CHK-021 | Governance | Secrets are not stored in plain manifest env vars | Critical | Kubernetes manifest / Helm values |
| AOP-CHK-022 | Governance | Namespace has resource quota or limit range | Medium | Kubernetes manifest / cluster scan |
| AOP-CHK-023 | CI/CD | GitHub Actions workflow runs readiness scan | Medium | GitHub workflow |
| AOP-CHK-024 | CI/CD | Critical findings can fail CI | Medium | GitHub workflow |
| AOP-CHK-025 | Incident Response | Scanner can generate Markdown readiness report | High | Scanner output |

## Report Sections

The first scanner report should include:

- Executive summary
- Readiness score
- Critical gaps
- Category scores
- Findings table
- Recommended fixes
- Missing telemetry attributes
- Kubernetes production gaps
- Security/governance gaps
- CI/CD gaps
- Next actions
