resource "hcloud_ssh_key" "installer" {
  name       = "test_installer_key"
  public_key = file("${path.module}/id_rsa.shapevpn.test_installer.pub")
}

module "installer_test_subject" {
  server_name  = "shapevpn-test-installer"
  source       = "../modules/server"
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