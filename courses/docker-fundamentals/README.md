# Docker Fundamentals

## Summary
This course is designed to familiarize students with the benefits of containerization for both systems and application design. Hardware virtualization brought along a new era of server management and application architecture, by allowing companies to more rapidly plan and migrate environments.

The introduction of lighter weight virtualized systems, called “containers”, has finally achieved the goal of hardware agnosticism. Docker, introduced in 2013, has become an unofficial standard for building, deploying, and managing these containers.Through a series of hands-on, guided sections, students will first absorb and then put into practice the tools needed to bring the virtualization revolution back with them.

## Course Outline

### Introduction to microservices
Benefits and disadvantages
What considerations must be taken into account to manage their production workloads and development lifecycle. 
Stateless applications, being cloud-native, auto-scaling and healing, and service discovery
Infrastructure-as-code concepts
Disposable infrastructure

### Introduction to containerization and Docker
Concepts
Background and history
Levels of virtualization – bare-metal, virtual machine, container
Alternatives
Portability
Isolation with kernel namespaces and cgroups
Uses for containers - microservices, batch jobs, local utilities, etc.
Security considerations

### Docker Images
Basic concepts
Immutability
Layers
Single process and use of systemd
Building from containers, but discussion of why Dockerfile is the way
Dockerfile
Anatomy and important instructions
Building from Dockerfile
Operations on images
Multi-stage builds
What is Docker Hub and how to use it
Tagging
Managing images - removing, cleaning up, managing tags, etc

### Docker Containers
Basic concepts
Difference between images and containers
Isolation
Ability to run same image multiple times on same host (port mapping concepts)
Running containers
Container inputs - environment variables, port mapping, etc.
Volumes and persistence
Exploring containers - logs, bash shell
Managing container lifecycle and execution
Restart policies

### Advanced Docker Topics
Networks and container communication
Running as non-root user
Lightweight or slim Docker images with Alpine, Debian Slim, etc
Using private registries and repositories
Tagging relationship
Authenticating
Implications with CI/CD systems and pipeline overview

### Docker Compose
Basic concepts and relationship to basic Docker usage
Use as a lightweight alternative to full orchestration on local workstation
Walkthrough of a running multi-container application

### Introduction to container orchestration
Basic concepts
Manually running containers vs. Compose vs. true orchestration
Scaling, healing, deploying, etc.
Load balancing, geographic distribution
Orchestration options - Swarm, Kubernetes, mention of others
Kubernetes overview
architecture(apiserver, controller manager, scheduler, kubelet and their interaction)
Clusters, nodes, master components
Pods, services, replicasets, deployments
Discussion of Kubernetes course available
