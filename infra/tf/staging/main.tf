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

locals {
  domain      = "light-search.com"
  environment = "staging"
}

module "ssh_key" {
  source = "../modules/ssh_key"
}

module "cluster" {
  server_name  = "shapevpn-cluster"
  source       = "../modules/server"
  environment  = local.environment
  server_power = "cpx11"
  domain       = local.domain
  ssh_key_id   = module.ssh_key.id
  domain_records = [
    {
      type    = "A"
      value   = "cluster_ip"
      name    = local.domain
      proxied = false
    },
    {
      type    = "CNAME"
      value   = local.domain # "@"
      name    = "www"
      proxied = false
    },
    {
      type    = "A"
      value   = "cluster_ip"
      name    = "shapevpn-cluster.${local.domain}"
      proxied = false
    },
  ]
}

module "installer_test_subject" {
  server_name  = "shapevpn-installer-test-subject"
  source       = "../modules/server"
  environment  = local.environment
  server_power = "cpx11"
  domain       = local.domain
  ssh_key_id   = module.ssh_key.id
  domain_records = [
    {
      type    = "A"
      value   = "cluster_ip"
      name    = "shapevpn-installer-test-subject.${local.domain}"
      proxied = false
    },
  ]
}


