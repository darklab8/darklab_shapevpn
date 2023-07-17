package main

import (
	"context"
	"fmt"
	"io"

	"shapevpn/serverInstaller/shapevpnAnsible"

	"github.com/apenella/go-ansible/pkg/execute"
	"github.com/apenella/go-ansible/pkg/options"
	"github.com/apenella/go-ansible/pkg/playbook"
)

type StdoutRedirect struct {
}

func (s StdoutRedirect) Write(p []byte) (n int, err error) {
	fmt.Println("stdout=", string(p))
	return len(p), nil
}

func main() {
	fmt.Println("executing ansible play book")
	config := shapevpnAnsible.GetPlaybookInstallWireguard()
	host := "shapevpn-test-installer.dd84ai.com"

	exec := execute.NewDefaultExecute(
		execute.WithWrite(io.Writer(StdoutRedirect{})),
	)

	ansiblePlaybookConnectionOptions := &options.AnsibleConnectionOptions{
		Connection:   "ssh",
		PrivateKey:   "~/.ssh/id_rsa.shapevpn.test_installer",
		SSHExtraArgs: "-o ForwardAgent=yes",
		User:         "root",
	}
	ansiblePlaybookOptions := &playbook.AnsiblePlaybookOptions{
		Inventory: fmt.Sprintf("%s,", host),
		ExtraVars: config.Extravars,
	}

	playbook := &playbook.AnsiblePlaybookCmd{
		Playbooks:         []string{config.Playbookpath},
		ConnectionOptions: ansiblePlaybookConnectionOptions,
		Options:           ansiblePlaybookOptions,
		Exec:              exec,
	}

	err := playbook.Run(context.TODO())
	if err != nil {
		panic(err)
	}
	fmt.Println("finished playbook")
}
