# Packer

Packer is an open-source tool by HashiCorp used to automate the creation of machine images.
Instead of manually installing software on servers every time, Packer builds a reusable golden image that already contains everything your application needs.

Without Packer:
- You create a VM
- SSH into it
- Install packages
- Configure software
- Save it manually as an image

This process is:
- ❌ Error-prone
- ❌ Slow
- ❌ Hard to reproduce

With Packer:
- You define the image configuration in code
- Run one command
- Get a ready-to-use image

Core Concepts:
- __Builders__: create machine images for specific platforms:
  - Amazon Web Services → AMIs
  - Microsoft Azure → Managed Images
  - Docker → Docker images
  - VMware → VM templates
- __Provisioners__: install and configure software inside the image. Like: Shell scripts, etc.
- __Post-Processors__: used after the image is built (e.g., compressing, exporting, uploading).

## Example

AWS AMI:
```
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  region        = "us-east-1"
  instance_type = "t2.micro"
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      virtualization-type = "hvm"
      root-device-type    = "ebs"
    }
    owners      = ["099720109477"]
    most_recent = true
  }
  ssh_username = "ubuntu"
  ami_name     = "custom-ubuntu-nginx-{{timestamp}}"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx",
      "sudo systemctl enable nginx"
    ]
  }
}
```

Docker Image:
```
source "docker" "nginx" {
  image  = "ubuntu:22.04"
  commit = true
}

build {
  sources = ["source.docker.nginx"]

  provisioner "shell" {
    inline = [
      "apt update",
      "apt install -y nginx"
    ]
  }
}
```

## Packer + Terraform (Common Pattern)

Workflow:
- Packer builds AMI
- Terraform references AMI ID
- Infrastructure launches using golden image

## Packer vs Docker

| Category                      | Packer                               | Docker                                       |
| ----------------------------- | ------------------------------------ | -------------------------------------------- |
| **Primary Purpose**           | Builds machine (VM) images           | Builds container images                      |
| **Scope**                     | Full operating system + software     | Application + dependencies                   |
| **Layer**                     | Infrastructure / OS layer            | Application layer                            |
| **Output Artifact**           | AMI, VM image, template              | Container image                              |
| **Includes OS?**              | Yes (entire OS image)                | No (shares host kernel)                      |
| **Boot Time**                 | VM boot time (slower than container) | Very fast container startup                  |
| **Use Case**                  | Golden images, hardened systems      | Microservices, app packaging                 |
| **Security Control**          | Controls host OS security            | Isolated at container level                  |
| **Cloud Integration**         | Native support for AWS, Azure, GCP   | Runs on any host with Docker                 |
| **Auto Scaling Speed**        | Faster when pre-baked                | Fast containers, but host setup still needed |
| **Best For**                  | Immutable infrastructure             | Portable applications                        |
| **Works Without Containers?** | Yes                                  | No                                           |


