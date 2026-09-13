# AWS Interview questions

## Table of contents

- [How do you run serverless container on aws](#how-do-you-run-serverless-container-on-aws)
  - [AWS App Runner](#aws-app-runner)
  - [Amazon ECS with Fargate](#amazon-ecs-with-fargate)
  - [AWS Lambda (Container Image mode)](#aws-lambda-container-image-mode)
  - [Amazon EKS](#amazon-eks)
  - [Comparison](#comparison)
- [AWS Reference architectures](#aws-reference-architectures)
  - [3-Tier Web Application](#3-tier-web-application-route-53-→-cloudfront-→-alb-→-ec2ecs-→-rds)
  - [Serverless Web Application](#serverless-web-application-cloudfront-→-s3-→-api-gateway-→-lambda-→-dynamodb)
  - [Modern Containerized Application](#modern-containerized-application-alb-→-ecsfargate-or-eks-→-rdsdynamodb-→-sqseventbridge)
  - [Data Lake / Analytics Architecture](#data-lake--analytics-architecture-s3-→-glue-→-athenaredshift-→-lake-formation-→-quicksight)
  - [Hybrid Cloud Architecture](#hybrid-cloud-architecture-data-center-→-direct-connectvpn-→-transit-gateway-→-vpcs)
- [Kubernetes / EKS architecture](#explain-in-detail-and-with-examples-kubernetes--eks-architecture-including-multi-cluster-management-and-stateful-workloads)
  - [1. Kubernetes Core Architecture](#1-kubernetes-core-architecture)
  - [2. EKS-Specific Architecture](#2-eks-specific-architecture)
  - [3. Multi-Cluster Management in Kubernetes](#3-multi-cluster-management-in-kubernetes)
  - [4. Managing Stateful Workloads in Kubernetes](#4-managing-stateful-workloads-in-kubernetes)
- [AWS Well-Architected Framework pillars](#list-and-explain-aws-well-architected-framework-pillars)
  - [Operational Excellence](#operational-excellence)
  - [Security](#security)
  - [Reliability](#reliability)
  - [Performance Efficiency](#performance-efficiency)
  - [Cost Optimization](#cost-optimization)

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

## AWS Reference architectures

### 3-Tier Web Application: Route 53 → CloudFront → ALB → EC2/ECS → RDS

- Cognito: 
  ```
                      1. Login
  Browser ─────────────────────────► Cognito
                                        │
                                        │ 2. Authenticate
                                        ▼
                                    User verified
                                        │
                                        │ 3. JWTs
                                        ▼
  Browser ◄───────────────────────── Cognito

  ```
- Route 53 = DNS
  - can point to: CloudFront, ALB, NLB, API Gateway, S3
  - direct users toward a healthy region.
  - AWS shield - DDOS protection
- CloudFront = CDN
  - caching, https, geo-drstribution, WAF for security (sql injection, eate limiting, IP reputation)
  - can send origin traffic to: S3, ALB, NLB, API Gateway, Lambda
  - can do https -> http translation (not good idea)
  - multiple origins and use origin groups for failover: 
    - Primary origin → Region A
    - Secondary origin → Region B
  - use CloudFront even if you don't want your application responses cached: 
    - It's also a global reverse proxy and edge security layer.
    - it provides: AWS WAF integration, DDoS protection, Global edge network connectivity
- ALB:
  - public VPC subnet + security groups
  - ALB can terminate HTTPS and send HTTP to your backend.
  - Cannot throttle - use WAF
  - Send traffic to: EC2, ECS/EKS, Lambda
  - enforce authentication (JWT bearer token)
  - ALB vs API Gateway: 
    - API Gateway is generally more API-focused and provides features such as API management, authorization options, throttling, stages, etc.
    - ALB is more oriented toward load balancing HTTP applications and can unify Lambda, EC2, and containers behind the same load-balancing model.
- EC2:
  - 2 or more AZ, separate private subnets, same VPC
  - security groups
  - TLS / HTTPS everywhere
  - REST API - authorizes (validates) user using JWT bearer token: enforce business authorization
- RDS
  - separate subnet
  - Secrets Manager
  - encryption at rest and flight
  - automated backups

### Serverless Web Application: CloudFront → S3 → API Gateway → Lambda → DynamoDB

- CloudFront
- S3
  - stores your frontend files (React/Vue/Angular)
  - it is not publiclty accessible, only through CloudFront
  - CloudFront → S3 → uses an Origin Access Control (OAC),
  - S3 is your frontend's storage/origin
- API Gateway = front door for your backend APIs
  - routes, http translation, defines endpoints, authentication/authorization, throtteling, 
  - sends traffic to: lambda, AWS services, http endpoints, VPC/private backends
  - enforce authentication
- Lambda
  - Lambda isn't normally exposed as your application's HTTP API.
  - Event-driven
  - enforce business authorization


### Modern Containerized Application: ALB → ECS/Fargate or EKS → RDS/DynamoDB → SQS/EventBridge

- ECS — Running your containers
  - ECS + EC2 = You manage the underlying EC2 capacity.
    - An ECS task is essentially a running instance of your containerized workload according to an ECS task definition.
  - ECS + Fargate = AWS manages the underlying compute infrastructure
- SQS:
  - after creating the order, you need to: send an email, update inventory, generate an invoice
- EventBridge: one event can be consumed by multiple consumers

Typically: 
```
             ┌──► SQS → Worker A
             │
SNS ─────────┼──► SQS → Worker B
             │
             └──► SQS → Worker C

```

```
                   EventBridge
                  /     |      \
                 ▼      ▼       ▼
             Inventory Email  Analytics
             
             OR

                     EventBridge
                    /     |      \
                   ▼      ▼       ▼
                 SQS    SQS     Lambda
                  │      │
                  ▼      ▼
             Inventory  Email
```

SNS and EventBridge look very similar because both can fan one event out to multiple consumers. The important difference is what problem they are designed to solve.
- SNS is primarily a pub/sub fan-out system
- EventBridge is primarily an event router: I have an event. Look at what's inside it and decide where it should go

### Data Lake / Analytics Architecture: S3 → Glue → Athena/Redshift → Lake Formation → QuickSight
### Hybrid Cloud Architecture: Data Center → Direct Connect/VPN → Transit Gateway → VPCs


## Explain in detail and with examples Kubernetes / EKS architecture, including multi-cluster management and stateful workloads.

Kubernetes (K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Amazon EKS (Elastic Kubernetes Service) is a fully managed Kubernetes service offered by AWS, which simplifies the operation of Kubernetes clusters in the cloud.

To fully understand Kubernetes architecture, including multi-cluster management and stateful workloads, let’s break it down in detail:

### 1. Kubernetes Core Architecture

At a high level, Kubernetes is designed to run containerized applications across a cluster of machines (physical or virtual). The architecture consists of two main components:

- Control Plane: Manages the state of the cluster (e.g., scheduling, scaling, maintaining desired state).
- Worker Nodes: Run containerized applications (pods) and are responsible for executing application workloads.

Control Plane Components: These components are responsible for making global decisions about the cluster (e.g., scheduling, managing workloads) and ensuring that the cluster is healthy and meets the desired state.
- API Server (kube-apiserver):
  - The API server is the front-end for the Kubernetes control plane. It exposes the Kubernetes API, allowing users, components, and external clients to interact with the cluster.
  - Example: The kubectl command-line tool communicates with the API server to deploy, manage, and monitor applications.
- Controller Manager (kube-controller-manager):
  - The controller manager ensures that the desired state of the cluster matches the actual state. It includes controllers for handling tasks like node management, deployment updates, etc.
  - Example: If a pod fails or becomes unhealthy, the controller will attempt to create a new pod to maintain the desired number of replicas.
- Scheduler (kube-scheduler): The scheduler assigns pods to specific nodes based on resource requirements and availability.
  - Example: When a new pod is created, the scheduler will decide which node to run the pod on, considering factors like resource utilization (CPU, memory), affinity rules, and node health.
- etcd: is a distributed key-value store used to store all cluster data, including configurations, secrets, and the current state of the system (e.g., pod configurations, deployment information).
  - Example: When you apply a deployment via kubectl, Kubernetes stores the configuration in etcd, and the system works to match the desired state.

Worker Node Components:
- Worker nodes are the machines where your containerized applications (pods) run. Each worker node has the following key components:
  - Kubelet: The kubelet is an agent running on each worker node that ensures containers are running in a pod.
  - Example: The kubelet ensures that the necessary containers in a pod are running and healthy by interacting with the container runtime (e.g., Docker, containerd).
- Kube Proxy:
  - The kube proxy is responsible for network routing and load balancing for services. It manages the network rules on each node to allow communication between pods and services.
  - Example: If there are two pods running a web application, the kube proxy ensures traffic is routed correctly to the right pod based on the service’s configuration.
- Container Runtime:
  - The container runtime (e.g., Docker, containerd) is responsible for running containers on the worker node.
  - Example: When a pod is scheduled on a node, the container runtime ensures that the container(s) defined in the pod’s specification are created and started.

### 2. EKS-Specific Architecture

AWS provides EKS as a fully managed Kubernetes service, where much of the control plane is handled by AWS. When you use EKS, AWS manages the Kubernetes control plane, including the API server, controller manager, and scheduler. This reduces the operational overhead, but you still manage the worker nodes (either EC2 instances or managed node groups).

- Control Plane Managed by AWS: In EKS, the Kubernetes control plane (API server, scheduler, controller manager, etc.) is managed by AWS, ensuring it is highly available, scalable, and patched. AWS takes care of the heavy lifting, such as cluster upgrades and failover.
- Worker Nodes: You can choose to run your worker nodes as EC2 instances or use EKS Managed Node Groups, where AWS automatically manages the EC2 instances on your behalf.

Example:
- EKS Cluster: You create a Kubernetes cluster using EKS, which provisions the control plane on your behalf. You then deploy worker nodes (either EC2 instances or managed node groups) into your VPC (Virtual Private Cloud).
- Multi-AZ Setup: EKS automatically distributes the control plane across multiple availability zones (AZs) for high availability and fault tolerance.
- Node Scaling: If your cluster requires more capacity, you can either scale the worker nodes manually or use EKS Auto Scaling to dynamically adjust the number of worker nodes based on demand.

### 3. Multi-Cluster Management in Kubernetes

In larger organizations, a single Kubernetes cluster may not meet the needs of all workloads or teams. In such cases, multi-cluster management becomes necessary, especially in distributed applications, global deployments, or for disaster recovery purposes.

Why Use Multi-Cluster Setup?
- Fault Isolation: Isolate workloads and mitigate the impact of failures (e.g., if one cluster fails, the others remain unaffected).
- Geographic Distribution: Deploy applications closer to end-users to reduce latency by having clusters in multiple regions or availability zones.
- Resource Management: Different clusters can be used for different environments (e.g., production, staging, testing) or different teams within an organization.

Managing Multiple Clusters:
- Kubernetes Federation:
  - Kubernetes Federation allows you to manage multiple clusters as if they were a single entity. You can federate resources across clusters, synchronize configurations, and deploy workloads across clusters.
  - Example: You might deploy your frontend in one cluster located in the US and your backend in another cluster located in Europe for better user experience.
- Cross-Cluster Communication:
  - Use Istio or Linkerd for service mesh capabilities, enabling secure and efficient communication between services in different clusters.
  - Example: A service in Cluster A might need to communicate with a service in Cluster B. With Istio, you can configure the mesh to route traffic securely between clusters.
- Centralized Management Tools:
  - Use AWS EKS Anywhere or Rancher for centralized multi-cluster management. These tools provide a unified interface to manage clusters across different environments.
  - Example: With Rancher, you can monitor, deploy, and manage multiple Kubernetes clusters across different cloud providers or on-premises environments.

Example: Managing Multiple EKS Clusters:
- Cluster in Different Regions: Deploy multiple EKS clusters in different AWS regions to reduce latency for users in different geographic locations.
- Cross-Cluster Communication: Use Service Mesh like Istio to allow services in Cluster 1 (US West) to communicate with services in Cluster 2 (US East).

### 4. Managing Stateful Workloads in Kubernetes

Kubernetes is commonly associated with stateless applications, but it also provides powerful features to support stateful workloads that need persistent storage.

StatefulSet:
- StatefulSet is a Kubernetes controller designed specifically for stateful applications. It ensures the ordering and uniqueness of pods, which is critical for applications that need stable network identities and persistent storage.
- Key Features:
  - Stable Persistent Storage: Ensures that each pod gets a persistent volume (PV) that survives pod restarts.
  - Stable Network Identity: Each pod in a StatefulSet gets a unique DNS hostname, which is important for applications like databases that need to track their peers.
  - Ordered Deployment and Scaling: Pods in a StatefulSet are deployed in a specific order (e.g., Pod 1 is created before Pod 2) and are terminated in the reverse order.

Example Use Case:
- A StatefulSet can be used to deploy a MySQL or Cassandra cluster. These databases require stable network identities for replication and persistent volumes for data storage. StatefulSets provide the necessary guarantees for such workloads.

Persistent Volumes (PVs) and Persistent Volume Claims (PVCs):
- Kubernetes provides Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) to manage storage for stateful workloads.
- PVs are abstractions that represent physical storage in the cluster, which could be backed by AWS services like EBS (Elastic Block Store), EFS (Elastic File System), or EFS CSI.
- PVCs are requests for storage made by users or pods. When a StatefulSet is created, it requests persistent storage through PVCs.

Example:
- For a MySQL database, a StatefulSet will request a PVC for each pod in the set. Kubernetes will then provision the necessary EBS volumes for each pod, ensuring that even if the pod is rescheduled or restarted, the data is retained.

## List and explain aws Well-Architected Framework pillars

### Operational Excellence

Run and monitor systems effectively; continuously improve processes and operations.

Build systems that are easy to operate, monitor, troubleshoot, and improve.

1. Prepare
- Defining business and operational requirements
- Creating runbooks and playbooks
- Establishing monitoring and alerting
- Planning for failures and operational events
2. Operate
- Monitoring application and infrastructure metrics
- Collecting logs and traces
- Setting up alerts
- Automating deployments
- Automating routine operational tasks
3. Evolve
- What went wrong?
- Why did it happen?
- Could we have detected it earlier?
- Can we automate the recovery?

### Security

Protect data, systems, and resources through identity management, detection, infrastructure protection, and incident response.

**Protect your systems and data by controlling access, detecting threats, protecting infrastructure, and responding to security incidents.**

1. Identity and Access Management
- Use **AWS Identity and Access Management (IAM)**.
- Follow the **principle of least privilege**.
- Avoid using the AWS root user for daily activities.
- Use roles instead of long-term access keys where possible.
2. Detection
- Monitor AWS API activity.
- Monitor logs and security events.
- Create alerts for suspicious activity.
- Detect unusual access patterns.
3. Infrastructure Protection
- Use network security controls.
- Restrict inbound and outbound traffic.
- Use private subnets for resources that don't need direct internet access.
- Use security groups and network ACLs appropriately.
- Protect applications from common network attacks.
4. Data Protection
- Data at Rest
- Data in Transit
5. Incident Response
- Prepare an incident response plan.
- Automate responses where possible.
- Define who is responsible for each action.
- Isolate compromised resources.
- Investigate the incident.


### Reliability

Ensure workloads perform correctly and recover quickly from failures.

The **Reliability** pillar focuses on ensuring that a workload:
- Performs its intended function correctly
- Can recover quickly from failures
- Can handle changes in demand
- Can meet business requirements consistently

1. Foundations
- Understand service quotas and limits.
- Define operational requirements.
- Establish monitoring and alerting.
2. Workload Architecture
- Avoid Single Points of Failure
3. Change Management
- Automate deployments.
- Test changes before production.
- Make small, reversible changes.
- Monitor deployments.
- Have a rollback strategy.
- Use Infrastructure as Code.
4. Failure Management
- Anticipate failures
- Detect failures
- Respond to failures
- Recover from failures
- Prevent similar failures in the future


### Performance Efficiency

Use computing resources efficiently and adapt resources as requirements change.

1. Selection: Choose AWS resources based on the actual workload requirements.
  - CPU-intensive workload -> Compute-optimized instance
  - Memory-intensive workload  -> Memory-optimized instance
  - Choosing the Right Compute Resources
    - Amazon EC2
    - Amazon ECS
    - Amazon EKS
    - AWS Lambda
    - AWS Fargate
2. Review: Regularly review your architecture and resource choices.
3. Monitoring
  - Identify Bottlenecks
4. Tradeoffs
5. Evolution

```
Performance Efficiency =

Choose the Right Resource
          ↓
Right-Size
          ↓
Monitor
          ↓
Find Bottlenecks
          ↓
Optimize
          ↓
Scale
          ↓
Review & Evolve

```

### Cost Optimization

Deliver business value at the lowest appropriate cost.

1. Practice Cloud Financial Management
  - who, what, why
  - cost allocation tags: application, team, project, environment, department
2. Expenditure and Usage Awareness
  - monitoring
  - set budgets
3. Cost-Effective Resources
4. Manage Demand and Supply Resources
  - remove unused resources
  - savings plans, reservered, spot
  - auto-scaling
  - serverless
5. Optimize Over Time
