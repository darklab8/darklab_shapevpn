locals {
  domain = var.domain
}

data "cloudflare_zone" "domain_main" {
  name = local.domain
}

resource "cloudflare_record" "record_front" {
  ttl     = 60
  type    = "A"
  value   = hcloud_server.cluster.ipv4_address
  name    = local.domain
  zone_id = data.cloudflare_zone.domain_main.id
  proxied = false
}

resource "cloudflare_record" "record_www_redirecter" {
  ttl     = 60
  type    = "CNAME"
  value   = "@"
  name    = "www"
  zone_id = data.cloudflare_zone.domain_main.id
  proxied = false
}

resource "cloudflare_record" "record_cluster" {
  ttl     = 60
  type    = "A"
  value   = hcloud_server.cluster.ipv4_address
  name    = "shapevpn-cluster.${local.domain}"
  zone_id = data.cloudflare_zone.domain_main.id
  proxied = false
}
