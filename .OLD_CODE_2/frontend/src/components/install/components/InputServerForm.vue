<template>
    <div class="sub_header_and_settings">
    <div
        class="sub_header"
    >{{ $i18n.t(`install.InputServerForm.insert_details_about_your_server`) }}</div>
    <figure @click="are_advanced_settings_shown = !are_advanced_settings_shown">
        <div class="label_to_button_advanced_features">
        {{ $i18n.t(`install.InputServerForm.advanced_features`) }}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M24 13.8725V9.90895L21.6 9.11623C21.4 8.52169 21.2 7.72898 20.8 7.13444L22 4.75629L19 2.17997L16.8 3.17086C16.2 2.7745 15.6 2.57633 14.8 2.37815L14 0H10L9.2 2.37815C8.6 2.57633 7.8 2.7745 7.2 3.17086L5 2.17997L2.2 4.95447L3.4 7.33262C3 7.92716 2.8 8.52169 2.6 9.31441L0 9.90895V13.8725L2.4 14.6652C2.6 15.2598 2.8 16.0525 3.2 16.647L2.2 18.827L5 21.6015L7.4 20.4124C8 20.8088 8.6 21.007 9.4 21.2051L10 23.7815H14L14.8 21.4033C15.4 21.2051 16.2 21.007 16.8 20.6106L19.2 21.7997L22 19.0252L20.8 16.647C21.2 16.0525 21.4 15.458 21.6 14.6652L24 13.8725ZM7.33333 11.8907C7.33333 9.24835 9.33333 7.26656 12 7.26656C14.6667 7.26656 16.6667 9.24835 16.6667 11.8907C16.6667 14.5331 14.6 16.5149 12 16.5149C9.4 16.5149 7.33333 14.5331 7.33333 11.8907Z" fill="#B0B0B0"/>
        </svg>
    </figure>
    </div>
    <div class="input_form" id="server_install">
        <div class="flexed-buttons">
            <div
                :class="[input_form.install_type == 'ssh' ? 'pressed' : 'not_pressed', 'button']"
                @click="set_install_type_ssh"
            >{{ $i18n.t(`install.InputServerForm.SSS_key_of_the_server`) }}</div>
            <div
                :class="[input_form.install_type == 'pass' ? 'pressed' : 'not_pressed', 'button']"
                @click="set_install_type_password"
            >{{ $i18n.t(`install.InputServerForm.server_password`) }}</div>
        </div>
        <div class="horizontal_line"></div>

        <div class="centralize_form">
            <div class="centralize_form_inside">
                <form>
                    <div class="flex-element operational_system">
                        <label
                            for="operational_system"
                        >{{ $i18n.t(`install.InputServerForm.operational_system`) }}</label>
                        <div
                            class="select"
                            id="operational_system"
                            name="operational_system"
                        >Ubuntu 20.04 LTS</div>
                    </div>

                    <div class="flex-element ip_address">
                        <label for="ipaddress">{{ $i18n.t(`install.InputServerForm.ip_address`) }}</label>
                        <input
                            required
                            type="text"
                            id="ipaddress"
                            name="ipaddress"
                            placeholder="Your IP address."
                            v-model="input_form.ip_address"
                        />
                        <div
                            v-if="validate_ip_address !== ''"
                            class="validator-error"
                        >{{ validate_ip_address }}</div>
                    </div>

                    <div class="flex-element login">
                        <label for="login">{{ $i18n.t(`install.InputServerForm.login`) }}</label>
                        <input
                            required
                            type="text"
                            id="login"
                            name="login"
                            placeholder="root"
                            v-model="input_form.login"
                        />
                        <div
                            v-if="validate_login !== ''"
                            class="validator-error"
                        >{{ validate_login }}</div>
                    </div>

                    <div class="flex-element ssh_key" >
                        <template v-if="input_form.install_type == 'ssh'">
                            <label
                                class="button-copy-anchor"
                                for="ssh_key"
                            >{{ $i18n.t(`install.InputServerForm.SSH_public_key`) }}
                                <figure class="button-copy-figure"
                                    @click="copy_ssh_to_clipboard">
                                    <svg width="13" height="15" viewBox="0 0 13 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="2.5" y="0.5" width="10" height="12" rx="0.5" stroke="#787878"/>
                                    <path d="M0 3C0 2.44772 0.447715 2 1 2V13C1 13.5523 1.44772 14 2 14H11C11 14.5523 10.5523 15 10 15H1C0.447715 15 0 14.5523 0 14V3Z" fill="#787878"/>
                                    </svg>
                                </figure>
                                <transition name="fade">
                                    <div v-if="toast_copied_shown" class="button-copy-message-copied">
                                    {{this.$i18n.t(`install.InputServerForm.copied`)}}
                                </div>
                                </transition>
                                
                            </label>
                            <input
                                required
                                disabled
                                readonly
                                type="text"
                                id="ssh_key"
                                name="ssh_key"
                                placeholder="SSH key"
                                v-model="keys.public"
                                
                            />
                            

                        </template>
                        <template v-else-if="input_form.install_type == 'pass'">
                            <label for="password">{{ $i18n.t(`install.InputServerForm.password`) }}</label>
                            <input
                                required
                                type="password"
                                id="password"
                                name="password"
                                placeholder="*******"
                                v-model="input_form.password"
                            />
                            <div
                                v-if="validate_password !== ''"
                                class="validator-error"
                            >{{ validate_password }}</div>
                        </template>
                    </div>

                    <div class="flex-element server_ssh_port" v-if="are_advanced_settings_shown">
                        <label for="server_ssh_port">{{ $i18n.t(`install.InputServerForm.server_ssh_port`) }}</label>
                        <input
                            required
                            type="text"
                            id="server_ssh_port"
                            name="server_ssh_port"
                            placeholder="22"
                            v-model="input_form.server_ssh_port"
                        />
                        <div
                            v-if="validate_number(input_form.server_ssh_port) !== ''"
                            class="validator-error"
                        >{{ validate_number(input_form.server_ssh_port) }}</div>
                    </div>

                    <div class="flex-element server_vpn_port" v-if="are_advanced_settings_shown">
                        <label for="server_vpn_port">{{ $i18n.t(`install.InputServerForm.server_vpn_port`) }}</label>
                        <input
                            required
                            type="text"
                            id="server_vpn_port"
                            name="server_vpn_port"
                            placeholder="31280"
                            v-model="input_form.server_vpn_port"
                        />
                        <div
                            v-if="validate_number(input_form.server_vpn_port) !== ''"
                            class="validator-error"
                        >{{  validate_number(input_form.server_vpn_port)  }}</div>
                    </div>

                    <div class="flex-element flex-element-button">
                        <template v-if="is_server_installing">
                            <div class="progress-bar">
                                <div class="progress-bar-words">
                                    <p>{{ status }} - {{ percentage_is_done }}%</p>
                                </div>

                                <div
                                    class="progress-bar-filling"
                                    :style="{ width: percentage_is_done + '%' }"
                                ></div>
                            </div>

                             <div v-if="status_meta !== null" class="status_meta">
                                {{status_meta.current_name}}
                             </div>
                             <div v-else class="status_meta">
                                 Awaiting for the installation to get started
                             </div>

                            <div class="flex-element-button_abort" @click="abort">Abort</div>
                        </template>
                        <template v-else>
                            <div class="submit" @click="action_install_vpn_server">
                                <p>{{ $i18n.t(`install.InputServerForm.install_vpn_to_server`) }}</p>
                            </div>
                            <div class="message">
                                <template v-if="error_message !== ''">
                                    <div class="error">
                                        <div>{{ $i18n.t(`install.InputServerForm.` + error_message) }}</div>
                                    </div>
                                </template>
                                <div v-if="configs !== null" class="phrase-success">
                                    {{ $i18n.t(`install.InputServerForm.installation_has_been_completed`) }}
                                    <span
                                        @click="click_ref('download_configs')"
                                    >{{ $i18n.t(`install.InputServerForm.go_to_config_downloading`) }}</span>
                                </div>
                                <div
                                    class="phrase-failure"
                                    v-if="is_console_visible"
                                    @click="turn_console_visilibity_on"
                                    v-html="$i18n.t(`install.InputServerForm.something_went_wrong`)"
                                ></div>
                            </div>
                        </template>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import * as Requests from '@/api.js';
import * as Utils from '@/util.js';
export default {
    data() {
        return {
            input_form: {
                install_type: "ssh",
                operational_system: "ubuntu_2004",
                ip_address: "",
                login: "root",
                password: "",
                server_ssh_port: "22",
                server_vpn_port: "31280",
                private: "generating",
                public: "generating",
                data_key: "generating",
            },
            polling: null,
            toast_copied_shown: false,
            are_advanced_settings_shown: false
        };
    },
    beforeUnmount() {
        clearInterval(this.polling)
    },
    async mounted() {

        // restoring previous session
        let task_id = sessionStorage.getItem('task_id');
        if (task_id !== null && task_id !== undefined) {
            this.$store.commit('set_task_id', { task_id: task_id, DontSetStatusForOnMount: true })
        }

        let saving_configs = sessionStorage.getItem('configs');

        if (saving_configs !== null && saving_configs !== undefined && saving_configs !== "undefined") {

            this.$store.commit('set_configs', saving_configs)

        }

        let saving_status = sessionStorage.getItem('status');
        if (saving_status !== null && saving_status !== undefined) {
            this.$store.commit('set_status', {status: saving_status, meta: null})
        }

        let saved_stdout = sessionStorage.getItem('stdout');
        if (saved_stdout !== null && saved_stdout !== undefined) {
            this.$store.commit('set_stdout', saved_stdout)
        }

        //mounting looper
        this.pollData();

        
        
    },
    methods: {
        isNumber(str) {
            var n = Math.floor(Number(str));
            return n !== Infinity && String(n) === str && n >= 0;
        },
        validate_number(str) {
            
            if (!(this.isNumber(str))){
                return this.$i18n.t(`install.InputServerForm.validators.invalid_number`)
            }

            return ""
        },
        copy_ssh_to_clipboard(){
            navigator.clipboard.writeText(this.keys.public);
            this.toast_copied_shown=true;

            let thiis = this;
            setTimeout(
                () => {
                    thiis.toast_copied_shown=false;
                },
                1000
            );
        },
        abort() {
            this.$store.commit('set_is_server_installing', false)
            this.$store.commit('set_task_id', { task_id: null, status: "NOT_STARTED" })
            this.$store.commit('set_log_visible', false);
            this.$store.commit('set_status', {status: "NOT_STARTED", meta: null})
            this.$store.state.server_installation.configs=null;

            sessionStorage.removeItem("status")
            sessionStorage.removeItem("task_id")
            sessionStorage.removeItem("stdout")
            sessionStorage.removeItem("configs")
        },
        turn_console_visilibity_on() {
            this.$store.commit(`set_console_minimized`, !this.console_minimized)
        },
        click_ref(refName) {
            var element_to_scroll_to = document.getElementById(refName);
            element_to_scroll_to.scrollIntoView();
        },
        set_install_type_ssh() {
            this.input_form.install_type = "ssh";
        },
        set_install_type_password() {
            this.input_form.install_type = "pass";
        },
        pollData() {
            this.polling = setInterval(async () => {
                if (this.task_id === null) {
                    return
                }

                if (this.status === "SUCCESS" || this.status === "FAILURE") {
                    return
                }

                let status_response = await Requests.Status(this.task_id)
                let status = status_response.data.task_id

                
                if (status === "SUCCESS") {
                    let configs = (await Requests.Configs(this.task_id, this.keys.data_key
                    )).data.configs
                    let stdout = (await Requests.Stdout(this.task_id)).data.stdout


                    this.$store.commit('set_configs', configs)
                    this.$store.commit('set_stdout', stdout)
                }

                if (status === "FAILURE") {
                    let stdout = (await Requests.Stdout(this.task_id)).data.stdout
                    this.$store.commit('set_stdout', stdout)
                }

                if (status === "FAILURE") {
                    this.$store.commit('set_log_visible', true);
                }

                this.$store.commit('set_status', {status: status, meta: status_response.data})


            }, 3000)
        },
        async action_install_vpn_server() {

            this.$store.commit('set_error_message', "")

            if (this.validate_ip_address !== "") return
            else if (this.input_form.ip_address === "") { this.$store.commit('set_error_message', "empty_field"); return; }

            if (this.validate_login !== "") return
            else if (this.input_form.login === "") { this.$store.commit('set_error_message', "empty_field"); return; }

            if (this.input_form.install_type == "pass") {
                if (this.validate_password !== "") return
                else if (this.input_form.password === "") { this.$store.commit('set_error_message', "empty_field"); return; }
            }


            let store = this.$store;

            this.$store.commit('set_is_server_installing', true)
            let data_for_sending = {
                auth: this.input_form.install_type,
                user: this.input_form.login,
                ip_address: this.input_form.ip_address,
                password: this.input_form.password,
                server_ssh_port: this.input_form.server_ssh_port,
                server_vpn_port: this.input_form.server_vpn_port,
                ssh_key: this.keys.private,
                data_key: this.keys.data_key,
            }
            await Requests.Install(data_for_sending).catch(function (error) {
                store.commit('set_is_server_installing', false)

                let msg = ""
                if (error.response) {
                    // Request made and server responded
                    msg += error.response.data + "\n";
                    msg += error.response.status + "\n";
                    msg += error.response.headers + "\n";
                } else if (error.request) {
                    // The request was made but no response was received
                    msg += error.request + "\n";
                } else {
                    // Something happened in setting up the request that triggered an Error
                    msg += error.message + "\n";
                }

                store.commit('set_stdout', "Failure to perform request for installation to API Service.\n" + msg)
                store.commit('set_log_visible', true);

            }).then(function (response) {
                if (response === undefined) return
                store.commit('set_task_id', { task_id: response.data.task_id, status: "STARTING" })
                store.commit('set_log_visible', false);
            });



        }
    },
    computed: {
        keys() {
            return this.$store.state.keys
        },
        validate_password() {
            return ""
        },
        validate_ip_address() {
            if (this.input_form.ip_address === "") return ""

            if (!Utils.is_ip_address(this.input_form.ip_address))
                return this.$i18n.t(`install.InputServerForm.validators.invalid_ip`)

            return ""
        },
        validate_login() {
            if (!Utils.is_correct_linux_login(this.input_form.login))
                return this.$i18n.t(`install.InputServerForm.validators.invalid_login`)

            return ""
        },
        is_console_visible() {
            return this.$store.getters.is_console_visible
        },
        selected_provider() {
            return this.$store.state.selected_provider
        },
        ssh_key_pub() {
            return this.input_form.public
        },
        task_id() {
            return this.$store.state.server_installation.task_id
        },
        is_server_installed() {
            return this.$store.state.server_installation.installed
        },
        is_server_installing() {
            return this.$store.state.server_installation.installing
        },
        configs() {
            return this.$store.state.server_installation.configs
        },
        status() {
            return this.$store.state.server_installation.status
        },
        status_meta() {
            return this.$store.state.server_installation.status_meta
        },
        error_message() {
            return this.$store.state.server_installation.error_message
        },
        percentage_is_done() {
           let status = this.$store.state.server_installation.status

            if (status != 'PROGRESS')
                return 0

            let meta = this.$store.state.server_installation.status_meta

            let percentage = (99 * meta.current_number / meta.total).toFixed(0)

            if (percentage > 99)
                percentage = 99;

            return percentage
        },
        server_installation() {
            return this.$store.state.server_installation
        },
        console_minimized() {
            return this.$store.state.console.minimized
        },
    },
    components: {
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

$input_padding: 10px;
$input_form_width: 500px;
$input_form_height: 450px;
$input_width: 500px;
$input_height: 44px;
$color_not_editable_input: #f4f4f4;




.sub_header_and_settings {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 0;
    padding: 0;
    align-items: center;

    .sub_header {
        @include font-main($size: 18px, $height: 125%, $weight: 500);

        margin: {
            top: 10px;
            bottom: 20px;
            right: 10px;
        }
    }

    .label_to_button_advanced_features {
    @include font-main($size: 18px, $height: 125%, $weight: 500);
        display: inline-block;
        line-height: 30px;
        
        margin: {
            right: 15px;
        }

    }

    svg {
        position: relative;
        top: 3px;
    }

    figure {
        display: flex;
        flex-direction: row;
        cursor: pointer;
    }
}



.status_meta {
    margin-top: 45px;
     @include font-main($size: 15px, $height: 125%, $weight: 500);
}

.button-copy-anchor {
    position: relative;
}

.button-copy-message-copied {
    color: #000;
    position:absolute;
    right: 0px;
    bottom: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

#ssh_key {
    padding-right: 46px;
}

.button-copy-figure {
    position:absolute;
    bottom: -$input_height - 3px;
    right: 2px;
    height: $input_height - 4px;
    width: $input_height - 4px;
    display: flex;
    justify-content: center;
    align-items: center;

    svg {
        transform: scale(1.3);
    }

    cursor: pointer;
}


.message {
    max-width: $input_width;
    width: 100%;

    position: relative;
    top: 5px;

    .phrase {
        &-success {
            @include font-main(
                $size: 13px,
                $height: 134%,
                $color: darken($color-green, 20%)
            );

            span {
                @include font-main($size: 13px, $height: 134%, $color: blue);
                cursor: pointer;
            }
        }

        &-failure {
            @include font-main($size: 13px, $height: 134%, $color: $color-red);
        }
    }
}

.input_form {

    .flexed-buttons {
        display: flex;
        flex-direction: row;
        align-items: flex-end;
        justify-content: space-around;
        text-align: center;

        width: 100%;
        height: 50px;
        .button {
            flex-basis: 50%;
            height: 30px;
            cursor: pointer;
            @include font-main($size: 20px, $height: 125%);
        }

        .pressed {
            border-bottom: 3px solid $color-green;
        }
    }

    .horizontal_line {
        background: #c8d0d4;
        height: 2px;
        width: 100%;
    }

    .centralize_form {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        flex-wrap: wrap;
        width: 100%;
        margin-top: 20px;

        .centralize_form_inside {
            width: 100%;
        }

        form {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            align-items: flex-start;
            justify-content: flex-start;

            width: 100%;

            $border-begin-end: 20px;
            margin-top: $border-begin-end;
            .flex-element {
                &-button {
                    margin-top: $border-begin-end;
                }

                &-button_abort {
                    position: relative;
                    top: 30px;
                    left: 0;

                    cursor: pointer;

                    @include font-main($size: 18px, $height: 123%);
                    @include flex-center();
                    text-decoration: underline;

                    width: 250px;
                    height: 50px;
                }

                .validator-error {
                    box-sizing: border-box;
                    max-width: $input_width;
                    width: 100%;
                    position: relative;
                    top: -15px;

                    @include font-main(
                        $size: 13px,
                        $height: 134%,
                        $color: $color-red
                    );
                }

                width: 100%;
                &:nth-child(8) {
                    margin-top: 15px;
                }

                padding: {
                    left: 10px;
                    right: 10px;
                }
                box-sizing: border-box;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .error {
                max-width: $input_width;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                margin-top: 5px;
                @include font-main(
                    $size: 13px,
                    $height: 134%,
                    $color: $color-red
                );
            }

            .progress-bar {
                max-width: $input_width;
                width: 100%;
                height: $input_height;
                background-color: #b8b3b3;

                position: relative;
                top: 0;
                left: 0;

                @include font-main($size: 16px, $color: $color-white);

                &-filling {
                    position: absolute;
                    top: 0;
                    left: 0;
                    background-color: lighten($color-green, 1%);
                    max-width: $input_width;
                    height: 100%;
                    z-index: 1;
                    width: 0;
                    transition: width 5s ease;
                }

                &-words {
                    position: absolute;
                    top: 0;
                    left: 0;
                    z-index: 2;
                    width: 100%;
                    height: 100%;
                    @include flex-center();
                }
            }

            label {
                margin-bottom: 5px;

                box-sizing: border-box;
                max-width: $input_width;
                width: 100%;

                @include font-main(
                    $weight: 500,
                    $size: 13px,
                    $height: 68%,
                    $color: #b0b0b0
                );
            }

            
            input[id="ssh_key"] {
                background: $color_not_editable_input;
            }

            .select {
                text-indent: 12px;
            }
            input {
                text-indent: 10px;
            }

            input,
            .select {
                max-width: $input_width;
                width: 100%;
                height: $input_height;

                margin-bottom: 20px;

                margin-top: 0;

                box-sizing: border-box;
                padding-top: 0px;
                padding-bottom: 0px;

                @include font-main($size: $button-font-size);

                &:not(:focus) {
                    border: 1px solid $button-border-gray;
                }
                &:focus {
                    border: 1px solid #858585;
                }
            }

            .select {
                background: $color_not_editable_input;
                display: flex;
                flex-direction: row;
                align-items: center;
                cursor: default;
            }

            .submit {
                max-width: $input_width;
                width: 100%;
                height: $input_height;

                @include flex-center();

                @include font-main(
                    $size: $button-font-size,
                    $color: $color-white
                );
                cursor: pointer;

                &:not(:hover) {
                    background-color: darken($color-green, 0%);
                }

                &:hover {
                    background-color: darken($color-green, 10%);
                }

                &:active {
                    background-color: darken($color-green, 20%);
                }
            }
        }
    }
}
</style>