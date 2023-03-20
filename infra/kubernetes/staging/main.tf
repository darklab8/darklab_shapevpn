provider "helm" {
  kubernetes {
    config_path = "~/.kube/staging_shapevpn_config"
  }
  debug = true
}

module "shapevpn" {
  source = "../modules/shapevpn"

  environment = "staging"
  environ = {
  }
  limit = {
    hard_memory = 2000
    hard_cpu    = 2000
  }
  image_version = "latest"
}
