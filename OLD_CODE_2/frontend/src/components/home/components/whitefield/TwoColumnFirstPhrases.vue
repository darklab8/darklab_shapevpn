<template>
    <div class="two-column-first-phrase">
        <div class="margin-wrapper">
            <div class="flex-item">
                <p v-html="$i18n.t(`home.white_field.TwoColumnFirstPhrases.msg`)"></p>
            </div>
            <div class="flex-item logo-shield">
                <ServerShield />
            </div>
        </div>
    </div>
</template>

<script>
import ServerShield from "@/components/home/assets/ServerShield.vue"

export default {
    components: {
        ServerShield
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.two-column-first-phrase {
    width: 100%;
    background-color: $color-background-block;
    padding-top: 60px;
    padding-bottom: 60px;
}
.margin-wrapper {
    @include margin-auto();

    display: flex;

    align-items: center;
    justify-content: space-around;
    align-content: center;

    @include media-width-split-small(750px) {
        flex-direction: column-reverse;

        .flex-item {
            width: 90%;
        }

        .flex-item:last-child {
            @include flex-center();
        }
    }
    @include media-width-split-big(750px) {
        flex-direction: row;
        .flex-item {
            width: 40%;
        }
    }

    .flex-item {
        height: auto;

        padding: 2%;

        margin-top: 20px;
        margin-bottom: 20px;
    }

    .flex-item:nth-child(1) {
        @include font-main($size: 25px, $height: 124%, $spacing: 0.01em);

        flex-grow: 1;
    }

    .flex-item:nth-child(2) {
        flex-basis: 450px;
        display: flex;
        flex-direction: row-reverse;
    }
}
</style>