variable "environ" {
  type = object({
  })
}

variable "environment" {
  type = string
}

variable "image_version" {
  type        = string
  description = "shapevpn image version"
  default     = "latest"
}

variable "domain" {
  type        = string
}

variable "limit" {
  type = object({
    hard_memory = string
    hard_cpu    = string
  })
}
