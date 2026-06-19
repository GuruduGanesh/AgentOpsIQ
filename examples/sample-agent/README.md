# Sample AI Agent

This folder will contain the local demo agent used for AgentOpsIQ testing.

## Purpose

The sample agent should create realistic telemetry and failure modes without requiring any cloud service.

## Local Stack

- Docker Desktop
- Local Kubernetes
- Ollama
- OpenTelemetry SDK
- OpenTelemetry Collector
- Sample tool services

## Initial Agent Behavior

The first sample agent should:

- Receive a task
- Call a local tool service
- Call Ollama for a model response
- Emit logs
- Emit OpenTelemetry traces
- Expose health endpoints

## Failure Modes To Simulate

1. Tool call failure
2. Retry loop
3. Model latency spike
4. Missing trace context
5. Pod restart due to memory pressure
