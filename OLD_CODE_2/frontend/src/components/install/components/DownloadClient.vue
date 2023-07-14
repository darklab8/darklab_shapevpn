<template>
    <div class="main-field" id="download_client">
        <div class="picture client can_be_disabled scaling-picture">
            <LogoClient />
        </div>
        <div class="picture server can_be_disabled scaling-picture">
            <LogoServer />
        </div>

        <div class="button_download can_be_disabled">
            <template v-if="client_download_state != 'linux'">
                <a
                    :href="client_download_urls[client_download_state]"
                    class="button-link-active button-link"
                >
                    <div class="button_inside-active button_inside">
                        <p>{{ $i18n.t(`install.DownloadClient.download_application`) }}</p>
                    </div>
                </a>
            </template>
            <template v-else>
                <div
                    class="button_inside-active button_inside"
                    @click="linux_instruction_anchor_move"
                >
                    <p>{{ $i18n.t(`install.DownloadClient.download_application`) }}</p>
                </div>
            </template>
        </div>

        <div class="arrow horizontal horizonal_1 can_be_disabled">
            <LogoArrowHorizonal />
        </div>
        <div class="arrow horizontal horizonal_2 can_be_disabled">
            <LogoArrowHorizonal />
        </div>

        <div
            :class="[client_download_state === 'windows' ? 'hovering' : '', 'arrow', 'arrow_1', 'can_be_disabled']"
        >
            <LogoArrow1 />
        </div>
        <div
            :class="[client_download_state === 'android' ? 'hovering' : '', 'arrow', 'arrow_2', 'can_be_disabled']"
        >
            <LogoArrow2 />
        </div>
        <div
            :class="[client_download_state === 'ios' ? 'hovering' : '', 'arrow', 'arrow_3', 'can_be_disabled']"
        >
            <div class="resizer">
                <LogoArrow3 />
            </div>
        </div>
        <div
            :class="[client_download_state === 'macos' ? 'hovering' : '', 'arrow', 'arrow_4', 'can_be_disabled']"
        >
            <LogoArrow4 />
        </div>
        <div
            :class="[client_download_state === 'linux' ? 'hovering' : '', 'arrow', 'arrow_5', 'can_be_disabled']"
        >
            <LogoArrow5 />
        </div>
        <div class="OS windows">
            <div
                :class="[client_download_state === 'windows' ? 'OS_button_pressed' : 'OS_button_not_pressed', 'OS_button']"
                @click="changeOSPlatform('windows')"
            >
                <LogoWindows />
                <p>Windows</p>
            </div>
        </div>
        <div class="OS android">
            <div
                :class="[client_download_state == 'android' ? 'OS_button_pressed' : 'OS_button_not_pressed', 'OS_button']"
                @click="changeOSPlatform('android')"
            >
                <LogoAndroid />
                <p>Android</p>
            </div>
        </div>
        <div class="OS ios">
            <div
                :class="[client_download_state == 'ios' ? 'OS_button_pressed' : 'OS_button_not_pressed', 'OS_button']"
                @click="changeOSPlatform('ios')"
            >
                <LogoIos />
                <p>iOS</p>
            </div>
        </div>
        <div class="OS macos">
            <div
                :class="[client_download_state == 'macos' ? 'OS_button_pressed' : 'OS_button_not_pressed', 'OS_button']"
                @click="changeOSPlatform('macos')"
            >
                <LogoMacos />
                <p>macOS</p>
            </div>
        </div>
        <div class="OS linux">
            <div
                :class="[client_download_state == 'linux' ? 'OS_button_pressed' : 'OS_button_not_pressed', 'OS_button']"
                @click="changeOSPlatform('linux')"
            >
                <LogoLinux />
                <p>GNU/Linux</p>
            </div>
        </div>
    </div>
</template>

<script>
import LogoClient from "../assets/client_download/LogoClient.vue";
import LogoServer from "../assets/client_download/LogoServer.vue";
import LogoArrowHorizonal from "../assets/client_download/LogoArrowHorizonal.vue";
import LogoWindows from "../assets/client_download/LogoWindows.vue";
import LogoAndroid from "../assets/client_download/LogoAndroid.vue";
import LogoIos from "../assets/client_download/LogoIos.vue";
import LogoLinux from "../assets/client_download/LogoLinux.vue";
import LogoMacos from "../assets/client_download/LogoMacos.vue";
import LogoArrow1 from "../assets/client_download/LogoArrow1.vue";
import LogoArrow2 from "../assets/client_download/LogoArrow2.vue";
import LogoArrow3 from "../assets/client_download/LogoArrow3.vue";
import LogoArrow4 from "../assets/client_download/LogoArrow4.vue";
import LogoArrow5 from "../assets/client_download/LogoArrow5.vue";

export default {
    data() {
        return {
            isHovering: false,
        };
    },
    components: {
        LogoClient,
        LogoServer,
        LogoArrowHorizonal,
        LogoWindows,
        LogoAndroid,
        LogoIos,
        LogoLinux,
        LogoMacos,
        LogoArrow1,
        LogoArrow2,
        LogoArrow3,
        LogoArrow4,
        LogoArrow5,
    },
    computed: {
        client_download_state() {
            return this.$store.state.client_download_state
        },
        client_download_urls() {
            return this.$store.state.client_download_urls
        }
    },
    methods: {
        changeOSPlatform(new_platform) {
            this.$store.commit('changeOSPlatform', new_platform)
        },
        linux_instruction_anchor_move() {

            var element_to_scroll_to = document.getElementById('linux_instruction');
            element_to_scroll_to.scrollIntoView();
        }
    }
}
</script>
<style lang="scss" scoped>
@import "@/assets/_style.scss";

@mixin dont_display() {
    display: none;
}

@mixin set-size($size) {
    width: $size;
    height: $size;
    min-width: $size;
    min-height: $size;
}


.OS_button {
    @include media-controllable-mobile(750px) {
        width: 100%;
        height: 100px;
    }
    @include media-controllable-tablet(750px, 1150px) {
        width: 95%;
        height: 100%;
    }
    @include media-controllable-pc(1150px) {
        @include set-size(110px);
    }

    box-sizing: border-box;
    border-radius: 8px;
    @include margin-auto();

    @include flex-center();
    flex-direction: column;

    cursor: pointer;

    @include font-main(
        $weight: 500,
        $size: 11px,
        $height: 123%,
        $color: $color-dark-gray
    );
}

.OS_button_not_pressed {
    border: 2px solid #747474;
}

.OS_button_pressed {
    border: 2px solid #4da94e; // #4da94e

    background: {
        image: url("@/assets/icons/check_mark.svg");
        repeat: no-repeat;
        position: top right;
        size: 40px 40px;
    }
}

@include media-width-split-small(750px) {
    .can_be_disabled {
        @include dont_display();
    }

    .main-field {
        display: flex;
        flex-direction: row;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-around;
        width: 100%;

        .OS {
            box-sizing: border-box;
            width: 40%;

            margin-top: 20px;
        }

        .OS::nth-child(1 + n) {
            margin-top: 20px;
        }
    }
}

@include media-width-split-big(750px) {
    .main-field {
        display: grid;
        grid-template-columns: repeat(12, 8.3333%);
        grid-template-rows: repeat(3, 15%) repeat(2, 27.5%);
        height: 550px;

        .scaling {
            &-picture {
                transform: scale(0.7);
                z-index: 100;
            }
        }

        .arrow {
            transition-property: transform;
            transition-duration: 1s;
            transform: scale(0.8);
        }

        .horizontal {
            width: 100%;
        }
        .hovering {
            transform: scale(1) translateY(0px);
        }

        .button_download {
            grid: {
                column: {
                    start: 5;
                    end: 9;
                }
                row: {
                    start: 2;
                    end: 3;
                }
            }

            @include flex-center();

            a {
                @include link-reset();
            }
            .button-link {
                width: 90%;
            }
            .button_inside {
                @include font-main(
                    $weight: 500,
                    $size: 18px,
                    $height: 123%,
                    $color-enabled: false
                );

                @include flex-center();

                border: 1px solid #4da94e;
                color: $color-green;

                cursor: default;
                &-active {
                    cursor: pointer;
                    &:hover {
                        border: 2px solid #4da94e;
                        color: darken($color-green, 10%);
                    }
                }

                box-sizing: border-box;
                border-radius: 3px;

                width: 100%;
                max-width: 318px;
                margin-left: auto;
                margin-right: auto;
                height: 63px;

                p {
                    width: 100%;
                    height: 100%;
                    @include flex-center();
                }
            }
        }

        .client {
            @include flex-center();
            grid: {
                column: {
                    start: 1;
                    end: 4;
                }
                row: {
                    start: 1;
                    end: 4;
                }
            }
        }

        .server {
            @include flex-center();
            grid: {
                column: {
                    start: 10;
                    end: 13;
                }
                row: {
                    start: 1;
                    end: 4;
                }
            }
        }

        .horizonal_1 {
            @include flex-center();
            grid: {
                column: {
                    start: 4;
                    end: 5;
                }
                row: {
                    start: 2;
                    end: 3;
                }
            }
        }

        .horizonal_2 {
            @include flex-center();
            grid: {
                column: {
                    start: 9;
                    end: 10;
                }
                row: {
                    start: 2;
                    end: 3;
                }
            }
        }

        .arrow_1 {
            @include flex-center();
            grid: {
                column: {
                    start: 3;
                    end: 5;
                }
                row: {
                    start: 3;
                    end: 5;
                }
            }
        }

        .arrow_2 {
            @include flex-center();
            grid: {
                column: {
                    start: 5;
                    end: 6;
                }
                row: {
                    start: 3;
                    end: 5;
                }
            }
        }

        .arrow_3 {
            @include flex-center();
            grid: {
                column: {
                    start: 6;
                    end: 8;
                }
                row: {
                    start: 3;
                    end: 5;
                }
            }

            .resizer {
                display: block;
                object-fit: cover;
                width: 100%;
                height: 250px;
                @include flex-center();
            }
        }

        .arrow_4 {
            @include flex-center();
            grid: {
                column: {
                    start: 8;
                    end: 9;
                }
                row: {
                    start: 3;
                    end: 5;
                }
            }
        }

        .arrow_5 {
            @include flex-center();
            grid: {
                column: {
                    start: 9;
                    end: 11;
                }
                row: {
                    start: 3;
                    end: 5;
                }
            }
        }

        .windows {
            @include flex-center();
            grid: {
                column: {
                    start: 2;
                    end: 4;
                }
                row: {
                    start: 5;
                    end: 6;
                }
            }
        }
        .android {
            @include flex-center();
            grid: {
                column: {
                    start: 4;
                    end: 6;
                }
                row: {
                    start: 5;
                    end: 6;
                }
            }
        }

        .ios {
            @include flex-center();
            grid: {
                column: {
                    start: 6;
                    end: 8;
                }
                row: {
                    start: 5;
                    end: 6;
                }
            }
        }
        .macos {
            @include flex-center();
            grid: {
                column: {
                    start: 8;
                    end: 10;
                }
                row: {
                    start: 5;
                    end: 6;
                }
            }
        }

        .linux {
            @include flex-center();
            grid: {
                column: {
                    start: 10;
                    end: 12;
                }
                row: {
                    start: 5;
                    end: 6;
                }
            }
        }
    }
}
</style>