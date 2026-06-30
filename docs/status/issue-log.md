# AgentOpsIQ Issue Log

This file tracks product, technical, legal, and execution issues.

## Open Issues

| ID | Severity | Area | Issue | Impact | Proposed Resolution | Status |
|---|---|---|---|---|---|---|
| AOP-ISS-001 | High | Legal/immigration | Need attorney confirmation before commercialization, incorporation, revenue, customer contracts, or active operation if visa status is restrictive | Prevents unsafe commercial execution | Consult immigration attorney and document allowed activity boundary | Open |
| AOP-ISS-003 | Medium | Testing | Local Docker Desktop/Kubernetes/Ollama environment not validated in repo | Blocks true E2E tests | Add local lab setup checklist and run first telemetry path | Open |
| AOP-ISS-004 | Medium | Product | OpenTelemetry semantic attributes for AI agents need v1 definition | Blocks telemetry pack | Draft `docs/architecture/otel-agent-attributes.md` | Open |
| AOP-ISS-005 | Low | Branding | Domain/trademark availability not verified for AgentOpsIQ | Could affect public launch naming | Check domain, GitHub org, package names, and trademark before public launch | Open |
| AOP-ISS-006 | Medium | Testing | Scanner prototype needs more rule coverage beyond the first fixtures | Blocks confidence in broader production readiness scoring | Add tests for unsafe secrets, GitHub Action gate, and retry-budget policy checks | Open |

## Closed Issues

| ID | Date | Issue | Resolution |
|---|---|---|---|
| AOP-ISS-000 | 2026-06-19 | Project name was not locked | Locked full name AgentOpsIQ Control Plane and short name AgentOpsIQ |
| AOP-ISS-002 | 2026-06-19 | Scanner implementation language not selected | Selected Python for prototype speed; keep Go as future packaging option |
| AOP-ISS-007 | 2026-06-29 | Bundled Python runtime did not include PyYAML | Created `.venv`, installed `requirements.txt`, installed package editable, verified CLI and unit tests |
