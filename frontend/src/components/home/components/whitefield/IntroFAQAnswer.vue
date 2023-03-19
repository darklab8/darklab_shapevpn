<template>
    <div>
        <p
            class="question-button"
            @click="switch_slider"
            v-bind:class="{ question_active: opened, question_not_active: !opened }"
        >
            <span class="margined-question">
                <span class="question-text">{{ question }}</span>

                <span class="sign" v-if="!opened">+</span>
                <span class="sign" v-else-if="opened">-</span>
            </span>
        </p>

        <div v-if="opened" class="answer">
            <div class="margined-answer">
                <p v-html="answer"></p>
            </div>
        </div>

        <div class="hr"></div>
    </div>
</template>

<script>
export default {
    props: {
        question: String,
        answer: String,
        number: Number,
    },
    methods: {
        switch_slider() {
            if (this.opened_FAQ_question === this.number) this.$store.commit('set_opened_FAQ_question', null)
            else this.$store.commit('set_opened_FAQ_question', this.number)

        }
    },
    computed: {
        opened_FAQ_question() {
            return this.$store.state.opened_FAQ_question
        },
        opened() {
            return this.$store.state.opened_FAQ_question === this.number
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
.hr {
    height: 1px;
    background: #c8d0d4;
}
.answer {
    @include font-main(
        $weight: 300,
        $height: 185%,
        $spacing: 0.01em,
        $size: 14px
    );

    display: flex;
    align-items: center;
    padding-top: $padding-main;
    padding-bottom: $padding-main;

    margin: 0;

    background: $color-black;
    color: $color-white;

    .margined-answer {
        @include margin-auto();
    }
}

.question-button {
    @include font-main($height: 123%, $spacing: 0.01em, $size: 20px);

    padding-top: $padding-main;
    padding-bottom: $padding-main;
    margin-top: 0;
    margin-bottom: 0;

    cursor: pointer;

    height: 63px;

    @include media-width-split-small(600px) {
        height: 90px;
    }

    text-align: left;
    display: flex;
    justify-content: flex-start;
    align-items: center;

    padding-top: 34px;
    padding-bottom: 34px;

    .margined-question {
        @include margin-auto();

        display: flex;
        align-items: center;
        justify-content: space-between;

        .sign {
            margin-left: 20px;
        }
    }
}

.question_not_active {
    background: #fff;
    color: $color-font-main;

    &:hover {
        background-color: darken($color-white, 10%);
    }
}

.question_active {
    background: #000;
    color: $color_white;

    &:hover {
        background-color: lighten(#000, 20%);
    }
}

.sign {
    font-size: 32px;
    font-weight: 300;
}
</style>