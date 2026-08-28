# Cloud-Native systems

Cloud-native systems are applications and architectures designed specifically to run in cloud environments, taking full advantage of cloud capabilities like scalability, resilience, and automation.

## Core Principles of Cloud-Native Systems

Microservices Architecture
- Applications are split into small, independent services.
- Each service handles a single business function.
- Enables faster development, independent scaling, and easier maintenance.

Containerization
- Services are packaged in containers (e.g., Docker).
- Ensures consistent environments across development, testing, and production.
- Simplifies deployment and isolation.

Dynamic Orchestration
- Tools like Kubernetes or Nomad manage deployment, scaling, and lifecycle of containers.
- Automatically handles failover and resource allocation.

DevOps & Continuous Delivery
- Infrastructure and deployment are automated.
- CI/CD pipelines (e.g., GitHub Actions, GitLab CI/CD) deploy changes continuously.
- Promotes rapid iteration and frequent releases.

Scalability
- Designed to scale horizontally by adding more instances of a service.
- Supports auto-scaling based on demand.

Resilience & Observability
- Systems are resilient to failures (e.g., service restarts, failover).
- Monitoring, logging, and tracing are integrated (e.g., Prometheus, Grafana).
- Designed to recover from partial failures without affecting the whole system.

Infrastructure as Code
- Infrastructure is declaratively defined (Terraform, CloudFormation).
- Enables repeatable and version-controlled environments.

API-First Communication
- Services communicate over APIs (REST, gRPC, or messaging queues).
- Loose coupling between services promotes flexibility.

Key Technologies in Cloud-Native Systems:
| Category             | Examples                          | Purpose                                 |
| -------------------- | --------------------------------- | --------------------------------------- |
| Containerization     | Docker, Podman                    | Package apps consistently               |
| Orchestration        | Kubernetes, Nomad                 | Deploy, scale, and manage workloads     |
| Service Mesh         | Consul, Istio, Linkerd            | Secure service-to-service communication |
| Secrets Management   | Vault, AWS Secrets Manager        | Manage credentials safely               |
| CI/CD                | GitHub Actions, GitLab CI, ArgoCD | Automate build/deploy pipelines         |
| Monitoring & Logging | Prometheus, Grafana, ELK stack    | Observe system health and performance   |



