locals {
  datacenter  = "ash-dc1" # USA
  image       = "ubuntu-22.04"
  server_type = var.server_power
}

resource "hcloud_server" "cluster" {
  name        = var.server_name
  image       = local.image
  datacenter  = local.datacenter
  server_type = local.server_type
  ssh_keys = [
    var.ssh_key_id,
  ]
  public_net {
    ipv4_enabled = true
    ipv6_enabled = true
  }
}

output "cluster_ip" {
  value = hcloud_server.cluster.ipv4_address
}

