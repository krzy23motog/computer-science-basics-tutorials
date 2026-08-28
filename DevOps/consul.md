# Consul

HashiCorp Consul is a service networking tool that provides:
- Service discovery
- Service segmentation
- Health checking
- Key/value storage

It is used in modern cloud-native and microservices architectures to help services find and securely communicate with each other.

Consul provides:
- Dynamic service discovery – services register themselves and discover peers automatically.
- Health checks – unhealthy services are removed from the registry.
- Service mesh capabilities – secure, encrypted communication.
- KV storage – configuration and metadata storage.

Core Concepts
- 1️⃣ Services
  - Each application instance registers as a service.
  - Can include metadata, health checks, tags.
- 2️⃣ Service Discovery
  - Other services query Consul to find endpoints.
  - Supports DNS, HTTP API, or native SDKs.
- 3️⃣ Health Checks
  - Periodically check if services are alive.
  - If a service fails, it is removed from discovery automatically.
- 4️⃣ Key/Value Store
  - Store application configuration, feature flags, secrets metadata.
  - Accessible via HTTP API or SDK.
- 5️⃣ Consul Agents. Each node runs a Consul agent with two modes:
  - Mode	Role
  - Client	Runs on every node, registers services, forwards queries
  - Server	Maintains cluster state, performs consensus (Raft)

Service Mesh
- Consul supports service-to-service encryption:
- Services communicate via sidecar proxies (Envoy).
- Traffic is encrypted (mTLS).
- Access is policy-controlled.

# Consul vs Kubernetes Service

| Feature                              | Consul                                                           | Kubernetes Service                                                   |
| ------------------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Primary Purpose**                  | Service discovery, service registry, health checks, service mesh | Expose and load-balance pods within a Kubernetes cluster             |
| **Scope**                            | Multi-platform: containers, VMs, databases, bare-metal services  | Kubernetes pods only                                                 |
| **Discovery Method**                 | Central registry + DNS + HTTP API                                | Cluster DNS (CoreDNS) or environment variables                       |
| **Health Checks**                    | Built-in; services self-report via agents                        | Liveness/Readiness probes at pod level, affects endpoints            |
| **Multi-Cluster / Multi-Datacenter** | Built-in support                                                 | Requires additional tools (e.g., federation, external load balancer) |
| **Service-to-Service Encryption**    | Native mTLS with sidecar proxies (service mesh)                  | Not provided natively; needs Istio, Linkerd, or similar              |
| **Service Registration**             | Automatic via Consul agent                                       | Kubernetes automatically exposes pods in a service                   |
| **Platform Agnostic**                | Yes — works across clouds, VMs, containers                       | No — tied to Kubernetes cluster                                      |
| **Dynamic Routing / Load Balancing** | Yes — via service mesh or DNS                                    | Yes — round-robin to pod endpoints within cluster                    |
| **Secret Injection / KV**            | Can integrate with Vault to inject credentials                   | No secret management; Kubernetes Secrets are separate                |

