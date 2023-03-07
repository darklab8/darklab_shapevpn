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
  }
}

variable "staging_hcloud_token" {
  type      = string
  sensitive = true
}

provider "hcloud" {
  token = var.staging_hcloud_token
}

module "stack" {
  source       = "../modules/shapevpn"
  environment  = "staging"
  server_power = "cpx11"
}

output "cluster_ip" {
  value = module.stack.cluster_ip
}
