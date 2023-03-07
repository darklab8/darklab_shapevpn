variable "ssh_key_id" {
  description = "hetzner ssh key id"
  type        = number
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
