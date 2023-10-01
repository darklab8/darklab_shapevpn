# Description

Project that gives Web GUI for wireguard installation

# Commands

## installerpy
### Dev env

- cd installerpy/vpn_playbooks
- task init

### Running playbooks
- cd installerpy/vpn_playbooks
- ansible-playbook install_dockered_requirements.yml -i shapevpn-test-installer.dd84ai.com, --key-file ~/.ssh/id_rsa.shapevpn.server_installer -u root --ssh-extra-args '-o ForwardAgent=yes' -e "ansible_port=22"
- ansible-playbook install_dockered_wireguard.yml -i shapevpn-test-installer.dd84ai.com, --key-file ~/.ssh/id_rsa.shapevpn.server_installer -u root --ssh-extra-args '-o ForwardAgent=yes' -e "ansible_port=22"
- ansible-playbook download_configs.yml -i shapevpn-test-installer.dd84ai.com, --key-file ~/.ssh/id_rsa.shapevpn.server_installer -u root --ssh-extra-args '-o ForwardAgent=yes' -e "ansible_port=22"
