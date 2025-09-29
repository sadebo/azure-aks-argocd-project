# Azure AKS + ArgoCD Project

## Overview
This repo provisions **Azure AKS + ACR (`parallelacr9875`)** with Terraform, bootstraps ingress/cert-manager/ArgoCD, and manages app deployments with ArgoCD.

📂 Repository Structure

## 📂 Repository Structure

```text
azure-aks-argocd-project/
├── app/                      # Sample Flask app
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── terraform/                # AKS + ACR infrastructure
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── providers.tf
│   └── backend.tf
│
├── bootstrap/                # Cluster bootstrap manifests
│   ├── ingress-nginx.yaml
│   ├── cert-manager.yaml
│   ├── cert-manager-crds.yaml
│   ├── argocd-core.yaml
│   └── letsencrypt-clusterissuer.yaml
│
├── argocd/                   # ArgoCD config
│   ├── projects/
│   │   └── default-project.yaml
│   └── applications/
│       ├── flask-app.yaml
│       └── redis.yaml
│
├── helm-charts/              # Helm charts for apps
│   ├── flask-app/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── deployment.yaml
│   │       ├── service.yaml
│   │       └── ingress.yaml
│   └── redis/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           └── deployment.yaml
│
├── .github/workflows/
│   └── deploy.yaml           # CI/CD pipeline
│
└── README.md                 # This file



🛠 Prerequisites

Azure subscription (with $200 free credit works for this POC).

GitHub repo with this code.

GitHub Secrets configured:

ARM_CLIENT_ID

ARM_CLIENT_SECRET

ARM_SUBSCRIPTION_ID

ARM_TENANT_ID

GITHUB_PAT (Personal Access Token with repo scope, for ArgoCD to pull manifests).

⚙️ Deployment Flow

GitHub Actions Workflow (deploy.yaml)
Provisions AKS + ACR via Terraform.
Builds Flask app image → pushes to ACR (parallelacr9875.azurecr.io/flask-app:v1).
Deploys bootstrap components:

* ingress-nginx

* cert-manager (with CRDs)

* argocd

* Creates Let’s Encrypt ClusterIssuer.

* Fetches ArgoCD admin password → saves as artifact.

* Logs into ArgoCD via CLI.

* Registers this GitHub repo in ArgoCD.

* Applies projects/ + applications/.

* ArgoCD

* Syncs flask-app + redis applications from Helm charts.

*Creates TLS certificates via cert-manager.

* Exposes apps over Ingress:

* https://argocd.parallelservicesllc.com

* https://flask.parallelservicesllc.com

🔑 Accessing ArgoCD

Fetch the ArgoCD password:

kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

Or download from GitHub Actions artifact.

Login:

URL: https://argocd.parallelservicesllc.com

Username: admin

Password: (from step above)

🔒 TLS & Cert-Manager

Certificates are issued by Let’s Encrypt via HTTP-01 challenge.

Critical ingress annotations:

annotations:
  kubernetes.io/ingress.class: nginx
  cert-manager.io/cluster-issuer: letsencrypt-prod
  nginx.ingress.kubernetes.io/ssl-redirect: "true"
  nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
  nginx.ingress.kubernetes.io/acme-http01-edit-in-place: "true"


Without the last annotation, cert-manager HTTP-01 self-check fails due to HTTPS redirect.

🐳 Sample Flask App

Simple Flask API with /healthz for readiness probes.

Connects to Redis via:

REDIS_HOST=redis.default.svc.cluster.local
REDIS_PORT=6379

🧩 Redis

Deployed via custom Helm chart (helm-charts/redis).
Exposed as ClusterIP service at redis.default.svc.cluster.local.

✅ Verification

Check ArgoCD Applications:
argocd app list

Verify TLS:
kubectl describe certificate flask-tls -n default

Test app:
curl -vk https://flask.parallelservicesllc.com/healthz

🧹 Teardown

Run the destroy workflow or manually:
cd terraform
terraform destroy -auto-approve
