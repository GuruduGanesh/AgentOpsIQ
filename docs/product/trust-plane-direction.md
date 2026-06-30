# AgentOpsIQ -> Agent Trust Plane Direction

Locked: 2026-06-30

## One-Line Direction

Elevate AgentOpsIQ from a one-time readiness scanner into a single product that also becomes a runtime Agent Trust Plane:

> One product, one codebase, two modes, one shared rule engine.

## Product Thesis

Delegating real authority to an AI agent today feels like gambling. People cannot see what an agent will do, constrain what it can do, or prove what it did.

AgentOpsIQ closes that gap so people can move from merely supervising agents to governing them.

## Naming And Messaging

Product name:

- **AgentOpsIQ Control Plane**

Primary product tagline:

- **Production intelligence for reliable AI agents.**

Marketing headline:

- **Delegate with confidence.**

Use the tagline for product/category positioning. Use the headline for landing pages, decks, and user-facing narrative.

## The Two Modes

## Scan Mode: Before It Ships

Scan mode is today's product wedge.

It statically checks an agent project and emits:

- Readiness score
- Findings
- Recommendations
- Markdown report
- JSON report
- Future SARIF output
- CI fail-on threshold

Scan mode answers:

> Is this AI agent ready to ship safely into production?

## Guard Mode: While It Runs

Guard mode is the Agent Trust Plane runtime.

It sits in the live path of agent actions and decides:

- **ALLOW:** action is permitted automatically.
- **ASK:** pause and request human approval.
- **BLOCK:** deny the action and record the reason.

Guard mode answers:

> Should this live agent action be allowed right now?

## How The Two Relate

```text
        BEFORE SHIPPING                 |            WHILE RUNNING
   (Scan mode = today's AgentOpsIQ)     |      (Guard mode = the Trust Plane)

  Dev / CI                              |     User or App
    | agentopsiq scan                   |        | "do this task"
    v                                   |        v
  reads K8s / Helm / OTel               |   AGENT TRUST PLANE
    | gives readiness score             |     identity + policy
    v                                   |     cost / retry caps
  pass the gate -> safe to deploy ------+---> live risk verdict: allow / ask / block
                                        |        v
                                        |   tools / data / money / prod  (all recorded)
                                        |        v
                                        |   human approval when needed
```

Scan is the inspection before the agent gets on the road. Guard is the seatbelt, brakes, and audit trail while it is driving.

The scanner's findings can feed the Trust Plane:

> This agent passed inspection. Here are the rules it must follow while running.

## Shared Rule Engine

The bridge between scan and guard is a shared rule engine.

A rule is written once and can run in either mode:

- In scan mode, the rule reports a gap.
- In guard mode, the rule enforces a live decision.

| Rule | Scan Mode: Report | Guard Mode: Enforce |
|---|---|---|
| Agents must have a cost cap | Warn: no cost cap configured | Block or ask when the cost cap is exceeded |
| High-risk tools need approval | Warn: no audit/approval on risky tool | Pause and ask a human |
| Retry budget required | Warn: no retry budget configured | Stop the retry loop |
| Tool calls must be traced | Warn: missing tool-call spans | Block high-risk tool calls with no audit/trace context |
| Agent identity required | Warn: missing identity metadata | Block unauthenticated agent action |

Write the rule once -> serve both jobs. This is why it is an elevation, not a second product.

See [Shared Rule Engine Contract](../architecture/rule-engine-contract.md).

## Core Feature Set

## 1. Shared Rule Engine

Foundation for both modes.

Features:

- Reusable rule objects
- `id`, `category`, `severity`, `description`, `recommendation`
- Static evaluation for scan mode
- Runtime evaluation for guard mode
- Policy-as-code rule packs
- YAML/JSON rule loading later
- Custom organization rule packs
- Severity model: critical / high / medium / low
- 100-point readiness scoring with penalties

## 2. Scan Mode

Keep and extend today's scanner.

Current checks:

- Kubernetes CPU/memory requests
- Kubernetes CPU/memory limits
- Liveness/readiness probes
- OpenTelemetry exporter endpoint
- OpenTelemetry service name

Target checks:

- Kubernetes manifests
- Helm values
- Dockerfiles
- GitHub Actions
- OpenTelemetry config
- Trace attributes: `agent.id`, `agent.step`, `tool.name`, `model.name`, `deployment.sha`
- Retry budgets
- Cost caps
- Audit logging
- Secrets-in-env
- Deployment metadata

Outputs:

- Markdown
- JSON
- SARIF later
- CI fail-on threshold: critical/high/medium/never

## 3. Guard Mode: Trust Plane Runtime

The runtime guard is a thin gateway, proxy, wrapper, or SDK integration that every important agent action passes through.

Guarded action types:

- Tool calls
- Model calls
- External API calls
- Email/message sends
- File or data writes
- Production infrastructure actions
- Payment or spend actions
- Ticket/code/PR actions

Verdicts:

- `ALLOW`
- `ASK`
- `BLOCK`

Runtime controls:

- Agent identity
- Tool allowlists
- Tool scopes
- Cost caps per task/day
- Retry budgets
- Rate limits
- Latency guards
- Kill switch
- Risky-tool blocking
- Human approval on dangerous action
- Prompt-injection / unsafe-intent checks before risky actions

Delivery forms:

- Python SDK wrapper
- Node SDK wrapper
- Network gateway
- MCP proxy later

## 4. OpenTelemetry-Native Observability

Emit telemetry for:

- Agent step
- Tool call
- Model call
- Guard decision
- Human approval event
- Runtime block event
- Cost and token usage
- Kubernetes context
- Deployment metadata

Correlation path:

```text
agent step -> tool call -> model call -> guard verdict -> Kubernetes pod -> deployment SHA -> environment
```

Export targets:

- Jaeger / Tempo
- Prometheus
- Grafana
- Azure Monitor
- OpenObserve
- Any OTel-compatible backend

## 5. Audit And Governance

Audit goal:

> For every agent action, prove who/what/when/why and the decision that allowed, asked, or blocked it.

Features:

- Tamper-evident audit log later
- Every allow / ask / block decision recorded
- Decision reason
- Rule that fired
- Agent identity
- Human approver identity when applicable
- Data-retention controls
- Compliance-ready exports
- BYOC / customer-owned storage option

## 6. Human Approval Experience

Start web-first.

Approval inbox:

- Action waiting for approval
- Agent identity
- Requested tool/action
- Risk reason
- Relevant trace/log context
- Approve / Block
- Future: approve once / approve always / auto rule

Later:

- Desktop cockpit for IDE/terminal-integrated agent mission control
- Mobile approval app for push notifications

Mobile concept:

> A banking app for your AI agent actions.

Example:

> Agent wants to spend $40 and email 3 people. Approve or Block?

## 7. Confidence Score

Adoption wedge:

- Standardized agent reliability/safety score
- Starts from free scanner score
- Grows into a trust badge
- Can become a data moat if many projects use the scanner

This should remain grounded in evidence:

- Static readiness
- Runtime guard coverage
- Audit completeness
- OTel coverage
- Policy coverage
- Incident history later

## 8. Enterprise Control Plane

Later-stage enterprise product:

- Multi-agent registry
- Multi-cluster inventory
- Reliability scorecards
- Policy management
- Incident history
- RBAC
- SSO
- Executive reports
- BYOC install on AKS/Kubernetes

## Platform Strategy

Preferred strategy:

> Local/BYOC-first, SaaS-compatible later.

Reason:

- The current scanner runs locally and in CI.
- Enterprise trust products often need customer-owned cloud, private network, and regulated deployment paths.
- Hosted SaaS should not be the first dependency for customers to try the product.
- The architecture should still support a SaaS control plane later.

Packaging strategy:

- Free open-source scanner as adoption wedge
- Paid Trust Plane runtime
- Paid enterprise control plane
- BYOC/private-network deployment for regulated customers
- SaaS dashboard later for smaller teams and faster adoption

## Architecture Principles

- One rule engine, two modes
- Framework-agnostic
- OpenTelemetry-native
- Zero-trust isolation in guard mode
- BYOC/private-network friendly
- Low added latency on live path
- Fail-safe defaults
- Ask or deny on uncertainty for high-risk actions
- Keep scan output stable while refactoring internals

## Founder Moat To Leverage

Ganesh's background maps directly to this category:

- SRE and reliability engineering
- DevOps and CI/CD
- DevSecOps and zero-trust policy
- OpenTelemetry observability
- Azure, Kubernetes, and AKS
- Terraform and GitHub Actions
- Enterprise architecture
- BYOC deployment patterns

This is exactly the product area where app-layer agent teams often lack deep infrastructure experience.

## Build Order

Ship value at each step. Do not build everything at once.

1. **Rule engine refactor**
   Move hard-coded scanner checks into reusable rule objects. Keep current scan output identical.

2. **Guard mode v0.1**
   Add `agentopsiq guard` as a thin runtime wrapper/gateway. Start with two live rules: cost cap and block risky tool.

3. **Audit log + approval inbox**
   Record every action. Risky ones wait for a human approve/block decision. Web first.

4. **OTel correlation + SARIF/GitHub Action distribution**
   Strengthen adoption and CI/CD workflow integration.

5. **Desktop cockpit, then mobile approval app**
   Add these only after web approval flow and guard mode are useful.

6. **Enterprise control plane + BYOC on AKS**
   Multi-agent, multi-cluster, RBAC/SSO, reporting, and regulated deployment.

## Non-Goals For Now

- Generic chatbot
- Full Datadog replacement
- Full LangSmith replacement
- Hosted SaaS before local/BYOC works
- Multi-cluster RBAC/SSO before guard mode is proven
- Mobile app before web approval flow works
- Full control-plane UI before rule engine and guard mode exist

## Current Reality

Real today:

- Scanner CLI
- Kubernetes manifest checks
- OTel env checks
- Markdown/JSON reports
- Fixtures and unit tests

Roadmap:

- Shared rule engine
- Guard mode
- Audit log
- Approval inbox
- OTel runtime decision telemetry
- Enterprise control plane

The immediate next implementation task is **Enhancement 1: shared rule engine refactor**.
