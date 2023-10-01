module "stack" {
  source       = "../modules/stack"
  environment  = local.environment
  zone         = local.zone
  server_power = "cpx21"
}

data "aws_ssm_parameter" "shapevpn_keys" {
  name = "/terraform/staging/darklab/shapevpn"
}

locals {
  environment      = "staging"
  zone             = "dd84ai.com"
  hcloud_token     = jsondecode(data.aws_ssm_parameter.shapevpn_keys.value)["hcloud_token"]
  cloudflare_token = jsondecode(data.aws_ssm_parameter.shapevpn_keys.value)["cloudflare_token"]
}

provider "hcloud" {
  token = local.hcloud_token
}

provider "cloudflare" {
  api_token = local.cloudflare_token
}





