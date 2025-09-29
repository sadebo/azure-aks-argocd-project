# Azure AKS + ArgoCD Project

## Overview
This repo provisions **Azure AKS + ACR (`parallelacr9875`)** with Terraform, bootstraps ingress/cert-manager/ArgoCD, and manages app deployments with ArgoCD.

## Steps
1. `cd terraform && terraform init && terraform apply`
2. `az aks get-credentials -g aks-rg -n aks-demo`
3. Bootstrap cluster:
   ```bash
   kubectl apply -f bootstrap/ingress-nginx.yaml
   kubectl apply -f bootstrap/cert-manager.yaml
   kubectl apply -f bootstrap/argocd-core.yaml
