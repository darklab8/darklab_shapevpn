<template>
    <div class="black_field">
        <div class="buttons-flexed">
            <div
                :class="[is_we_having_server === false ? 'pressed' : 'not_pressed', 'button']"
                @click="set_is_we_having_server(false)"
            >
                <h2>
                    <span v-html="$i18n.t(`install.intro.i_have_no_server.title`)"></span>
                </h2>
                <p>{{ $i18n.t(`install.intro.i_have_no_server.notes`) }}</p>
            </div>
            <div class="space"></div>
            <div
                :class="[is_we_having_server === true ? 'pressed' : 'not_pressed', 'button']"
                @click="set_is_we_having_server(true)"
            >
                <h2>
                    <span v-html="$i18n.t(`install.intro.i_have_server.title`)"></span>
                </h2>
                <p>{{ $i18n.t(`install.intro.i_have_server.notes`) }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {

    components: {
    },
    computed: {
        is_we_having_server() {
            return this.$store.state.is_we_having_server
        }
    },
    methods: {
        set_is_we_having_server(new_status) {
            this.$store.commit('set_is_we_having_server', new_status)
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.black_field {
    width: 100%;

    .button {
        padding: {
            top: 25px;
            bottom: 25px;
        }
    }

    @include media-width-split-small(750px) {
        .buttons-flexed {
            flex-wrap: wrap;
        }

        .button:last-child {
            margin-top: 20px;
        }
    }

    @include media-width-split-big(750px) {
    }

    .buttons-flexed {
        display: flex;
        flex-direction: row;
        @include media-width-split-small(750px) {
            justify-content: space-around;

            .space {
                display: none;
            }
        }
        @include media-width-split-big(750px) {
            justify-content: space-between;

            .space {
                width: $provider-button-space;
            }
        }

        align-items: stretch;
        width: 100%;
        height: 100%;

        .button {
            border-radius: 10px;

            border: $color-font-main;

            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;

            text-align: left;

            width: 450px;

            box-sizing: border-box;

            @include hovering-scale();

            $space-left: 20%;
            h2 {
                @include font-main($weight: 500, $size: 20px, $height: 123%);
                padding: {
                    top: 40p;
                    left: $space-left;
                    right: $space-left;
                    bottom: 0px;
                }
            }

            p {
                @include font-main(
                    $weight: 300,
                    $size: 13px,
                    $height: 148%,
                    $spacing: 0.005em
                );

                padding: {
                    bottom: 40p;
                    left: $space-left;
                    right: $space-left;
                    top: 5px;
                }
            }
        }

        .not_pressed {
            border: $button-border-size solid $color-light-gray;
            cursor: pointer;
        }

        .pressed {
            border: $button-border-size solid $color-green;
            background: {
                image: url("@/assets/icons/check_mark.svg");
                repeat: no-repeat;
                position: 101% -2%;
            }
        }
    }
}
</style>


