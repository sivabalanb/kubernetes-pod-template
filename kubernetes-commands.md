
# Basic Commands

**List all pods in the specified namespace:**
```bash
kubectl get pods
```

**List all services in the specified namespace:**
```bash
kubectl get services
```

**List all Horizontal Pod Autoscalers (HPAs) in the specified namespace:**
```bash
kubectl get hpa
```
**List all services in the specified namespace:**
```bash
kubectl get se
```

# Intermediate Commands

**Forward local port to a pod's specific port:**
```bash
kubectl port-forward pod/my-pod 8080:80
```

**Retrieve the stdout and stderr output of a running pod:**
```bash
kubectl logs pod/my-pod
```

**List all namespace-specific network policies:**
```bash
kubectl get netpol
```

**List all namespace-specific virtual services:**
```bash
kubectl get virtualservices
```

#  Advanced Commands

**Create a new pod from the deployment.yaml file:**
```bash
kubectl apply -f deployment.yaml
```

**Edit the deployment manifest:**
```bash
kubectl edit deploy my-deployment
```

**Create a new network policy to allow traffic from pods with label app=web to pods with label app=backend:**
```bash
kubectl apply -f networkpolicy.yaml
```

**Create a new virtual service to route traffic to the pods with label app=frontend:**
```bash
kubectl apply -f virtualservice.yaml
```

**List all constraints in the specified namespace, typically for Anthos fixes:**
```bash
kubectl get constraints -n my-namespace
```
