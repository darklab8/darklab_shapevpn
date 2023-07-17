resource "helm_release" "metallbdeps" {
  name             = "metallbdeps"
  chart            = "../charts/metallbdeps"
  create_namespace = true
  namespace        = "metallbdeps"
}

data "hcloud_server" "server" {
  name = "shapevpn-cluster"
}

resource "helm_release" "metallb" {
  name             = "metallb"
  chart            = "../charts/metallb"
  create_namespace = true
  namespace        = "metallb"

  depends_on = [
    helm_release.metallbdeps
  ]

  set {
    name  = "server_ip"
    value = data.hcloud_server.server.ipv4_address
  }
}

resource "helm_release" "ingress" {
  name             = "ingress-nginx"
  chart            = "../charts/ingress-nginx"
  create_namespace = true
  namespace        = "ingress-nginx"

  depends_on = [
    helm_release.metallb
  ]
}