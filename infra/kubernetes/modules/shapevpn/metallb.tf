resource "helm_release" "metallb" {
  name             = "metallb"
  chart            = "../charts/metallb"
  create_namespace = true
  namespace        = "metallb"

  values = [
    "${file("${path.module}/../../charts/metallb/values.yaml")}"
  ]
}
