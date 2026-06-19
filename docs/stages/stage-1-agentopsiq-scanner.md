# Stage 1 - AgentOpsIQ Scanner Foundation

## Goal

Build the foundation for the first product: a production-readiness scanner for AI agents running on Kubernetes/AKS.

## Stage Status

Status: **Started**

Start date: 2026-06-19

## Scope

Stage 1 is documentation and foundation first, then scanner implementation.

Included:

- Top five product priorities
- Readiness checks v1
- Scanner CLI specification
- Test fixture plan
- Progress tracker
- Issue log

Not included yet:

- Full control-plane UI
- Hosted SaaS backend
- Enterprise RBAC/SSO
- Production AKS deployment

## Stage 1 Deliverables

| Deliverable | Status | Notes |
|---|---|---|
| Top five product priorities documented | Done | See `docs/product/top-five-product-priorities.md` |
| Readiness checks v1 documented | Done | See `docs/product/readiness-checks-v1.md` |
| Scanner CLI scope documented | Done | See `src/cli/README.md` |
| Test fixture plan documented | Done | See `tests/fixtures/README.md` |
| Sample agent plan documented | Done | See `examples/sample-agent/README.md` |
| Initial progress tracker created | Done | See `docs/status/progress-tracker.md` |
| Initial issue log created | Done | See `docs/status/issue-log.md` |
| Scanner implementation skeleton | Started | Python prototype created in `src/cli/agentopsiq.py` |
| First YAML scanner rule | Started | Kubernetes resource and OTel env checks added |
| First Markdown report output | Started | Markdown renderer added to CLI prototype |

## Initial Action Items

1. Confirm scanner language: Python for prototype.
2. Create scanner CLI skeleton.
3. Add fixture: missing resource limits.
4. Add fixture: missing OpenTelemetry exporter.
5. Add first finding model.
6. Add Markdown report output.
7. Add JSON report output.
8. Add unit tests for first checks.

## Acceptance Criteria

Stage 1 is complete when:

- `agentopsiq scan --path <folder>` can scan sample Kubernetes YAML.
- Scanner detects at least five readiness gaps.
- Scanner emits Markdown and JSON reports.
- Test fixtures exist for passing and failing examples.
- Progress tracker and issue log are updated after each work session.
