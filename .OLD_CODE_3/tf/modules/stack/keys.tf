resource "hcloud_ssh_key" "darklab" {
  name       = "darklab_key"
  public_key = file("${path.module}/id_rsa.darklab.pub")
}
