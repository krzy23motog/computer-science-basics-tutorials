# Waypoint

Waypoint is an application deployment tool created by HashiCorp that standardizes how developers:
- 🏗 Build applications
- 🚀 Deploy them
- 🌍 Release them

It provides a consistent workflow across platforms like Kubernetes, Nomad, Docker, and cloud services.

Before Waypoint, developers had to:
- Write Dockerfiles
- Write Kubernetes YAML
- Configure CI/CD
- Write Helm charts
- Handle deployment scripts

Waypoint:
- deploys applications on top of infrastructure (created by terraform), 
- manages the full lifecycle of docker containers (build + deploy + release),
- simplifies interacting with Kubernetes.

Core Concepts:
| Stage       | What It Does                             |
| ----------- | ---------------------------------------- |
| **Build**   | Creates an artifact (Docker image, etc.) |
| **Deploy**  | Deploys the artifact to a platform       |
| **Release** | Makes it publicly accessible             |

Where it fits:
| Layer                   | Tool       |
| ----------------------- | ---------- |
| Infrastructure          | Terraform  |
| VM Images               | Packer     |
| App Deployment          | Waypoint   |
| Container Orchestration | Kubernetes |


## Example

Deploy to Kubernetes:
- Waypoint builds a Docker image
- Deploys it to Kubernetes
- Creates a service for external access
    ```
    project = "node-app"

    app "node-app" {
    build {
        use "docker" {}
    }

    deploy {
        use "kubernetes" {
        replicas = 2
        }
    }

    release {
        use "kubernetes" {}
    }
    }
    ```

Deploy to Docker:
```
app "web" {
  build {
    use "docker" {}
  }

  deploy {
    use "docker" {}
  }
}
```









