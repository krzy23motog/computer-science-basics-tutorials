# Nomad

Nomad is a lightweight, high-performance workload orchestrator developed by HashiCorp.

It schedules and runs applications across clusters of machines — whether they are:
- Virtual machines
- Bare metal servers
- Cloud instances
- Containers

You can think of Nomad as A simpler alternative to Kubernetes that can run containers, VMs, and non-containerized applications.

Core concepts:
- Cluster Architecture: Nomad has two types of nodes:
    - 🧠 Servers
    - Manage cluster state
    - Handle scheduling decisions
    - Use consensus (Raft)
    - ⚙ Clients
    - Run workloads
    - Execute tasks
    - Report health
- Jobs: In Nomad, everything is a Job. A job contains:
  - Task groups
  - Tasks
  - Resource requirements
  - Networking config
  - Jobs are written in HCL (similar to Terraform).

Nomad vs Kubernetes:
| Feature                 | Nomad         | Kubernetes             |
| ----------------------- | ------------- | ---------------------- |
| Complexity              | Simple        | Complex                |
| Installation            | Single binary | Many components        |
| Runs non-container apps | Yes           | No (mostly containers) |
| Learning curve          | Lower         | Higher                 |
| Ecosystem size          | Smaller       | Very large             |

Choose Nomad if:
- You want simplicity
- You run mixed workloads (not only containers)
- You want lightweight orchestration
- You prefer HashiCorp ecosystem integration

Choose Kubernetes if:
- You need huge ecosystem support
- You require advanced container features
- You want community tooling

