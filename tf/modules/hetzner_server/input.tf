variable "ssh_key_id" {
  description = "hetzner ssh key id"
  type        = number
}

variable "ssh_key" {
  description = "hetzner ssh key"
  type = object({
    name       = string
    public_key = string
  })
  default = {
    name       = ""
    public_key = ""
  }
}

variable "server_image" {
  description = "server image"
  type        = string
  default     = "ubuntu-22.04"
}

variable "server_name" {
  description = "server name"
  type        = string
}

variable "environment" {
  description = "staging or production"
  type        = string
}

variable "server_power" {
  description = "hetzner server hardware size"
  type        = string
}

variable "domain" {
  description = "cloudflare domain selection"
  type        = string
}

variable "domain_records" {
  description = "cloudflare domain records"
  type = list(object({
    type    = string
    value   = string
    name    = string
    proxied = bool
  }))
}
