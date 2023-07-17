<template>
  <NavBar />

  <QuestionAnswersLayout :header="header" :subheaders="subheaders" :statements="statements" :header_width="90"/>

  <BlackFooter />
  <footer></footer>
</template>

<script>
import NavBar from "@/components/shared/components/NavBar.vue";
import QuestionAnswersLayout from "@/components/extra/QuestionAnswersLayout.vue";
import BlackFooter from "../components/shared/components/BlackFooter.vue";


export default {
  name: 'FAQView',
  mounted() {
    window.scrollTo(0, 0);
    document.title = this.$store.state.brand + " - FAQ";
        document.querySelector('meta[name="description"]').setAttribute("content", "Frequently Asked Questions");
  },
  components: {
    NavBar,
    QuestionAnswersLayout,
    BlackFooter
  },
  computed: {
    header() {
      return this.$i18n.t(`home.white_field.main.most_frequent_questions`)
    },
    subheaders() {
      return []
    },
    statements() {
      let result = []

      for (let step = 1; step <= 8; step++) {
        result.push(
          {
            heading: this.$i18n.t(`home.white_field.introFAQ.${step}.question`),
            content: this.$i18n.t(`home.white_field.introFAQ.${step}.answer`)
          }
        )
      }
      return result
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
</style>