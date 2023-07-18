package main

import (
	"fmt"
	"shapevpn/serverInstaller/installer"
)

func main() {
	fmt.Println("launched main")
	installer := installer.Installer{
		Username: "root",
		RsaKey:   "~/.ssh/id_rsa.shapevpn.test_installer",
		Hostname: "shapevpn-test-installer.dd84ai.com",
	}
	installer.Run()
}
