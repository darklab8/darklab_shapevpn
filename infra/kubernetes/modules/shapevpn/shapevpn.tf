
locals {
  chart_path = "${path.module}/../../charts/shapevpn"
  # This hash forces Terraform to redeploy if a new template file is added or changed, or values are updated
  chart_hash  = sha1(join("", [for f in fileset(local.chart_path, "**/*ml") : filesha1("${local.chart_path}/${f}")]))
  environment = var.environment
}

resource "helm_release" "experiment" {
  name             = "shapevpn"
  chart            = "../charts/shapevpn"
  create_namespace = true
  namespace        = "shapevpn"
  force_update     = false
  reset_values     = true
  recreate_pods    = true

  values = [
    <<-EOT
    soft_memory_limit: "250Mi"
    soft_cpu_limit: "500m"
    hard_memory_limit: "${var.limit.hard_memory}Mi"
    hard_cpu_limit: "${var.limit.hard_cpu}m"

    image_version: "${var.image_version}"
    domain_main: "${var.domain}"

    ENVIRONMENT: "${var.environment}"
    EOT
  ]
  set {
    name  = "chartHash"
    value = local.chart_hash
  }

}
