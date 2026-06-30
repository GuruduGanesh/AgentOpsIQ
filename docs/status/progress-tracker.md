# AgentOpsIQ Progress Tracker

This file tracks every meaningful project step. Update it after each work session.

## Current Phase

Current phase: **Stage 1 - AgentOpsIQ Scanner Foundation**

Current status: **Started**

## Strategic Direction (Locked 2026-06-30)

AgentOpsIQ is being elevated from a one-time **readiness scanner** into a single product
that also becomes a runtime **Agent Trust Plane**. It stays one product, one codebase, two modes:

- **Scan mode** (today): check an agent before it ships. *"Are you ready to drive?"*
- **Guard mode** (new): protect the agent while it runs - allow / ask-a-human / block on every
  action, with an audit trail. *"Seatbelt and brakes while you drive."*

Both modes are powered by **one shared rule engine** - a rule is written once and can either
*report* a gap (scan mode) or *enforce* it live (guard mode). The scanner stays the free, viral
wedge; the Trust Plane is where the durable enterprise product lives. This is an elevation, not a pivot.

Immediate technical bridge: refactor today's hard-coded checks into a shared rule engine that can
run in both scan and guard modes. See [Trust Plane Direction](../product/trust-plane-direction.md).

## Progress Log

| Date | Area | Status | Progress | Next Step |
|---|---|---|---|---|
| 2026-06-19 | Project setup | Done | AgentOpsIQ project folder created and initialized as Git repo | Commit baseline |
| 2026-06-19 | Branding | Done | Locked name: AgentOpsIQ Control Plane; tagline: Production intelligence for reliable AI agents | Keep branding stable |
| 2026-06-19 | Documentation | Done | Product brief, roadmap, feature catalog, architecture, local lab plan, inspiration map, and legal/IP boundaries created | Keep docs updated as product changes |
| 2026-06-19 | Prioritization | Done | Top five product priorities selected | Start scanner implementation |
| 2026-06-19 | Stage 1 | Started | Scanner foundation docs, readiness checks, fixture plan, and issue log created | Choose implementation language |
| 2026-06-19 | Scanner prototype | Started | Python CLI skeleton, first Kubernetes/OTel checks, Markdown/JSON output, and initial fixtures added | Run scanner locally and add tests |
| 2026-06-19 | Scanner execution | Blocked | CLI execution reached dependency gate; bundled Python is missing PyYAML | Create local venv and install requirements |
| 2026-06-29 | Scanner execution | Done | Created `.venv`, installed requirements, installed package editable, verified entry point, ran unit tests and fixture scans | Expand scanner checks and define OTel agent attributes |
| 2026-06-29 | Customer pain validation | Done | Documented enterprise pain points, validation questions, personas, signals, MVP hypothesis, and long-term product hypothesis | Use this in customer interviews and investor narrative |
| 2026-06-30 | Strategy | Done | Locked direction: elevate AgentOpsIQ into a combined Scan + Guard product (Agent Trust Plane) on one shared rule engine | Write Trust Plane direction doc and refactor checks into a rule engine |
| 2026-06-30 | Trust Plane direction doc | Done | Captured vision, scan-vs-guard model, relationship to scanner, and phased roadmap | Begin Enhancement 1 (rule engine refactor) |
| 2026-06-30 | Rule engine refactor | Not started | Will move hard-coded checks in `cli.py` into reusable rules that run in scan or guard mode | Implement and keep existing scan output identical |
| 2026-06-30 | Rule engine contract | Done | Added shared rule engine contract for Rule, StaticContext, Finding, RuntimeAction, Verdict, and scoring | Implement Enhancement 1 against the contract |

## Action Items (Next)

Ordered, each ships value on its own:

1. **Enhancement 1 - Rule engine refactor.** Turn each hard-coded check into a reusable rule object;
   keep current `scan` output identical. *(This is the bridge from scanner to Trust Plane.)*
2. **Enhancement 2 - Guard mode v0.1 (`agentopsiq guard`).** A thin proxy/wrapper agent tool calls
   pass through; start with two live rules: cost cap and block-risky-tool.
3. **Enhancement 3 - Audit log + approval inbox.** Record every action; risky ones wait for a human
   "approve / block." Web first, phone app later.
4. Expand scanner checks toward the full readiness-checks-v1 list and define OTel agent attributes.
5. Package the scanner as a free GitHub Action (adoption wedge).
6. Local lab sample agent to demo both scan and guard end to end.

## Expectations (Reality Check)

- **Scope discipline:** build in the order above; do **not** try to ship scan + guard + UI at once.
- **What is real today:** scan mode works (CLI, score, Markdown/JSON, fixtures, tests). Guard mode,
  audit log, and approval app do **not** exist yet - they are roadmap, not current capability.
- **Effort gradient:** Enhancement 1 is small and contained. Guard mode and the audit/approval layer
  are real infrastructure and significantly larger.
- **Rough horizon (solo, part-time):** rule engine in days; guard v0.1 in weeks; audit + approval inbox
  and enterprise/BYOC control plane in months. Treat dates as direction, not promises.
- **Non-goals for now:** full multi-cluster control plane, RBAC/SSO, hosted SaaS, and mobile app are
  later stages - not part of the immediate build.

## Milestone Tracker

| Milestone | Status | Target |
|---|---|---|
| M0: Project structure ready | Done | 2026-06-19 |
| M1: Scanner foundation documented | Done | 2026-06-19 |
| M2: Scanner CLI skeleton | Done | 2026-06-29 |
| M3: First five scanner checks | Done | 2026-06-29 |
| M4: Markdown/JSON report output | Done | 2026-06-29 |
| M5: Local lab sample agent | Not started | After scanner report |
| M6: GitHub Action gate | Not started | After scanner MVP |
| M7: Shared rule engine (scan + guard ready) | Not started | Next - Enhancement 1 |
| M8: Guard mode v0.1 (cost cap + block risky tool) | Not started | After M7 |
| M9: Audit log + human approval inbox | Not started | After M8 |
| M10: Enterprise / BYOC control plane on AKS | Not started | Later stage |

## Operating Rule

Every implementation session should update:

- This progress tracker
- `docs/status/issue-log.md`
- Any affected product or architecture doc
