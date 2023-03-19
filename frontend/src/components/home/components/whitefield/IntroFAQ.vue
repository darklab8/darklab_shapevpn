<template>
    <template v-for="item in questions" :key="item.id">
        <IntroFAQAnswer :question="item.question" :answer="item.answer" :number="item.number" />
    </template>
</template>

<script>
import IntroFAQAnswer from "./IntroFAQAnswer.vue"
export default {
    computed: {

        questions() {
            let questions = []

            for (let number = 1; number <= 8; number++)
                questions.push(
                    {
                        question: this.$i18n.t(`home.white_field.introFAQ.${number}.question`),
                        answer: this.$i18n.t(`home.white_field.introFAQ.${number}.answer`),
                        number: number
                    }
                )
            return questions
        }

    },
    components: { IntroFAQAnswer }
}

</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
</style>