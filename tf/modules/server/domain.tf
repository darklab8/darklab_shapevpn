locals {
  domain = var.domain
}

data "cloudflare_zone" "domain_main" {
  name = local.domain
}

resource "cloudflare_record" "record" {
  for_each = {
    for index, record in var.domain_records : record.name => record
  }

  ttl     = 60
  type    = each.value.type
  value   = each.value.value == "server_ip" ? hcloud_server.cluster.ipv4_address : each.value.value
  name    = each.value.name
  zone_id = data.cloudflare_zone.domain_main.id
  proxied = each.value.proxied
}
