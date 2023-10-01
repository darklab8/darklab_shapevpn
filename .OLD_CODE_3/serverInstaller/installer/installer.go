package installer

import (
	"context"
	"fmt"
	"io"

	"shapevpn/serverInstaller/vpnPlaybooks"

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

type Installer struct {
	Hostname Hostname
	Username Username
	Password Password
	RsaKey   RsaKey
}

func (i Installer) RunPlaybook(playbookName vpnPlaybooks.PlaybookName) {
	fmt.Println("executing ansible play book")
	playbookConfig := vpnPlaybooks.GetPlaybook(playbookName)

	exec := execute.NewDefaultExecute(
		execute.WithWrite(io.Writer(StdoutRedirect{})),
	)

	ansiblePlaybookConnectionOptions := &options.AnsibleConnectionOptions{
		Connection:   "ssh",
		PrivateKey:   string(i.RsaKey),
		SSHExtraArgs: "-o ForwardAgent=yes",
		User:         string(i.Username),
	}
	ansiblePlaybookOptions := &playbook.AnsiblePlaybookOptions{
		Inventory: fmt.Sprintf("%s,", i.Hostname),
		ExtraVars: playbookConfig.Extravars,
	}

	playbook := &playbook.AnsiblePlaybookCmd{
		Playbooks:         []string{playbookConfig.Playbookpath},
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

func (i Installer) Run() {
	i.RunPlaybook(vpnPlaybooks.PbInstallPython)
	i.RunPlaybook(vpnPlaybooks.PbInstallWireguard)
	i.RunPlaybook(vpnPlaybooks.PbDownloadConfigs)
}

// -e ansible_password=revealed
type Username string
type Password string
type RsaKey string
type Hostname string
