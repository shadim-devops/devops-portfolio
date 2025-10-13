Cloud-Native DevOps Starter (Portfolio Project)

This is a small educational DevOps portfolio project that demonstrates basic principles of containerization, CI/CD, Kubernetes, infrastructure as code, and monitoring. The project includes a simple Python Flask app with Docker multi-stage builds, unit tests using Pytest, and automated CI/CD pipelines via GitHub Actions. It uses Kubernetes with Kustomize for separate development and production environments, Nginx Ingress configuration, and Makefile helpers. Terraform stubs are prepared for AWS (EKS and ECR), and Trivy is used for container security scanning. You can practice locally for free using kind or minikube and push images to GitHub Container Registry.

The workflow is simple: a developer pushes changes to GitHub, which triggers GitHub Actions for CI (linting, testing, building, and scanning) and pushes the image to GHCR. Deployment to a Kubernetes cluster can be done manually or automated via Argo CD. The cluster runs the app as a Deployment with a Service and Ingress.

Repository structure includes:

* app/ for the main application code (app.py, requirements, Dockerfile)
* tests/ for unit tests
* k8s/ for Kubernetes manifests (base and overlays for dev/prod)
* .github/workflows/ for CI/CD pipelines
* infra/terraform/ for infrastructure templates
* docker-compose.yaml for local setup
* Makefile for helper commands

Quick start locally: install Docker and Python 3.11+, run tests with `pytest`, then build and run the container using `docker build` and `docker run`. You can also start the app with `docker compose up --build` and check it at [http://localhost:8000/health].

For Kubernetes, base manifests are in k8s/base, and overlays for environments are in k8s/overlays/dev and k8s/overlays/prod. Deploy using `kubectl apply -k k8s/overlays/dev` or `kubectl apply -k k8s/overlays/prod`. An Ingress controller (like ingress-nginx) is required.

CI/CD details:
The CI workflow (ci.yml) runs linting with flake8, testing with pytest, builds and scans the Docker image with Trivy, and pushes it to GHCR. The CD workflow (cd.yml) is triggered manually with environment protection and applies manifests using kubectl and a kubeconfig provided via GitHub Secrets. It can be replaced with Argo CD for a GitOps setup. Required secrets: GHCR_USERNAME, GHCR_TOKEN, KUBE_CONFIG, and optionally TRIVY_DB_REPOSITORY.

Monitoring and logging are handled through kube-prometheus-stack (Prometheus and Grafana) and Loki + Promtail. The app includes a simple /metrics endpoint for future monitoring extensions. Security checks include Trivy scans in CI and example NetworkPolicy lines in the base manifests.

When presenting the project to employers, you can show a successful CI run with green checks, the image published to GHCR, Kubernetes rollout output (`kubectl get pods`), a screenshot of the app running behind Ingress, and optionally a Grafana dashboard panel. Possible future improvements include replacing kubectl CD with Argo CD, using Helm charts, adding Terraform modules for AWS resources, implementing Canary or Blue/Green deployments, and managing secrets with the External Secrets Operator. Commit often, use GitHub issues and a small project board to simulate real teamwork.

