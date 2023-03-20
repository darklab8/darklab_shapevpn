variable "environ" {
  type = object({
    # SCRAPPY_PLAYER_URL  = string
    # LOGGING             = bool
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

variable "limit" {
  type = object({
    hard_memory = string
    hard_cpu    = string
  })
}
