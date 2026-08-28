# AWS Interview questions

## How do you run serverless container on aws

### AWS App Runner

Closest match to Azure ACA

What it gives you
- Deploy from container image (ECR or Docker Hub)
- Automatic HTTPS endpoint
- Built-in load balancing
- Auto scaling
- No cluster management
- Optional VPC access
- Very simple setup
- one App Runner microservice can call another.
- App Runner services are automatically load-balanced: 
  - Automatically scales to multiple instances
  - Automatically distributes traffic across those instances
  - Includes built-in HTTPS endpoint
  - Requires no manual ALB/NLB setup

When to use
- REST APIs
- Backend services
- Microservices
- Web apps

I cannot have (ECS + Fargete does):
- Have 10+ microservices
- Need canary routing
- Need A/B traffic splitting
- Want internal-only service names
- Want service mesh observability

### Amazon ECS with Fargate

(Serverless containers)

This is more powerful but more complex.

Use:
- ECS + Fargate (no EC2 management)

What it gives you
- Full control
- VPC-native networking
- Service discovery
- Load balancers
- Production-grade flexibility

Tradeoff
- More configuration than App Runner.

### AWS Lambda (Container Image mode)

Lambda can run container images up to 10GB.

Good for:
- APIs
- Event-driven workloads
- Background processing

Not good for:
- Long-running services
- WebSockets
- Stateful apps

### Amazon EKS

(Kubernetes)

Only use this if:
- You need Kubernetes
- You need portability
- You need advanced orchestration

### Comparison

| Service                               | Pros                                                                                                                                            | Cons                                                                                                   | Best Use Case                                                                              |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **AWS App Runner**                    | • Simplest deployment<br>• Built-in HTTPS endpoint<br>• Auto scaling<br>• No cluster management<br>• Optional VPC access                        | • Less flexible than ECS<br>• Fewer networking controls<br>• Not ideal for complex microservice meshes | Public APIs, backend services, SaaS apps, quick deployments (closest to ACA)               |
| **Amazon ECS + Fargate**              | • Full VPC control<br>• Fine-grained scaling<br>• Load balancer integration<br>• Mature production setups<br>• No EC2 management (with Fargate) | • More configuration<br>• Requires ALB/NLB setup<br>• More Terraform overhead                          | Production microservices, internal services, containerized APIs needing networking control |
| **AWS Lambda (Container Image mode)** | • True serverless (scale to zero)<br>• Pay per invocation<br>• Minimal infra<br>• Built-in HA                                                   | • 15-min max execution<br>• Not for long-running services<br>• Cold starts possible                    | Event-driven APIs, background processing, lightweight HTTP services                        |
| **Amazon EKS**                        | • Full Kubernetes ecosystem<br>• Portable workloads<br>• Advanced orchestration<br>• Service mesh support                                       | • Highest complexity<br>• Cluster management required<br>• Higher operational overhead                 | Large-scale microservices, platform teams, multi-cloud K8s environments                    |


| Feature                    | App Runner | ECS + Fargate       |
| -------------------------- | ---------- | ------------------- |
| Easiest setup              | ✅          | ❌                   |
| Built-in HTTPS             | ✅          | ❌                   |
| Internal service discovery | ❌          | ✅                   |
| Automatic service routing  | ❌          | ✅ (Service Connect) |
| Full VPC control           | Limited    | ✅                   |
| Enterprise flexibility     | Medium     | High                |
