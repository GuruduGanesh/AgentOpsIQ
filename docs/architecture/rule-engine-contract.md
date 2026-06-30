# Shared Rule Engine Contract

Locked: 2026-06-30

## Purpose

The shared rule engine is the bridge between AgentOpsIQ Scanner and the Agent Trust Plane runtime.

A rule should be written once and be usable in two modes:

- **Scan mode:** inspect static project/deployment inputs and return findings.
- **Guard mode:** inspect a live runtime action and return a verdict.

The first implementation should keep the existing `agentopsiq scan` output identical while moving hard-coded checks into rule objects.

## Core Concepts

## Rule

A rule is a reusable policy unit.

Required fields:

| Field | Purpose |
|---|---|
| `id` | Stable rule ID, for example `AOP-CHK-001` |
| `name` | Short human-readable name |
| `category` | Kubernetes, Observability, Governance, Cost, Reliability, Security, CI/CD |
| `severity` | critical, high, medium, low |
| `description` | What the rule checks |
| `recommendation` | How to fix or satisfy the rule |
| `modes` | scan, guard, or both |
| `evaluate_static` | Optional scan-mode evaluator |
| `evaluate_runtime` | Optional guard-mode evaluator |

Python shape for the first prototype:

```python
@dataclass
class Rule:
    id: str
    name: str
    category: str
    severity: str
    description: str
    recommendation: str
    modes: set[str]

    def evaluate_static(self, context: StaticContext) -> list[Finding]:
        return []

    def evaluate_runtime(self, action: RuntimeAction) -> Verdict:
        return Verdict.allow()
```

## StaticContext

Used by scan mode.

Represents a static project/deployment input.

Initial fields:

| Field | Purpose |
|---|---|
| `root_path` | Root path being scanned |
| `file_path` | Current file |
| `document` | Parsed YAML/JSON document |
| `resource_kind` | Kubernetes kind if available |
| `resource_name` | Kubernetes resource name if available |
| `container` | Current container if applicable |
| `metadata` | Extra scan metadata |

## Finding

Returned by scan mode.

Current output compatibility fields:

| Field | Purpose |
|---|---|
| `id` | Rule/check ID |
| `category` | Finding category |
| `severity` | critical/high/medium/low |
| `message` | Human-readable finding |
| `file` | Relative file path |
| `resource` | Resource label |
| `recommendation` | Remediation guidance |
| `evidence` | Optional structured evidence later |

The initial refactor must preserve current JSON/Markdown output fields.

## RuntimeAction

Used by guard mode.

Represents one proposed live agent action.

Initial fields:

| Field | Purpose |
|---|---|
| `action_id` | Unique action ID |
| `agent_id` | Agent identity |
| `session_id` | Task/session/conversation ID |
| `action_type` | tool_call, model_call, api_call, email, file_write, prod_write, spend |
| `tool_name` | Tool being used, if any |
| `model_name` | Model being used, if any |
| `target` | External system or target resource |
| `input_summary` | Safe summary of the requested action |
| `risk_level` | low/medium/high/critical |
| `estimated_cost` | Cost estimate if available |
| `retry_count` | Current retry count |
| `metadata` | Extra runtime context |

## Verdict

Returned by guard mode.

Allowed values:

- `ALLOW`
- `ASK`
- `BLOCK`

Initial fields:

| Field | Purpose |
|---|---|
| `decision` | ALLOW / ASK / BLOCK |
| `rule_id` | Rule that decided or influenced the verdict |
| `reason` | Human-readable reason |
| `severity` | critical/high/medium/low |
| `audit_required` | Whether to record an audit event |
| `approval_required` | Whether a human approval is needed |
| `metadata` | Extra decision context |

## Rule Engine

Responsibilities:

- Load built-in rules.
- Run scan-mode rules over static contexts.
- Run guard-mode rules over runtime actions.
- Preserve current scanner scoring.
- Return deterministic decisions.
- Record enough evidence for future audit logs.

Initial engine functions:

```python
def evaluate_static(contexts: list[StaticContext], rules: list[Rule]) -> list[Finding]:
    ...

def evaluate_runtime(action: RuntimeAction, rules: list[Rule]) -> Verdict:
    ...
```

## Scoring

Keep current severity penalties initially:

| Severity | Penalty |
|---|---:|
| critical | 10 |
| high | 6 |
| medium | 3 |
| low | 1 |

Readiness score:

```text
score = max(0, 100 - sum(severity penalties))
```

This can become category-weighted later, but the first rule-engine refactor should not change report behavior.

## Built-In Rule Packs

Initial built-in rule packs:

- `kubernetes-baseline`
- `otel-baseline`
- `agent-reliability`
- `governance-baseline`
- `ci-cd-baseline`

Future custom rule packs:

- YAML/JSON organization policies
- Regulated-industry packs
- AKS-specific pack
- MCP/tool-call safety pack

## First Refactor Target

Move these existing checks from imperative code into built-in static rules:

- `AOP-CHK-001`: CPU requests
- `AOP-CHK-002`: memory requests
- `AOP-CHK-003`: CPU limits
- `AOP-CHK-004`: memory limits
- `AOP-CHK-005`: liveness probe
- `AOP-CHK-006`: readiness probe
- `AOP-CHK-007`: OTel exporter endpoint
- `AOP-CHK-008`: OTel service name

Acceptance criteria:

- Existing tests still pass.
- JSON output shape remains compatible.
- Markdown output remains compatible.
- Scan scores remain unchanged for current fixtures.
- Rule objects can later add runtime behavior without changing scanner callers.
