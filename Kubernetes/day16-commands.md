# Day 16 - Kubernetes Basics

## What is Kubernetes?
Kubernetes (K8s) is a container orchestration platform that manages 
containers at scale across multiple servers.

Docker handles "how to run a container"
Kubernetes handles:
- Where to run it
- How many copies
- What to do if it crashes
- How to expose it to users

## Docker vs Kubernetes
| | Docker | Kubernetes |
|--|--------|-----------|
| What | Runs containers | Manages containers at scale |
| Scale | One server | Multiple servers |
| Self healing | No | Yes |
| Auto scaling | No | Yes |
| Load balancing | No | Yes |
| Rolling updates | No | Yes |

## Real World Analogy
Hospital analogy:
- Hospital building = Kubernetes cluster
- Wards/floors      = Nodes (servers)
- Patients          = Containers
- Hospital manager  = Kubernetes control plane
- Nurse             = Kubelet

## Key Concepts

### 1. Cluster
A group of servers working together
Like a hospital with multiple buildings

### 2. Node
A single server inside the cluster
Like one building in the hospital
Two types:
- Control plane = brain, makes all decisions
- Worker node   = runs actual containers

### 3. Pod
Smallest unit in Kubernetes
One or more containers running together
Temporary — if crashes without Deployment, gone forever!

### 4. Deployment
Manages pods
Ensures desired number of pods always running
If pod crashes — creates new one automatically
You never create pods directly — always create Deployments!

### 5. Service
Exposes your pods to outside world
Types:
- ClusterIP   = internal only, pods talk to each other
- NodePort    = external access via node IP + port
- LoadBalancer = creates cloud load balancer (production)

### 6. Control Plane Components
| Component | Purpose |
|-----------|---------|
| etcd | K8s database — stores all cluster data |
| kube-apiserver | Handles all kubectl commands |
| kube-scheduler | Decides which node to run pods on |
| kube-controller-manager | Manages deployments and replicas |

## kubectl — Kubernetes CLI
kubectl is the command line tool for Kubernetes
Same relationship as:
- AWS     → aws cli
- Docker  → docker command
- K8s     → kubectl

## Commands Learned

### Check nodes
```bash
kubectl get nodes
```

### Create deployment
```bash
kubectl create deployment my-app --image=nginx
```

### Get pods
```bash
kubectl get pods
```

### Self Healing — Delete pod and K8s recreates it!
```bash
kubectl delete pod <pod-name>
kubectl get pods  # new pod created automatically!
```

### Scale deployment
```bash
kubectl scale deployment my-app --replicas=3
```

### Expose deployment
```bash
kubectl expose deployment my-app --port=80 --type=NodePort
```

### Get services
```bash
kubectl get service
```

### Access app
```bash
curl http://node01:31955
```

### Describe pod — detailed info and events
```bash
kubectl describe pod <pod-name>
```

### Pod logs — debug app issues
```bash
kubectl logs <pod-name>
```

### Get everything at once
```bash
kubectl get all
```

## Key Features Demonstrated

### Self Healing
Deployment says "I want 1 pod always running"
You delete the pod
Deployment notices "I have 0 pods, I need 1!"
Automatically creates new pod in seconds!
No human intervention needed!

### Scaling
One command goes from 1 pod to 3 pods
Load balanced automatically across all pods
In real production:
- Low traffic  = scale down (save money)
- High traffic = scale up (handle load)

## Interview Answers

Q: What is Kubernetes?
A: Kubernetes is a container orchestration platform that manages 
containers at scale. While Docker handles running individual containers, 
Kubernetes handles where to run them, how many copies, self healing 
when they crash and load balancing traffic across them.

Q: What is the difference between Pod and Deployment?
A: A Pod is the smallest unit that runs containers but is temporary. 
A Deployment manages pods and ensures the desired number always runs. 
If a pod crashes, the Deployment automatically creates a new one. 
You should always create Deployments, not pods directly.

Q: What is self healing in Kubernetes?
A: When a pod crashes or is deleted, the Deployment controller detects 
the difference between desired state and actual state and automatically 
creates a new pod. This happens within seconds without human intervention.

Q: What are the different Service types?
A: ClusterIP exposes service only inside cluster for internal 
communication. NodePort exposes service on a port on each node for 
external access during testing. LoadBalancer provisions a cloud load 
balancer for production use on AWS or GCP.
```
