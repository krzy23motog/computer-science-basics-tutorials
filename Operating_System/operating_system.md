# Operating System

## Computer Hardware components

### CPU (central processing unit): 

Executes commands 

Properties:

* cpu cores
* clock speed

#### RAM (random access memory)

Temporarily stores data

Properties:

* size (GB)
* speed

### Video Card

Expansion card that allows the computer to send graphical information to a video display device. All of them contain GPU (graphics processing unit)

Properties:

* outputs (HDMI, DVI etc.)
* RAM

#### Drive or Data storage

Data storage device

HDD (Hard disk drive) or SSD (Solid state drive)

Properties:

* size (GB)
* speed

#### Motherboard: 

## Basic OS concepts

### Definition

An Operting System is the low-level software that supports a computer's basic functions, such as scheduling tasks and controlling peripherals.

### Functions

* Process Management
* I/O Device Management
* File Management
* Network Management
* Main Memory Management

### Links explaining OS basic functions

[OS main concepts](https://www.tutorialspoint.com/operating_system/index.htm)

### Exercises

* Run 'File Explorer' on Windows to see files
* Run 'Device Manager' to see IO devices
* Run 'Resource Monitor' on Windows to see processes
* Run 'Network Status'

## Virtual Machines

### Definition

* A Virtual Machine (VM) is a compute resource that uses software instead of a physical computer to run programs and deploy apps. 
* One or more virtual “guest” machines run on a physical “host” machine.  
* Each virtual machine runs its own operating system and functions separately from the other VM

### why use VMs?

* computer idle time
* reuse of computer resources
* automation
* isolation
* easy migrationto new hardware

### Links explaning VMs basics

[Why VMs are useful](https://www.networkworld.com/article/3583508/what-is-a-virtual-machine-and-why-are-they-so-useful.html)

[Reasons to use VMs](https://www.makeuseof.com/tag/reasons-start-using-virtual-machine/)

## Docker and Containers

### Functions

* Docker enables application portability
* Docker is an open platform for developing, shipping, and running applications. 
* Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
* Docker streamlines the development lifecycle by allowing developers to work in standardized environments using local containers which provide your applications and services.

### Architecture

[Docker architecture](https://geekflare.com/docker-architecture/)

### Docker Desktop

Docker desktop is a GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine. 

[Install docker desktop](https://docs.docker.com/desktop/install/windows-install/)

### Exercise

Find an interesting yes simple docker image in GitHub, run it as a container in docker desktop and use it. If you cannot find it, try to use this one: https://github.com/purrbot-site/ImageAPI

## Windows Command line

### Functions

* work with windows without GUI

### Selected basic commands

* file system: dir, cd, mkdir, rmdir, fc, tree, findstr
* os info: systeminfo, ver, shutdown
* processes: tasklist, taskkill 
* network: netstat, ping, ipconfig 
* programing: set, echo

### links to check about windows cmd

* [Short video about windows cmd](https://www.youtube.com/watch?v=A3nwRCV-bTU)
* [Windows cmd examples](https://www.makeuseof.com/tag/windows-batch-if-statements/?newsletter_popup=1)
* [More Windows cmd examples](https://github.com/Richu-Antony/Usefull-Windows-Scripts-and-Applications)

### Exercises

Create and run a simple .bat script. See [.bat script tutorial](https://www.howtogeek.com/263177/how-to-write-a-batch-script-on-windows/)
