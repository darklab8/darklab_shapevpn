locals {
  datacenter  = "ash-dc1" # USA
  image       = var.server_image
  server_type = var.server_power
}

data "hcloud_image" "image" {
  name = local.image
}

resource "hcloud_server" "cluster" {
  name        = var.server_name
  image       = data.hcloud_image.image.id
  datacenter  = local.datacenter
  server_type = local.server_type
  ssh_keys = concat([
    var.ssh_key_id,
    ],
  )
  public_net {
    ipv4_enabled = true
    ipv6_enabled = true
  }

  lifecycle {
    ignore_changes = [
      image,
    ]
  }
}

output "server_ip" {
  value = hcloud_server.cluster.ipv4_address
}

