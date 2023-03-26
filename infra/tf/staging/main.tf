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
  server_power = "cpx21"
  domain       = local.domain
  ssh_key_id   = module.ssh_key.darklab_id
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
    {
      type    = "A"
      value   = "cluster_ip"
      name    = "api.${local.domain}"
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
  ssh_key_id   = module.ssh_key.installer_id
  ssh_key = {
    name = "extra_installer_key"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkYPmxS9PpssQ+dmsC21pPgpZEWhYGf8aj9gYOd+JwPeF+PH3nlcvht6n0JMCVQLI7U0HoGqkgE0JAO4HhtpN2PfGk8Rjo/lw7fQgXBkKB9pZN4Vpe+pD1Av90O08Ot5cS7IhjHc+g2ixIRugZJOdAqFrgRqXm/xoj33qmhntE03gfOtDENQF6zY1eLe4c6H3MFiFJdzb5r4RR7vyUBksPRqKVVYv0p3d/m6Gld0JVhp2skZ/Zn7qAn4gvccdlI0cEo3S3uVmZ/lB0kCJ7P/NQjLQXzlqbvSKmi/pkHs8t2M2cr5dSYyW++w1xFXf2j6x/wap2jhMfEQ1H2sim6PQd"
  }
  server_image = "ubuntu-20.04"
  domain_records = [
    {
      type    = "A"
      value   = "cluster_ip"
      name    = "shapevpn-installer-test-subject.${local.domain}"
      proxied = false
    },
  ]
}


