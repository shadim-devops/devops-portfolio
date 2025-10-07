
.PHONY: help test build run kind-up kind-load k8s-dev

IMAGE ?= ghcr.io/shadim-devops/devops-portfolio
TAG ?= local

help:
	@echo "make test | build | run | kind-up | kind-load | k8s-dev"

test:
	pip install -r app/requirements.txt
	pip install -r tests/requirements.txt
	pytest -q

build:
	docker build -t $(IMAGE):$(TAG) ./app

run:
	docker run --rm -p 8000:8000 $(IMAGE):$(TAG)

kind-up:
	kind create cluster --name devops-portfolio || true
	kubectl cluster-info --context kind-devops-portfolio

kind-load: build
	kind load docker-image $(IMAGE):$(TAG) --name devops-portfolio

k8s-dev:
	kubectl apply -k k8s/overlays/dev
