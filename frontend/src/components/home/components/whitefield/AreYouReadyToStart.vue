<template>
    <div class="flex-container">
        <div class="phrase">
            <p>{{ $i18n.t(`home.white_field.AreYouReadyToStart.title`) }}</p>
        </div>
        <div class="button">
            <ButtonCreateVPN />
        </div>
    </div>
</template>

<script>
import ButtonCreateVPN from "../ButtonCreateVPN.vue";

export default {
    components: { ButtonCreateVPN }
}

</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
.button {
    background-color: $color-green;
    color: $color-white;
}

.flex-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: $color-background-block;
    height: 400px;
    width: 100%;
}

.phrase {
    @include font-main($spacing: 0.01em, $size: 26px, $height: 144%);

    display: flex;
    align-items: center;
    text-align: center;

    margin-left: 5%;
    margin-right: 5%;
    margin-bottom: 40px;
}
</style>