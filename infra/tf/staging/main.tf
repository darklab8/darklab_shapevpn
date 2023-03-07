terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.35.2"
    }
    aws = {
      source  = "hashicorp/aws"
      version = ">= 2.7.0"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = ">=3.7.0"
    }
  }
}

variable "staging_hcloud_token" {
  type      = string
  sensitive = true
}

provider "hcloud" {
  token = var.staging_hcloud_token
}

variable "staging_cloudflare_token" {
  type      = string
  sensitive = true
}

provider "cloudflare" {
  api_token = var.staging_cloudflare_token
}
module "cluster" {
  source       = "../modules/shapevpn"
  environment  = "staging"
  server_power = "cpx11"
  domain       = "light-search.com"
}

output "cluster_ip" {
  value = module.cluster.cluster_ip
}
