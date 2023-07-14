provider "helm" {
  kubernetes {
    config_path = "~/.kube/prod_shapevpn_config"
  }
}


module "darkbot" {
  source = "../modules/darkbot"

  environment = "prod"
  environ = {
    CONSOLER_PREFIX     = "."
    SCRAPPY_PLAYER_URL  = var.SCRAPPY_PLAYER_URL
    SCRAPPY_BASE_URL    = var.SCRAPPY_BASE_URL
    DISCORDER_BOT_TOKEN = var.PRODUCTION_DISCORDER_BOT_TOKEN
    LOGGING             = true
    LOOP_DELAY          = 60
  }
  limit = {
    hard_memory = 2000
    hard_cpu    = 2000
  }
  image_version = "v0.3.9"
}
