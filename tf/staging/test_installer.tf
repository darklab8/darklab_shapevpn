resource "hcloud_ssh_key" "installer" {
  name       = "test_installer_key"
  public_key = tls_private_key.test_server.public_key_openssh
}

resource "tls_private_key" "test_server" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

output test_server_private_key {
  value = tls_private_key.test_server.private_key_openssh
  sensitive = true
}

module "installer_test_subject" {
  server_name  = "shapevpn-test-installer"
  source       = "../modules/hetzner_server"
  environment  = local.environment
  server_power = "cpx11"
  domain       = local.zone
  ssh_key_id   = hcloud_ssh_key.installer.id
  server_image = "ubuntu-20.04"
  domain_records = [
    {
      type    = "A"
      value   = "server_ip"
      name    = "shapevpn-test-installer.${local.zone}"
      proxied = false
    },
  ]
}