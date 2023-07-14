
<template>
    <div class="console">
        <div
            class="console-wrapper"
            :class="[server_installation.visible_log ? 'console-wrapper-active' : 'console-wrapper-not-active', 'console-wrapper']"
            :style="{ height: console_height + 'px' }"
            @mouseleave="up($event)"
            @mousemove="move($event)"
            v-if="is_console_visible"
        >
            <div class="console-heading" @mouseup="up($event)" @mousedown="down($event)">
                <div class="terminal">Stdout Log</div>
                <div class="button-minimize" @click="turn_visisibility()">
                    <template v-if="!minimized">—</template>
                    <template v-else>+</template>
                </div>
            </div>
            <!-- server_installation.visible_log -->
            <div class="console-wrapper-text">
                <p
                    class="console-wrapper-msg"
                    v-for="message in server_installation.stdout.split('\n')"
                    :key="message.id"
                >
                    <span>{{ message }}</span>
                </p>
            </div>
        </div>
    </div>
</template>

    <script>

export default {
    data() {
        return {
            resizing: false,
            mouse_position: 0,
        };
    },
    mounted() {
        let minimized_state = sessionStorage.getItem('console_minimized')
        if (minimized_state === 'true') this.$store.commit(`set_console_minimized`, true)
    },

    methods: {
        turn_visisibility() {
            this.$store.commit(`set_console_minimized`, !this.minimized)
        },
        down(event) {
            this.resizing = true;
            this.mouse_position = event.clientY;
        },
        move(event) {
            if (this.resizing) {
                this.$store.commit('set_console_height', document.documentElement.clientHeight - event.clientY + 25);
            }
        },
        up() {
            this.resizing = false;
        },
    },
    computed: {
        server_installation() {
            return this.$store.state.server_installation
        },
        minimized() {
            return this.$store.state.console.minimized
        },
        console_height() {
            return this.$store.state.console.height
        },
        is_console_visible() {
            return this.$store.getters.is_console_visible
        }
    },
    components: {
    }
}



</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.console {
    $height: 30vh;
    $console-background-color: #383732;
    $console-darkened-color: darken($console-background-color, 10%);
    z-index: 100001;

    &-heading {
        cursor: n-resize;

        width: 100%;
        background-color: $console-darkened-color;
        z-index: 11;
        margin: 0;
        padding: 0;

        display: flex;
        flex-direction: row;
        justify-content: space-between;

        .terminal {
            background-color: $console-background-color;
            margin: 0;
            padding: {
                left: 30px;
                right: 30px;
                top: 5px;
                bottom: 5px;
            }
        }

        .button {
            &-minimize {
                cursor: pointer;
                padding: {
                    left: 15px;
                    right: 15px;
                    top: 5px;
                    bottom: 5px;
                }

                @include font-main(
                    $size: 16px,
                    $color: $color-white,
                    $family: monospace,
                    $height: 150%,
                    $weight: 1000
                );
            }
        }
    }

    &-wrapper {
        position: fixed;
        bottom: 0;
        left: 0;
        z-index: 10;

        width: 100%;

        background-color: $console-background-color;


        overflow: auto;

        margin: 0;
        padding: 0;

        display: flex;
        flex-direction: column;
        justify-content: flex-end;

        @include font-main(
            $size: 16px,
            $color: $color-white,
            $family: monospace,
            $height: 150%
        );

        text-align: left;

        &-msg {
            margin-left: 15px;
            margin-bottom: 15px;
        }

        &-text {
            overflow-y: auto;
            width: 100%;
            flex-grow: 1;
        }
    }
}
</style>