package shapevpnAnsible

import (
	"path/filepath"
	"runtime"
)

func GetCurrrentFolder() string {
	_, filename, _, _ := runtime.Caller(1)
	directory := filepath.Dir(filename)
	return directory
}

type PlaybookConfig struct {
	Playbookpath string
	Extravars    map[string]interface{}
}

func newPlaybookSettings() PlaybookConfig {
	p := PlaybookConfig{
		Extravars: make(map[string]interface{}),
	}
	p.Extravars["ansible_port"] = 22
	return p
}

func GetPlaybookInstallPython() PlaybookConfig {
	config := newPlaybookSettings()
	config.Playbookpath = filepath.Join(GetCurrrentFolder(), "install_dockered_requirements.yml")
	return config
}

func GetPlaybookInstallWireguard() PlaybookConfig {
	config := newPlaybookSettings()
	config.Playbookpath = filepath.Join(GetCurrrentFolder(), "install_dockered_wireguard.yml")
	config.Extravars["ansible_python_interpreter"] = "/docker_py/venv/bin/python3"
	return config
}

func GetPlaybookDownloadConfigs() PlaybookConfig {
	config := newPlaybookSettings()
	config.Playbookpath = filepath.Join(GetCurrrentFolder(), "download_configs.yml")
	return config
}
