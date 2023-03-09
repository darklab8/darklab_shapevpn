resource "hcloud_ssh_key" "darklab" {
  name       = "darklab_key"
  public_key = file("${path.module}/id_rsa.darklab.pub")
}

resource "hcloud_ssh_key" "installer" {
  name       = "installer_key"
  public_key = file("${path.module}/private.key.pub")
}

output "darklab_id" {
  value = hcloud_ssh_key.darklab.id
}

output "installer_id" {
  value = hcloud_ssh_key.installer.id
}
