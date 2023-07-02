module "cluster" {
  server_name  = "shapevpn-cluster"
  source       = "../server"
  environment  = var.environment
  server_power = var.server_power
  domain       = var.zone
  ssh_key_id   = hcloud_ssh_key.darklab.id
  domain_records = [
    {
      type    = "A"
      value   = "server_ip"
      name    = var.zone
      proxied = false
    },
    {
      type    = "CNAME"
      value   = var.zone # "@"
      name    = "www"
      proxied = false
    },
    {
      type    = "A"
      value   = "server_ip"
      name    = "shapevpn-cluster.${var.zone}"
      proxied = false
    },
    {
      type    = "A"
      value   = "server_ip"
      name    = "api.${var.zone}"
      proxied = false
    },
  ]
}