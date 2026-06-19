# Scanner Test Fixtures

Fixtures are sample inputs used to verify scanner behavior.

## Fixture Categories

- `passing/`: examples that should produce high readiness scores.
- `missing-resource-limits/`: deployment without CPU/memory limits.
- `missing-otel-exporter/`: agent with no OpenTelemetry exporter.
- `missing-tool-call-traces/`: agent telemetry without tool-call spans.
- `unsafe-secrets/`: Kubernetes manifests with unsafe secret patterns.
- `missing-ci-gate/`: repo with no GitHub Action scan.

## First Fixtures To Build

1. Failing Kubernetes deployment with no resource limits.
2. Passing Kubernetes deployment with resource requests/limits.
3. Failing deployment with no OTel exporter.
4. Passing deployment with basic OTel environment variables.
5. Failing GitHub Actions workflow with no scanner gate.

## Expected Fixture Output

Each fixture should have:

- Input files
- Expected findings
- Expected severity
- Expected score impact
- Expected report snapshot later
