<template>
    <div class="selector" @mouseleave="selector.active = false">
        <div class="selector-wrapper">
            <div class="chosen" @click="selector.active = !selector.active">
                <p>{{ $i18n.t(`install.DownloadConfigs.user`, { number: selected_user }) }}</p>
                <figure
                    :class="[selector.active ? 'figure-active' : 'figure-not-active', 'figure']"
                >
                    <svg
                        width="12"
                        height="9"
                        viewBox="0 0 12 9"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path d="M6 9L11.1962 0H0.803848L6 9Z" fill="#747474" />
                    </svg>
                </figure>
            </div>
            <div :class="[selector.active ? 'dropdown-active' : 'dropdown-not-active', 'dropdown']">
                <div
                    v-for="number in [1, 2, 3, 4, 5]"
                    :key="number.id"
                    class="option"
                    @click="set_selected(number)"
                >{{ $i18n.t(`install.DownloadConfigs.user`, { number: number }) }}</div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            selector: {
                active: false,
            }
        };
    },
    components: {

    },
    mounted() {
    },
    computed: {
        selected_user() {
            return this.$store.state.download_configs_selector.selected
        },
    },
    methods: {
        set_selected(number) {
            this.$store.commit('set_download_configs_selector', number)
            this.selector.active = false
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.selector {
    @include font-main($size: $button-font-size);
    &-wrapper {
        width: 100%;

        box-sizing: border-box;

        position: relative;
        top: 0;
        left: 0;
        height: $button-create-vpn-height;

        z-index: 5;
        cursor: pointer;

        .chosen {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            text-indent: 20px;

            border: 1px solid $button-border-gray;

            p,
            .figure {
                height: 100%;
            }

            p {
                width: 90%;
                display: flex;
                flex-direction: row;
                align-items: center;
            }
            .figure {
                width: 10%;
                @include flex-center();

                &-not-active {
                    transform: translateY(2px);
                }
                &-active {
                    transform: rotate(180deg) translateY(0px);
                }
            }
        }

        .dropdown {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;

            &-not-active {
                display: none;
            }

            .option {
                background-color: #fff;
                &:hover {
                    background-color: darken(#fff, 5%);
                }

                &:active {
                    background-color: darken(#fff, 15%);
                }
            }

            @for $i from 0 through 5 {
                .option:nth-child(#{$i}) {
                    position: absolute;

                    $number: $i - 1;
                    top: -1px + 49px * $number;

                    left: 0;

                    box-sizing: border-box;

                    border: 1px solid $button-border-gray;

                    height: 50px;
                    width: 100%;

                    display: flex;
                    flex-direction: row;
                    justify-content: flex-start;
                    align-items: center;
                    text-indent: 20px;
                }
            }
        }
    }
}
</style>