<template>
    <NavBar />

    <div class="white_field">
        <div class="sidebar-object1">
            <div class="sidebar-object2">
                <div class="sidebar-object3">
                    <div class="sidebar-object4">
                        <StepBar />
                    </div>
                </div>
            </div>
        </div>

        <section class="space_at_the_border"></section>
        <section class="white_block">
            <section class="white_block-wrapper">
                <div
                    class="heading heading-installation_requires_server"
                >{{ $i18n.t(`install.MainField.installation_requires_server`) }}</div>
                <BlackField />
            </section>
        </section>

        <div id="anchor-tag-to-begin-server-install"></div>
        <template v-if="is_we_having_server === false">
            <section class="white_block" id="server_buy">
                <section class="white_block-wrapper">
                    <div class="heading heading_main-v1">
                        <div class="step">1</div>
                        <div class="text">{{ $i18n.t(`shared.nav_bar.server_buy`) }}</div>
                    </div>
                    <div class="content">
                        <div class="provider_choice">
                            <p>{{ $i18n.t(`install.MainField.choose_provider`) }}</p>
                            <p>{{ $i18n.t(`install.MainField.we_chose_best_providers_for_you`) + ':' }}</p>
                        </div>
                        <InstructionProviderChoiceVue />
                    </div>
                </section>
            </section>

            <section class="white_block" id="instruction">
                <section class="white_block-wrapper">
                    <h1 class="heading">
                        {{ $i18n.t(`install.VideoInstruction.title`) + ' ' + selected_provider.replace(/(^\w|\s\w)/g, m => m.toUpperCase()) }}

                    </h1>
                    <div class="content">
                        <VideoInstruction />

                        <div class="instruction">
                            <InstructionForServer />
                        </div>
                    </div>
                </section>
            </section>

            <div class="button-to-end-instruction">
                <h1 class="heading_server_install">
                    <TitlePhraseVue
                        :msg="$i18n.t(`install.MainField.begin_VPN_installation_to_server`)"
                    />
                </h1>
                <div
                    class="action-button action-button-green-active"
                    @click="button_go_to_server_install"
                >{{ $i18n.t(`install.MainField.to_install_VPN_to_server`) }}</div>
            </div>
        </template>
        <template v-else-if="is_we_having_server === true">
            <section class="white_block" id="server_install">
                <section class="white_block-wrapper">
                    <div class="heading heading_main-v1">
                        <div class="step">2</div>
                        <div
                            class="text"
                        >{{ $i18n.t(`install.MainField.to_install_VPN_to_server`) }}</div>
                    </div>
                    <div class="content">
                        <InputServerForm />
                    </div>
                </section>
            </section>

            <ConsoleWindowErrorsVue />

            <section class="white_block" id="download_configs">
                <section class="white_block-wrapper">
                    <div class="heading heading_main-v1">
                        <div class="step">3</div>
                        <div class="text">{{ $i18n.t(`install.MainField.download_config_files`) }}</div>
                    </div>
                    <div class="content">
                        <DownloadConfigs />
                    </div>
                </section>
            </section>

            <section class="white_block">
                <section class="white_block-wrapper">
                    <div class="heading heading_main-v1">
                        <div class="step">4</div>
                        <div
                            class="text"
                        >{{ $i18n.t(`install.MainField.download_client_application`) }}</div>
                    </div>
                    <div class="content">
                        <DownloadClient />
                    </div>
                </section>
            </section>

            <section class="white_block">
                <section class="white_block-wrapper">
                    <DownloadClientButton />
                </section>
            </section>
        </template>
        <section class="space_at_the_border"></section>
    </div>

    <BlackFooter />
</template>

<script>
import BlackField from "./components/BlackField.vue";
import BlackFooter from "@/components/shared/components/BlackFooter.vue";
import InputServerForm from './components/InputServerForm.vue';
import InstructionProviderChoiceVue from "./components/InstructionProviderChoice.vue";

import TitlePhraseVue from "@/components/home/components/whitefield/TitlePhrase.vue";
import NavBar from "@/components/shared/components/NavBar.vue";
import VideoInstruction from "./components/VideoInstruction.vue";
import StepBar from "./components/StepBar.vue";
import DownloadConfigs from "./components/DownloadConfigs.vue";
import DownloadClient from "./components/DownloadClient.vue";
import InstructionForServer from "./components/InstructionForServer.vue";
import DownloadClientButton from "./components/DownloadClientButton.vue";
import ConsoleWindowErrorsVue from "./components/ConsoleWindowErrors.vue";

import * as Utils from '@/util.js';
import * as Requests from '@/api.js';

export default {
    components: {
        BlackField,
        BlackFooter,
        InputServerForm,
        InstructionProviderChoiceVue,
        TitlePhraseVue,
        NavBar,
        VideoInstruction,
        StepBar,
        DownloadConfigs,
        DownloadClient,
        InstructionForServer,
        DownloadClientButton,
        ConsoleWindowErrorsVue
    },
    computed: {
        is_we_having_server() {
            return this.$store.state.is_we_having_server
        },
        is_vpn_server_installed() {
            return this.$store.state.server_installation.installed
        },
        selected_provider() {
            return this.$store.state.selected_provider
        }
    },
    methods: {
        button_go_to_server_install() {
            this.$store.commit('set_is_we_having_server', true)
            document.getElementById("anchor-tag-to-begin-server-install").scrollIntoView();
        },

    },
    async mounted() {
        let saved_state = sessionStorage.getItem('is_we_having_server');
        if (saved_state !== null && saved_state !== undefined) {
            let loaded = Utils.json_loads(saved_state)
            this.$store.commit('set_is_we_having_server', loaded['state'])

        }



        if (this.$route.query.anchor == 'instruction') {
            this.$store.commit('set_is_we_having_server', false)
            if (this.$route.query.provider === 'vultr' || this.$route.query.provider === 'linode') {
                this.$store.commit('set_selected_provider', this.$route.query.provider)
            }

            setTimeout(() => {
                var element = document.getElementById("instruction");
                element.scrollIntoView();
            }
            )
        }


        if (this.$route.query.anchor == 'server_buy') {

            this.$store.commit('set_is_we_having_server', false)
            setTimeout(() => {
                var element = document.getElementById("server_buy");
                element.scrollIntoView();
            }
            )
        }

        if (this.$route.query.anchor == 'server_install') {

            this.$store.commit('set_is_we_having_server', true)
            setTimeout(() => {
                var element = document.getElementById("server_install");
                element.scrollIntoView();
            }
            )
        }

        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        // loading ssh keys
        
        if (window.location.host === "localhost:45678") {
            return // we don't need to run the request in Server Side Generation.
        }

        let store = this.$store;
        let ssh_keys = sessionStorage.getItem('ssh_keys');
        if (ssh_keys !== null && ssh_keys !== undefined) {
            let decoded = JSON.parse(ssh_keys);
            this.$store.commit('set_keys', decoded)
        } else {
            while (this.$store.state.keys.private === "generating"){
                await Requests.GetKeys().catch(function (error) {
                    console.log(error)
                    sleep(5000)
                
                }).then(function (response) {
                    if (response === undefined) return
                    sessionStorage.setItem('ssh_keys', JSON.stringify(response.data));
                    store.commit('set_keys', response.data)
                });
            }
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

iframe {
    @include media-width-split-big(550px) {
        height: 500px;
    }
    @include media-width-split-small(550px) {
        height: 300px;
    }
    margin: {
        top: 40px;
        bottom: 40px;
    }
}

.button-to-end-instruction {
    margin: {
        left: $margin-mobile-border;
        right: $margin-mobile-border;
    }
}
.space_at_the_border {
    height: 1px;
}

.white_block {
    @include white-block-width();

    background-color: #fff;

    &-wrapper {
        @include white-block-wrapper-margins();

        margin: {
            top: 38px;
            bottom: 38px;
        }
        padding: {
            top: 38px;
            bottom: 69px;
        }

        .heading {
            @include font-main($size: 30px, $height: 125.5%, $weight: 500);

            margin-bottom: $heading-margin-bottom;

            &-installation_requires_server {
                padding-top: 20px;
                @include font-main($size: 18px, $height: 125.5%, $weight: 500);
            }
        }

        .content {
            width: 100%;

            .provider_choice {
                p:nth-child(1) {
                    @include font-main(
                        $size: 18px,
                        $height: 125.5%,
                        $weight: 500
                    );
                }

                p:nth-child(2) {
                    @include font-main(
                        $size: 15px,
                        $height: 125.5%,
                        $weight: 400,
                        $spacing: 0.02em
                    );

                    margin-top: 14px;
                    margin-bottom: 48px;
                }
            }
        }
    }
}

.heading_main {
    &-v1 {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;

        @include font-main($size: 30px, $height: 125.5%, $weight: 500);

        text-align: center;

        height: $heading_height;

        position: relative;

        @include heading_main-width();

        .step {
            border-radius: 50%;
            border: 3px solid #4da94e;
            box-sizing: border-box;
            height: 60px;
            width: 60px;
            min-width: 60px;
            min-height: 60px;
            @include flex-center();
        }

        .text {
            margin-left: 20px;
        }
    }
}

.heading1 {
    padding-top: 110px;

    margin-top: 0;
    margin-bottom: 70px;
}

.white_field {
    background-color: $color-background-install;
    width: 100%;
}

section.headings {
    text-align: center;
    margin-bottom: 55px;

    h1 {
        margin-top: 100px;
        margin-bottom: 58px;
    }
}

.heading_configs {
    margin-top: 120px;
    margin-bottom: 60px;
}

.heading_download_client {
    margin-top: 120px;
}

.instruction {
    margin-bottom: 50px;
}

.button-to-end-instruction {
    @include flex-center();
    .action-button {
        @include action-button();
    }
    .action-button-green-active {
        @include action-button-green-active();
    }

    background-color: $color-background-install;
    padding-top: 100px;
    padding-bottom: 100px;
}
.client-download-button {
    padding-top: 100px;
    padding-bottom: 100px;
}

.white_field {
    position: relative;
}

.sidebar-object1 {
    @include media-width-split-small(1000px) {
        display: none;
    }

    @include media-height-split-small(650px) {
        display: none;
    }

    position: absolute;
    top: -220px;
    left: 0;
    width: 100%;
    height: calc(100% + 300px);

    z-index: 2;
    pointer-events: none;

    .sidebar-object2 {

        @include margin-auto();
        height: 100%;

        position: relative;

        .sidebar-object3 {
            $width: 150px;
            width: $width;

            position: absolute;
            left: -$width;
            top: 0;
            height: 100%;
            .sidebar-object4 {
                width: $width;
                height: 100vh;

                position: sticky;

                @include flex-center();
                top: 0;
                left: 0;

                z-index: 2;

                @include margin-auto();
            }
        }
    }
}
</style>