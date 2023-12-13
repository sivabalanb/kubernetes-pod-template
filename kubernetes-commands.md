
**Basic Commands**

**1. List all pods in the specified namespace:**
```bash
kubectl get pods
```

**2. List all services in the specified namespace:**
```bash
kubectl get services
```

**3. List all Horizontal Pod Autoscalers (HPAs) in the specified namespace:**
```bash
kubectl get hpa
```

**Intermediate Commands**

**4. Forward local port to a pod's specific port:**
```bash
kubectl port-forward pod/my-pod 8080:80
```

**5. Retrieve the stdout and stderr output of a running pod:**
```bash
kubectl logs pod/my-pod
```

**6. List all namespace-specific network policies:**
```bash
kubectl get netpol
```

**7. List all namespace-specific virtual services:**
```bash
kubectl get virtualservices
```

**Advanced Commands**

**8. Create a new pod from the deployment.yaml file:**
```bash
kubectl apply -f deployment.yaml
```

**9. Edit the deployment manifest:**
```bash
kubectl edit deploy my-deployment
```

**10. Create a new network policy to allow traffic from pods with label app=web to pods with label app=backend:**
```bash
kubectl apply -f networkpolicy.yaml
```

**11. Create a new virtual service to route traffic to the pods with label app=frontend:**
```bash
kubectl apply -f virtualservice.yaml
```

**12. List all constraints in the specified namespace, typically for Anthos fixes:**
```bash
kubectl get constraints -n my-namespace
```

This format highlights the executable nature of the commands, making it easier for users to grasp the instructions and apply them effectively.
