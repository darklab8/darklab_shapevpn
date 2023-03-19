<template>
    <div class="step_bar" id="side_bar">
        <div
            :class="[(!is_we_having_server && (scrolling_states.server_buy_choice || scrolling_states.clicked_i_have_no_server)) || is_we_having_server ? 'cycle-active' : 'cycle-not-active', 'cycle']"
        >
            <div class="number">1</div>
        </div>
        <p
            :class="[(!is_we_having_server && (scrolling_states.server_buy_choice || scrolling_states.clicked_i_have_no_server)) || is_we_having_server ? 'words-active' : 'words-not-active', 'words']"
        >
            <span v-html="$i18n.t(`install.StepBar.server_buying`)"></span>
        </p>

        <div
            :class="[is_we_having_server || (scrolling_states.server_buy_instruction && !is_we_having_server) ? 'vertical-bar-active' : 'vertical-bar-not-active', 'vertical-bar']"
        ></div>
        <div :class="[is_we_having_server ? 'cycle-active' : 'cycle-not-active', 'cycle']">
            <div class="number">2</div>
        </div>
        <p :class="[is_we_having_server ? 'words-active' : 'words-not-active', 'words']">
            <span v-html="$i18n.t(`install.StepBar.server_installation`)"></span>
        </p>

        <div
            :class="[is_we_having_server && scrolling_states.server_install ? 'vertical-bar-active' : 'vertical-bar-not-active', 'vertical-bar']"
        ></div>
        <div
            :class="[is_we_having_server && server_installation.installed && scrolling_states.download_configs ? 'cycle-active' : 'cycle-not-active', 'cycle']"
        >
            <div class="number">3</div>
        </div>
        <p
            :class="[is_we_having_server && server_installation.installed && scrolling_states.download_configs ? 'words-active' : 'words-not-active', 'words']"
        >
            <span v-html="$i18n.t(`install.StepBar.download_configs`)"></span>
        </p>

        <div
            :class="[is_we_having_server && scrolling_states.download_client ? 'vertical-bar-active' : 'vertical-bar-not-active', 'vertical-bar']"
        ></div>
        <div
            :class="[is_we_having_server && scrolling_states.download_client ? 'cycle-active' : 'cycle-not-active', 'cycle']"
        >
            <div class="number">4</div>
        </div>
        <p
            :class="[is_we_having_server && scrolling_states.download_client ? 'words-active' : 'words-not-active', 'words']"
        >
            <span v-html="$i18n.t(`install.StepBar.download_client`)"></span>
        </p>
    </div>
</template>

<script>

export default {
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    },
    unmounted() {
        window.removeEventListener('scroll', this.handleScroll);
    },

    components: {
    },
    computed: {
        scrolling_states() {
            return this.$store.state.scrolling_states
        },
        is_we_having_server() {
            return this.$store.state.is_we_having_server
        },
        server_installation() {
            return this.$store.state.server_installation
        }
    },



    methods: {

        handleScroll() {
            // Any code to be executed when the window is scrolled

            this.$store.commit("check_scrollings")
        },
        WinWidth: function () {
            // `this` points to the vm instance
            return screen.width
        },
        WinHeight: function () {
            // `this` points to the vm instance
            return screen.height
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

@mixin progress-bar-percentage($percent) {
    background: linear-gradient(
        $color-green 0%,
        $color-green $percent,
        $color-progress-side-bar $percent,
        $color-progress-side-bar 100%
    );
    // transform: scale($percent / 100);
}

@keyframes progress-bar-in {
    @for $i from 0 through 100 {
        #{$i * 1%} {
            @include progress-bar-percentage(#{$i * 1%});
        }
    }
}

@keyframes progress-bar-out {
    @for $i from 0 through 100 {
        #{$i * 1%} {
            @include progress-bar-percentage(#{(100-$i) * 1%});
        }
    }
}

.step_bar > div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.step_bar {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 75%;

    .cycle {
        border-radius: 50%;

        &-active {
            border: 2px solid $color-green;
            color: $color-font-main;
        }
        &-not-active {
            border: 2px solid $color-sidebar-disabled;
            color: $color-sidebar-disabled;
        }

        $size: 32px; //supposed to be 32px;
        min-height: $size;
        width: $size;
        height: $size;

        @include font-main(
            $weight: 500,
            $size: 13px,
            $height: 123%,
            $color-enabled: false
        );

        @include flex-center();

        margin-top: 14px;
        margin-bottom: 10p;

        padding: 0;
        .number {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        flex-grow: 0;
        flex-shrink: 0;
    }

    .vertical-bar {
        background-color: $color-progress-side-bar;

        &-not-active {
            animation: {
                name: progress-bar-out;
                duration: 1s;
                iteration-count: 1;
                fill-mode: forwards;
            }
        }
        &-active {
            animation: {
                name: progress-bar-in;
                duration: 1s;
                iteration-count: 1;
                fill-mode: forwards;
            }
        }
        width: 2px;

        flex-basis: 50px;
        flex-grow: 1;
        flex-shrink: 1;

        margin-top: 8px;
        margin-bottom: 14px;
    }

    .words {
        @include font-main(
            $weight: 500,
            $size: 13px,
            $height: 108%,
            $color-enabled: false
        );

        @include flex-center();

        &-active {
            color: $color-font-main;
        }
        &-not-active {
            color: $color-sidebar-disabled;
        }

        text-align: center;

        margin-top: 10px;
        margin-bottom: 4px;

        flex-grow: 0;
        flex-shrink: 0;
    }
}
</style>