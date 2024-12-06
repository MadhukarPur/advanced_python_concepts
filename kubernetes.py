# Kubernetes Basics
'''
    What is Kubernetes?
        -- Kubernetes (K8s) is an open-source platform for automating the deployment, scaling, and management of 
        containerized applications.
        -- Kubernetes is a container orchestration platform. It helps manage containers across multiple hosts, 
        ensuring they run efficiently, are fault-tolerant, and can scale as needed.

    Key Features:
        -- Container Orchestration: 
                Manages container deployment, scaling, and operation.
        -- Load Balancing: 
                Distributes traffic across containers.
        -- Self-Healing: 
                Automatically restarts failed containers.
        -- Scalability: 
                Dynamically scale applications up or down.
        -- Storage Orchestration: 
                Mounts storage systems like AWS, GCP, or on-prem solutions.

    Key Kubernetes Concepts:
        a. Nodes
            A Node is a machine (physical or virtual) in a Kubernetes cluster that runs containerized applications.

        b. Cluster
            A Cluster is a group of nodes managed by Kubernetes.

        c. Pod
            A Pod is the smallest deployable unit in Kubernetes. It encapsulates one or more containers that share resources like storage, networking, and configurations.

        d. Deployment
            A Deployment defines how Pods are created, updated, and managed.

        e. Service
            A Service exposes Pods to the outside world or within the cluster.

        f. ConfigMap and Secret
            ConfigMap: Stores configuration data for applications.
            Secret: Stores sensitive data like passwords.
'''