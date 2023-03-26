locals {
  datacenter  = "ash-dc1" # USA
  image       = var.server_image
  server_type = var.server_power
}

resource "hcloud_ssh_key" "additional_key" {
  count = var.ssh_key.public_key != "" ? 1 : 0

  name       = var.ssh_key.name
  public_key = var.ssh_key.public_key
}

resource "hcloud_server" "cluster" {
  name        = var.server_name
  image       = local.image
  datacenter  = local.datacenter
  server_type = local.server_type
  ssh_keys = concat([
    var.ssh_key_id,
  ],
  var.ssh_key.public_key != "" ? [for s in hcloud_ssh_key.additional_key : s.id] : []
  )
  public_net {
    ipv4_enabled = true
    ipv6_enabled = true
  }
  depends_on = [
    hcloud_ssh_key.additional_key
  ]
}

output "cluster_ip" {
  value = hcloud_server.cluster.ipv4_address
}

