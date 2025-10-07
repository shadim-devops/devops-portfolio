
# Terraform Stub (AWS)

This folder is a placeholder for infrastructure-as-code:
- Backend: S3 + DynamoDB for state locking
- EKS cluster (managed)
- ECR (if not using GHCR)
- IAM OIDC for GitHub Actions

> Keep credentials safe. Prefer OIDC over static keys. Split modules for `network`, `eks`, `observability`.

Example init:
```hcl
terraform {
  required_version = ">= 1.7.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "YOUR-STATE-BUCKET"
    key    = "devops-portfolio/terraform.tfstate"
    region = "eu-central-1"
    dynamodb_table = "YOUR-LOCK-TABLE"
  }
}

provider "aws" {
  region = "eu-central-1"
}
```
