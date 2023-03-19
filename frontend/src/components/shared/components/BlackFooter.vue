<template>
    <footer>
        <div class="gird-is-good">
            <div class="flex-outter-item">
                <div class="rubik">
                    <LogoRubik />
                </div>

                <div class="trademark">
                    <p>© 2020–2021 Shapevpn</p>
                </div>
            </div>

            <div class="flex-outter-item menu">
                <div class="flex-item header">{{ $i18n.t(`shared.BlackFooter.info`).toUpperCase() }}</div>
                <div
                    class="flex-item header"
                >{{ $i18n.t(`shared.BlackFooter.extra`).toUpperCase() }}</div>
                <div
                    class="flex-item header"
                >{{ $i18n.t(`shared.BlackFooter.contacts`).toUpperCase() }}</div>

                <div class="flex-item black-text-button">
                    <router-link
                        to="/terms"
                        class="router_link"
                    >{{ $i18n.t(`shared.BlackFooter.terms_of_usage`) }}</router-link>
                </div>

                <div class="flex-item black-text-button">
                    <router-link to="/FAQ" class="router_link">{{ $i18n.t('shared.nav_bar.FAQ') }}</router-link>
                </div>

                <div class="flex-item black-text flex-item-email">shapevpn.helpcenter@gmail.com</div>
                <div class="flex-item black-text-button">
                    <router-link
                        to="/data"
                        class="router_link"
                    >{{ $i18n.t(`shared.BlackFooter.data_privacy`) }}</router-link>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
import LogoRubik from "../../home/assets/LogoRubik.vue";

export default {
    components: {
        LogoRubik
    },
    methods: {
        move_to_anchor(anchor) {
            this.$store.commit('move_to_anchor', anchor)
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

footer {
    background-color: black;

    width: 100%;

    .gird-is-good {
        @include media-width-split-big(900px) {
            width: 100%;
            display: flex;
            flex-direction: row;

            padding-top: 50px;
            padding-bottom: 50px;

            .flex-outter-item:nth-child(1) {
                flex-basis: 300px;
                min-width: 250px;
                flex-shrink: 1;
            }
            .flex-outter-item:nth-child(2) {
                flex-grow: 1;
                margin-left: auto;
                margin-right: auto;
                max-width: 1000px;
            }

            .rubik {
                @include flex-center();
            }

            .trademark {
                @include flex-center();
            }

            .menu {
                display: grid;
                box-sizing: border-box;
                grid-template-rows: 30px repeat(2, 20px);
                grid-template-columns: 33% 23% 35%;
                column-gap: 30px;
                row-gap: 20px;
            }
        }

        @include media-width-split-small(900px) {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-bottom: 30px;
            padding-top: 20px;

            width: 100%;

            .header {
                display: none;
            }

            .trademark {
                margin-top: 10px;
                margin-bottom: 20px;
            }

            .flex-outter-item {
                width: 100%;
                @include flex-center();

                .flex-item-email {
                    order: 5;
                    padding-top: 20px;
                }
            }

            .flex-outter-item:nth-child(1) {
                padding-top: 20px;
            }
            .flex-outter-item:nth-child(3) {
                padding-top: 20px;
                padding-bottom: 20px;
            }
        }
    }

    .trademark {
        @include font-main(
            $weight: 300,
            $color: darken($color-white, 50%),
            $size: 10px,
            $height: 123%
        );
    }

    .menu {
        @include font-main($color: $color-white, $weight-enabled: false);

        .flex-item {
            box-sizing: border-box;
            padding-left: 10px;
            padding-right: 10px;
        }

        .black-text-button {
            @include black-text-button();
        }
        .black-text,
        .black-text-button {
            @include font-main($color: $color-white, $weight-enabled: false);

            padding-top: 10px;
            padding-bottom: 10px;

            box-sizing: border-box;

            @include media-mobile {
                flex-basis: 100%;
            }

            @include media-tablet {
                flex-basis: 100%;
            }

            @include media-pc {
                flex-basis: 33%;
            }
        }
    }
}
</style>