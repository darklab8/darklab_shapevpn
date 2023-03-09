# Description

Project to install self hosted VPN from web interface to your server

# How to use. Only CLI interface is ready for now.

in order to install with ssh authentification to ubuntu20.04 server at hetzner, run next command
```
docker run -v $(pwd)/configs:/app/configs darkwind8/shapevpn:installer-latest install --user="root" --ip="your_server_ip_address" --auth="ssh" --private_key="$(cat private.abc.key)"
```