<template>
    <div class="white_field">
        <section class="space_at_the_border"></section>
        <section class="heading">
            <h1>{{ $i18n.t(`data.title`) }}</h1>
            <div class="text">
                <p>{{ $i18n.t(`data.we_obtain.title`) }}:</p>
                <ul>
                    <li v-for="statement in obtained_info" :key="statement.id">{{ statement }}</li>
                </ul>
                <p>{{ $i18n.t(`data.we_dont_obtain.title`) }}:</p>
                <ul>
                    <li v-for="statement in not_obtained_info" :key="statement.id">{{ statement }}</li>
                </ul>
            </div>
        </section>
    </div>
</template>

<script>

export default {
    components: {

    },
    computed: {
        obtained_info() {
            let result = []

            for (let step = 1; step <= 1; step++) {
                result.push(
                    this.$i18n.t(`data.we_obtain.${step}`)
                )
            }
            return result
        },
        not_obtained_info() {
            let result = []

            for (let step = 1; step <= 2; step++) {
                result.push(
                    this.$i18n.t(`data.we_dont_obtain.${step}`)
                )
            }
            return result
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

* {
    margin: 0;
    padding: 0;
}

.space_at_the_border {
    height: 1px;
}

section {
    @include margin-auto($max-width: 1000px);
}

.heading {
    h1 {
        margin-top: 77px;
        margin-bottom: 77px;

        @include font-main($height: 36px, $size: 30px, $color: $color-black);
    }

    .text {
        margin-bottom: 77px;
    }

    p {
        @include font-main($height: 142%, $size: 15px, $weight: 600);

        margin-bottom: 10px;
        margin-top: 30px;
    }
    ul {
        padding-left: 20px;
    }
    li {
        @include font-main($height: 182%, $size: 15px);
    }
}

.white_field {
    background-color: $color-white;
    width: 100%;
    min-height: 70vh;
}
</style>


