<template>
    <div class="main-field">
        <div class="field-item field-item-selector">
            <DownloadConfigsSelector />
        </div>

        <div class="field-item field-item-qrcode">
            <template v-if="configs !== null">
                <div class="image-resizer">
                    <img
                        alt="qr code containing wireguard config for mobile device"
                        class="qr_code qr_code-normal"
                        :src="'data:image/png;base64, ' + encodeURIComponent(configs[selected_user + '.png'])"
                    />
                </div>
            </template>
            <template v-else>
                <div class="image-resizer">
                    <img alt="gif animation of qr code, containing wireguard config for mobile device, which is building itself like in tetris" class="qr_code qr_code-default" src="@/assets/icons/default-qrcode.gif" />
                </div>
            </template>
        </div>

        <div class="field-item field-item-read_qrcode">
            <p
                class="words"
                v-html="$i18n.t(`install.DownloadConfigs.read_QR_code`, { number: selected_user })"
            ></p>
        </div>

        <div class="field-item">
            <template v-if="configs !== null">
                <a
                    :href="'data:text/plain;charset=utf-8,' + encodeURIComponent(decoder(configs[selected_user + '.conf']))"
                    :download="selected_user + '.conf'"
                    class="button-link"
                >
                    <div
                        class="button button-active"
                    >{{ $i18n.t(`install.DownloadConfigs.download_config_file`, { filename: selected_user + ".conf" }) }}</div>
                </a>
            </template>
            <template v-else>
                <div
                    class="button button-not-active"
                >{{ $i18n.t(`install.DownloadConfigs.download_config_file`, { filename: selected_user + ".conf" }) }}</div>
            </template>
        </div>

        <div class="field-item">
            <p class="words words-or">{{ $i18n.t(`install.DownloadConfigs.or`) }}</p>
        </div>

        <div class="field-item">
            <template v-if="configs !== null">
                <a
                    :href="'data:application/zip;base64,' + encodeURIComponent(configs['zip'])"
                    download="configs.zip"
                    class="button-link"
                >
                    <div class="button button-active">
                        <span
                            v-html="$i18n.t(`install.DownloadConfigs.download_config_files_and_QR_codes_for_5_users`)"
                        ></span>
                    </div>
                </a>
            </template>
            <template v-else>
                <div class="button button-not-active">
                    <span
                        v-html="$i18n.t(`install.DownloadConfigs.download_config_files_and_QR_codes_for_5_users`)"
                    ></span>
                </div>
            </template>
        </div>
    </div>
</template>

<script>

import DownloadConfigsSelector from "./DownloadConfigsSelector.vue"

export default {
    data() {
        return {
            email: '',

            selector: {
                active: false,
            }
        };
    },
    components: {
        DownloadConfigsSelector
    },
    mounted() {
    },
    computed: {
        configs() {
            return this.$store.state.server_installation.configs
        },
        selected_user() {
            return this.$store.state.download_configs_selector.selected
        },
        button_active: function() {

        return {
          'background-image': 'url("/check_mark.svg")',
      }
      }
    },
    methods: {
        decoder(data) {
            return atob(data)
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.words-or {
    padding: 5px;
}

.normal_qr_code {
    transform: scale(1.2) translateY(10px);
}
.button-link {
    @include flex-center();
}

.main-field {
    @include font-main($size: 14px, $height: 123%, $color-enabled: false);
    width: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .field-item {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;

        &:nth-child(n + 2) {
            margin-top: 10px;
        }

        &-qrcode {
            .image-resizer {
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
                width: 300px;

                margin: 0;
            }
        }

        &-read_qrcode {
            position: relative;
            top: -20px;
            margin-bottom: 0px;
            text-align: center;
        }
    }

    .qr_code {
        width: 100%;
        max-width: 300px;
    }
}

a {
    width: 100%;
    @include link-reset();
}

input,
select,
.button,
.selector,
option {
    box-sizing: border-box;
    width: 100%;
    max-width: 492px;
}

.button {
    height: 50px;
}

select {
    padding-top: 5px;
    padding-bottom: 5px;
}
.button {
    @include flex-center();
    color: $color-white;

    &-not-active {
        $button-color: rgb(184, 184, 184);
        background-color: $button-color;

        &:hover {
            background-color: darken($button-color, 10%);
        }

        &:active {
            background-color: darken($button-color, 20%);
        }
    }
    &-active {
        cursor: pointer;
        background-color: $color-blue;

        &:hover {
            background-color: darken($color-blue, 10%);
        }

        &:active {
            background-color: darken($color-blue, 20%);
        }
    }
}

select,
input {
    border: 1px solid #c8d0d4;
    border-radius: 3px;
    background: #fff;
    box-sizing: border-box;
    padding-left: 27px;
}

.button-send-email {
    background-color: $color-green;

    &:hover {
        background-color: darken($color-green, 10%);
    }

    &:active {
        background-color: darken($color-green, 20%);
    }
}
</style>