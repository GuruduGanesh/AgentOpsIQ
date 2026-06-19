# Local Lab Test Plan

## Available Local Assets

- Docker Desktop
- Local Kubernetes
- Ollama
- Laptop GPU
- OpenTelemetry Collector
- Grafana, Prometheus, Jaeger/Tempo, and optional OpenObserve

## Test Goals

- Validate agent telemetry end to end.
- Simulate realistic AI agent production failures.
- Generate readiness scores.
- Generate incident reports locally without sending data to an external model.

## Required Test Scenarios

1. Agent calls the wrong tool.
2. Agent retries a failing tool until cost increases.
3. Model latency spikes.
4. Agent pod restarts due to memory pressure.
5. Trace context is lost across a tool call.
6. Deployment metadata is missing from traces.
7. Secret handling is unsafe.
8. Resource limits are missing.
9. Logs exist but traces are missing.
10. High-risk tool call has no audit event.

## Expected Output Per Scenario

- Raw telemetry
- Readiness score
- Incident timeline
- Root-cause hypothesis
- Suggested fix
- Markdown incident report
