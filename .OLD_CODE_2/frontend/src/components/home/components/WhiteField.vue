<template>
  <div class="white_field">
    <div class="heading1">
      <TitlePhrase :msg="$i18n.t('home.white_field.main.what_u_receive')" />
    </div>

    <ThreeThingsInARow />

    <TwoColumnFirstPhrases />

    <div class="heading1">
      <TitlePhrase :msg="$i18n.t('home.white_field.main.where_to_buy_server')" />

      <p
        class="sub_header_to_server_buying"
      >{{ $i18n.t('home.white_field.main.we_found_best_providers') }}</p>
    </div>

    <div class="provider_section">
      <ProvidersSection />
    </div>

    <div class="heading1" id="FAQ">
      <TitlePhrase :msg="$i18n.t('home.white_field.main.most_frequent_questions')" />
    </div>

    <div class="FAQ">
      <IntroFAQ />
    </div>

    <AreYouReadyToStart />
  </div>
</template>

<script>
import TwoColumnFirstPhrases from "./whitefield/TwoColumnFirstPhrases.vue";
import TitlePhrase from "./whitefield/TitlePhrase.vue";
import ThreeThingsInARow from "./whitefield/ThreeThingsInARow.vue";
import IntroFAQ from "@/components/home/components/whitefield/IntroFAQ.vue";
import AreYouReadyToStart from "./whitefield/AreYouReadyToStart.vue";
import ProvidersSection from "./whitefield/ProvidersSection.vue";


export default {
  components: {
    TwoColumnFirstPhrases,
    TitlePhrase,
    ThreeThingsInARow,
    IntroFAQ,
    AreYouReadyToStart,
    ProvidersSection
  },
  computed: {

  },
  mounted() {
    if (this.$route.query.anchor == 'FAQ') {

      setTimeout(() => {
        var element = document.getElementById("FAQ");
        element.scrollIntoView();
      }
      )
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.heading1 {
  margin: {
    top: 70px;
    bottom: 70px;
    left: 20px;
    right: 20px;
  }

  .sub_header_to_server_buying {
    margin-top: 62px;
    @include font-main($size: 20px, $height: 125.5%, $spacing: 0.05em);
    margin-left: 20px;
    margin-right: 20px;

    text-align: center;
  }
}
.white_field {
  background-color: $color-white;

  width: 100%;
}

.FAQ {
  margin-bottom: 150px;
}

</style>


