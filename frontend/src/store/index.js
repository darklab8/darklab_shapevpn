import { createStore } from 'vuex'
import * as Utils from '@/util.js';
import * as Settings from '@/settings.js';

export default createStore({
  state: {
    brand: "ShapeVPN",
    language: Settings.LOCALE,
    opened_FAQ_question: null,
    is_we_having_server: false,
    download_configs_selector: {
      selected: 1,
    },
    server_installation: {
      installed: false,
      installing: false,
      task_id: null,
      configs: null,
      status: "NOT_STARTED",
      status_meta: null,
      error_message: "",
      stdout: "",
      visible_log: false,
    },
    console: {
      minimized: false,
      height: 300
    },
    client_download_state: "windows",
    selected_provider: 'vultr',
    referral_link: {
      vultr: 'https://www.vultr.com/?ref=9014347',
      linode: 'https://www.linode.com/'
    },
    client_download_urls: {
      windows: "https://download.wireguard.com/windows-client/wireguard-installer.exe",
      ios: "https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8",
      macos: "https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12",
      android: "https://play.google.com/store/apps/details?id=com.wireguard.android",
      linux: "#linux_instruction"
    },
    scrolling_states: {

      server_buy_choice: false,
      server_buy_instruction: false,
      server_install: false,
      download_configs: false,
      download_client: false,
      clicked_i_have_no_server: false,
    },
    keys: {
      private: "generating",
      public: "generating",
      data_key: "generating"
    }
  },
  getters: {
    is_console_visible: state => {
      return state.server_installation.visible_log
    }
  },
  mutations: {
    set_keys(state, input_keys) {
      state.keys.private = input_keys.private
      state.keys.public = input_keys.public
      state.keys.data_key = input_keys.data_key
    },
    set_console_minimized(state, new_state) {
      state.console.minimized = new_state
      sessionStorage.setItem('console_minimized', new_state)

      if (new_state) state.console.height = 33;
      else state.console.height = 300;
    },
    set_console_height(state, new_state) {
      state.console.height = new_state;
    },
    move_to_anchor(state, anchor) {

      if (anchor == 'server_buy') this.commit('set_is_we_having_server', false)
      if (anchor == 'server_install') this.commit('set_is_we_having_server', true)

      setTimeout(() => {
        var element = document.getElementById(anchor);
        element.scrollIntoView();
      }
      )
    },
    set_opened_FAQ_question(state, new_state) {
      state.opened_FAQ_question = new_state
    },
    set_download_configs_selector(state, new_state) {
      state.download_configs_selector.selected = new_state
    },
    set_log_visible(state, new_state) {
      state.server_installation.visible_log = new_state
    },
    set_error_message(state, new_msg) {
      state.server_installation.error_message = new_msg
    },
    set_stdout(state, new_stdout) {
      state.server_installation.stdout = new_stdout
      sessionStorage.setItem('stdout', new_stdout);
    },
    set_is_we_having_server(state, new_state) {
      state.is_we_having_server = new_state

      state.scrolling_states.server_buy_choice = false;
      state.scrolling_states.server_buy_instruction = false;
      state.scrolling_states.server_install = false;
      state.scrolling_states.download_configs = false;
      state.scrolling_states.download_client = false;

      if (new_state === false) state.scrolling_states.clicked_i_have_no_server = true;

      sessionStorage.setItem('is_we_having_server', Utils.json_dumps({ "state": new_state }));
    },
    set_server_installation(state, server_installation_) {
      state.server_installation = Utils.json_loads(server_installation_)
    },
    set_is_server_installing(state, new_state) {
      state.server_installation.installing = new_state
    },
    set_status(state, new_data) {
      state.server_installation.status = new_data.status
      state.server_installation.status_meta = new_data.meta

      if (new_data.status === "NOT_STARTED") {
        state.server_installation.installing = false
        state.server_installation.installed = false
      }
      else if (new_data.status === "SUCCESS") {
        state.server_installation.installing = false
        state.server_installation.installed = true
      }
      else if (new_data.status === "FAILURE") {
        state.server_installation.installing = false
        state.server_installation.installed = false
      }
      else {
        state.server_installation.installing = true
        state.server_installation.installed = false
      }

      sessionStorage.setItem('status', new_data.status);
    },
    set_configs(state, new_configs) {
      state.server_installation.configs = Utils.json_loads(new_configs)

      sessionStorage.setItem('configs', new_configs)
    },

    set_task_id(state, task_id_and_status) {
      let task_id = task_id_and_status.task_id;
      let status = "status" in task_id_and_status ? task_id_and_status.status : "NOT STARTING";

      state.server_installation.task_id = task_id

      if ("DontSetStatusForOnMount" in task_id_and_status) return
      
      this.commit("set_status", {status: status, meta: null})

      sessionStorage.setItem('task_id', task_id);
    },
    check_scrollings(state) {
      var store = this;
      function GetScrollPosition() {
        return window.scrollY
      }

      function GetElementScrollTop(elementID) {
        return document.getElementById(elementID).offsetTop
      }
      function GetElementScrollBottom(elementID) {
        return GetElementScrollTop(elementID) + document.getElementById(elementID).scrollHeight
      }
      function ChangeStateIfChanged(elementID, new_state) {

        if (state.scrolling_states[elementID] != new_state) {
          store.commit("set_scrolling_states", { name: elementID, status: new_state })
        }
      }

      function PercentageOfScreenHeight(percentage) {
        return screen.height / 100 * percentage
      }

      if (state.is_we_having_server) {
        if (GetScrollPosition() > GetElementScrollTop("download_configs") - PercentageOfScreenHeight(50)) {
          ChangeStateIfChanged("download_configs", true)
        }
        else {
          ChangeStateIfChanged("download_configs", false)
        }

        if (GetScrollPosition() > GetElementScrollTop("download_client")  - PercentageOfScreenHeight(20)) {
          ChangeStateIfChanged("download_client", true)
        }
        else {
          ChangeStateIfChanged("download_client", false)
        }
      }

      if (state.is_we_having_server) {
        if (GetScrollPosition() > GetElementScrollTop("server_install") ) {
          ChangeStateIfChanged("server_install", true)
        } else {
          ChangeStateIfChanged("server_install", false)
        }
      }

      if (!state.is_we_having_server) {
        if (GetScrollPosition() > (GetElementScrollTop("server_buy_choice") - 300)) {
          ChangeStateIfChanged("server_buy_choice", true)
        } else {
          ChangeStateIfChanged("server_buy_choice", false)
        }


        if (GetScrollPosition() > (GetElementScrollBottom("server_buy_instruction") - PercentageOfScreenHeight(50))) {
          ChangeStateIfChanged("server_buy_instruction", true)
        } else {
          ChangeStateIfChanged("server_buy_instruction", false)
        }
      }

    },
    changeOSPlatform(state, new_platform) {
      state.client_download_state = new_platform
    },
    set_selected_provider(state, new_provider) {
      state.selected_provider = new_provider
    },

    is_vpn_server_installed(state, new_status) {
      state.is_vpn_server_installed = new_status
    },
    set_scrolling_states(state, state_object) {
      state.scrolling_states[state_object.name] = state_object.status
    },
    set_language(state, new_language) {
      state.language = new_language
    },
  },
  actions: {
  },
  modules: {
  }
})
