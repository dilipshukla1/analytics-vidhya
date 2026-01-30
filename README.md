# Analytics Web Application

This repository contains a full-stack analytics web application, including:

- **Frontend SPA** served via Nginx
- **Backend Django REST API** with GraphQL support
- **Identity management** for user authentication and profiles
- **Kubernetes deployment manifests** (`all.yaml`) for frontend, backend, services, and NLB
- **KEDA integration** for backend autoscaling
- **Docker support** for local and production environments

---

## Repository Structure

frontend/ # Frontend SPA code and Nginx config
graphql_api/ # GraphQL API schema
identity/ # Django app for authentication
newidentity2/ # Django project (settings, urls, wsgi)
keda/ # KEDA manifests for backend autoscaling
Dockerfile # Root Dockerfile
docker-compose.yml # Docker Compose for local dev
requirements.txt # Python dependencies
manage.py # Django management script
all.yaml # Kubernetes manifests (frontend + backend + services + NLB)

yaml
Copy code

---

## Features

- User login via `/api/login/`
- User profile via `/api/user-rest-galaxy/profile/`
- Frontend served via Nginx, proxying `/api/...` requests to backend
- Backend Django + Gunicorn, 2 replicas by default
- GraphQL support for analytics queries
- Kubernetes manifests include ConfigMap, Deployments, Services, and NLB
- KEDA autoscaling for backend pods
- Session management with cookies forwarded from frontend to backend

---

## Prerequisites

- Docker
- Docker Compose
- Kubernetes cluster (EKS, k3s, Minikube, etc.)
- `kubectl` configured for your cluster
- Optional: KEDA installed for backend autoscaling

---

## Running Locally with Docker Compose

```bash
docker-compose build
docker-compose up -d
Access frontend at:

arduino
Copy code
http://localhost:80
Quick Start – Deploy on Kubernetes with KEDA
Apply all Kubernetes manifests:

bash
Copy code
kubectl apply -f all.yaml
Restart frontend to pick up Nginx config:

bash
Copy code
kubectl rollout restart deployment analytics-frontend -n analytics
Verify deployments and services:

bash
Copy code
kubectl get all -n analytics
Frontend exposed via NLB (analytics-frontend-nlb)

Backend runs on ClusterIP (backend-service)

KEDA automatically scales backend pods based on metrics

Nginx Configuration
Frontend SPA served from /usr/share/nginx/html.

API requests (/api/...) are proxied to backend.

Cookies are forwarded for session authentication.

nginx
Copy code
location /api/ {
    proxy_pass http://backend-service:8000/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Cookie $http_cookie;
}
KEDA Autoscaling
Backend deployment can scale dynamically based on metrics.

Example triggers:

CPU usage

Memory usage

Queue length (SQS, RabbitMQ, Kafka, etc.)

Example ScaledObject
yaml
Copy code
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: analytics-backend-scaler
  namespace: analytics
spec:
  scaleTargetRef:
    name: analytics-backend
  minReplicaCount: 2
  maxReplicaCount: 10
  triggers:
  - type: cpu
    metadata:
      type: Utilization
      value: "50"
KEDA must be installed in the cluster before applying ScaledObjects.

Backend pods will autoscale automatically based on configured metrics.

API Endpoints
Endpoint	Method	Description
/api/login/	POST	User login
/api/user-rest-galaxy/profile/	GET	Get user profile
/admin/	GET	Django admin panel

Testing Endpoints
bash
Copy code
# Test login
kubectl exec -it -n analytics deploy/analytics-frontend -- curl -v http://backend-service:8000/api/login/

# Test profile
kubectl exec -it -n analytics deploy/analytics-frontend -- curl -v http://backend-service:8000/api/user-rest-galaxy/profile/
