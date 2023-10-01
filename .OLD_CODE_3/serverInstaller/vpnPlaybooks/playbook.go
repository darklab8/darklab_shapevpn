package vpnPlaybooks

import (
	"path/filepath"
	"runtime"
)

func GetCurrrentFolder() string {
	_, filename, _, _ := runtime.Caller(1)
	directory := filepath.Dir(filename)
	return directory
}

type playbookConfig struct {
	Playbookpath string
	Extravars    map[string]interface{}
}

func newPlaybookSettings() playbookConfig {
	p := playbookConfig{
		Extravars: make(map[string]interface{}),
	}
	p.Extravars["ansible_port"] = 22
	return p
}

type PlaybookName int64

const (
	PbInstallPython PlaybookName = iota
	PbInstallWireguard
	PbDownloadConfigs
)

func GetPlaybook(playbook PlaybookName) playbookConfig {
	config := newPlaybookSettings()

	switch playbook {
	case PbInstallPython:
		config.Playbookpath = filepath.Join(GetCurrrentFolder(), "install_dockered_requirements.yml")
	case PbInstallWireguard:
		config.Playbookpath = filepath.Join(GetCurrrentFolder(), "install_dockered_wireguard.yml")
		config.Extravars["ansible_python_interpreter"] = "/docker_py/venv/bin/python3"
	case PbDownloadConfigs:
		config.Playbookpath = filepath.Join(GetCurrrentFolder(), "download_configs.yml")
	}
	return config
}
