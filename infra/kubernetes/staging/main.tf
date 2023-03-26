provider "helm" {
  kubernetes {
    config_path = "~/.kube/staging_shapevpn_config"
  }
  debug = true
}

terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.35.2"
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

module "shapevpn" {
  source = "../modules/shapevpn"
  environment = "staging"
  domain = "light-search.com"
  environ = {
  }
  limit = {
    hard_memory = 2000
    hard_cpu    = 2000
  }
  image_version = "latest"
}
