
# Cloud-Native DevOps Starter (Portfolio Project)

A small but complete **DevOps portfolio project** you can show to employers. It demonstrates containerization, CI/CD, Kubernetes, GitOps-ready layout, basic monitoring hooks, and infrastructure-as-code stubs.

## 🔧 Tech Stack
- **Python Flask** sample app (minimal business logic)
- **Docker** (multi-stage build)
- **Pytest** (unit tests)
- **GitHub Actions** for CI (lint → test → build → push to GHCR) and CD (kubectl apply or Argo CD-ready)
- **Kubernetes** manifests with **Kustomize** overlays for `dev` and `prod`
- **Ingress** scaffold (Nginx Ingress assumed)
- **Makefile** helpers
- **Terraform stub** ready for AWS (backend + EKS/ECR placeholders)
- **Security**: Trivy image scan stage in CI (optional / enabled by default)

> Want to keep costs at **zero** while practicing? Use **kind** or **minikube** locally and push images to **GitHub Container Registry (GHCR)**.

---

## 🗺️ Architecture (high-level)

```
Developer -> GitHub (repo)
   |           |
   |       GitHub Actions (CI)
   |           |-- lint & test
   |           |-- build & push (GHCR)
   |           '-- trivy scan
   |
k8s cluster <- CD (manual, env-protected) ---- apply k8s/overlays/{dev,prod}
   |
   +-- Deployment + Service + Ingress
```

---

## 📂 Repository Structure

```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── tests/
│   └── test_app.py
├── k8s/
│   ├── base/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   └── overlays/
│       ├── dev/
│       │   └── kustomization.yaml
│       └── prod/
│           └── kustomization.yaml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── infra/
│   └── terraform/
│       └── README.md
├── docker-compose.yaml
├── Makefile
└── README.md
```

---

## 🚀 Quick Start (Local)

1) **Prereqs**
- Docker / Docker Desktop
- Python 3.11+ (optional, for local run without Docker)

2) **Run tests locally**

```bash
pip install -r app/requirements.txt
pip install -r tests/requirements.txt
pytest -q
```

3) **Build & run with Docker**

```bash
docker build -t ghcr.io/USERNAME/devops-portfolio:local ./app
docker run -p 8000:8000 ghcr.io/USERNAME/devops-portfolio:local
# open http://localhost:8000/health
```

4) **Compose (app + future addons)**

```bash
docker compose up --build
```

---

## ☸️ Kubernetes (with Kustomize)

- **Base** holds common manifests.
- **Overlays** hold env-specific patches (image tag, replicas, annotations).

### Apply to dev
```bash
kubectl apply -k k8s/overlays/dev
```

### Apply to prod
```bash
kubectl apply -k k8s/overlays/prod
```

> Assumes you have an Ingress controller (e.g., **ingress-nginx**) and a DNS entry pointing to it for prod.

---

## 🔁 CI/CD

- **CI (`.github/workflows/ci.yml`)**
  - Lint (flake8)
  - Test (pytest + coverage)
  - Build container
  - **Trivy** scan
  - Push to **GHCR** (tags: `sha`, `latest` for default branch)

- **CD (`.github/workflows/cd.yml`)**
  - Manual dispatch + env protection
  - Uses `kubectl` to apply Kustomize overlay (you provide kubeconfig via secrets)
  - Optional: Swap to **Argo CD** (GitOps) later; keep manifests in a separate **ops** repo.

### Required GitHub secrets
- `GHCR_USERNAME` – your GitHub username
- `GHCR_TOKEN` – a PAT with `write:packages`, `read:packages`
- `KUBE_CONFIG` – base64 of a kubeconfig for your cluster (for CD)
- *(optional)* `TRIVY_DB_REPOSITORY` to speed up scans

---

## 📊 Monitoring & Logging (hooks)
- Add **kube-prometheus-stack** via Helm to your cluster (Prometheus + Grafana).
- Add **Loki + Promtail** for logs.
- The app exposes a simple `/metrics` placeholder to extend later.

---

## 🛡️ Security
- **Trivy** image scan in CI.
- Example **NetworkPolicy** lines included as comments in base if your CNI supports it.

---

## 🧪 What to Demo to Employers
- CI run (green checks & artifacts) + **badges** in README
- Container image on GHCR
- `kubectl get pods` showing rollout after CD job
- Screenshot of app working behind Ingress + `/health` ok
- (Bonus) Grafana dashboard panel screenshot

---

## ✅ Next Steps / Enhancements
- Replace `kubectl` CD with **Argo CD**
- Add **Helm chart** instead of raw manifests
- Terraform modules for **EKS**/**ECR**/**Route53**
- Blue/Green or Canary via **Argo Rollouts**
- Secrets via **External Secrets Operator**

> Tip: Commit little and often. Use issues + a project board to simulate real teamwork.
