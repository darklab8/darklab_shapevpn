<template>
  <NavBar />

  <QuestionAnswersLayout :header="header" :subheaders="subheaders" :statements="statements" :header_width="30"/>

  <BlackFooter />
  <footer></footer>
</template>

<script>
import NavBar from "@/components/shared/components/NavBar.vue";
import QuestionAnswersLayout from "@/components/extra/QuestionAnswersLayout.vue";
import BlackFooter from "../components/shared/components/BlackFooter.vue";


export default {
  name: 'PoliticsView',
  mounted() {
    window.scrollTo(0, 0);
    document.title = this.$store.state.brand + " - Terms of Service";
        document.querySelector('meta[name="description"]').setAttribute("content", "Terms of Service for ShapeVPN usage");
  },
  components: {
    NavBar,
    QuestionAnswersLayout,
    BlackFooter
  },
  computed: {
    header() {
      return this.$i18n.t(`politics.title`)
    },
    subheaders() {
      return [this.$i18n.t(`politics.first_phrase`), this.$i18n.t(`politics.second_phrase`)]
    },
    statements() {
      let result = []

      for (let step = 1; step <= 8; step++) {
        result.push(
          {
            heading: this.$i18n.t(`politics.statements.${step}.heading`),
            content: this.$i18n.t(`politics.statements.${step}.content`)
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