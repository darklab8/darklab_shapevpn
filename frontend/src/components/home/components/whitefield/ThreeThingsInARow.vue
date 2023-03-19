<template>
  <div class="three-green-things-grid">
    <template v-for="item in green_things" :key="item.id">
      <div class="text-thing">
        <figure>
          <div v-if="item.icon === 1">
            <GreenIcon1 />
          </div>
          <div v-else-if="item.icon === 2">
            <GreenIcon2 />
          </div>
          <div v-else-if="item.icon === 3">
            <GreenIcon3 />
          </div>
        </figure>
        <p class="title">{{ item.title }}</p>
        <p class="msg" v-html="item.msg"></p>
      </div>

      <div class="green-vertical-line"></div>
    </template>
  </div>
</template>

<script>
import GreenIcon1 from "@/components/whitefield/assets/GreenIcon1.vue";
import GreenIcon2 from "@/components/whitefield/assets/GreenIcon2.vue";
import GreenIcon3 from "@/components/whitefield/assets/GreenIcon3.vue";


export default {
  mounted() {

  },
  components: {
    GreenIcon1,
    GreenIcon2,
    GreenIcon3
  },
  computed: {
    green_things() {
      let result = []

      for (let step = 1; step <= 3; step++) {
        result.push(

          {
            title: this.$i18n.t(`home.white_field.ThreeThingsInARow.${step}.title`).toUpperCase(),
            msg: this.$i18n.t(`home.white_field.ThreeThingsInARow.${step}.msg`),
            icon: step
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

.three-green-things-grid {
  @include margin-auto();

  margin-top: 90px;
  margin-bottom: 150px;

  @include media-mobile {
    display: grid;
    grid-template-rows: 32% 1% 32% 1% 32% 1%;
    grid-template-columns: 1fr;
  }

  @include media-tablet {
    display: grid;
    grid-template-rows: 32% 1% 32% 1% 32% 1%;
    grid-template-columns: 1fr;
  }

  @include media-pc {
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: 32% 1% 32% 1% 32% 1%;
  }

  .text-thing {
    @include font-main($size: 14px, $height: 130.5%, $spacing: 0.01em);

    padding: 30px;

    figure {
      height: 67px;
      display: flex;
      flex-direction: column-reverse;
    }

    p.title {
      margin-top: 43px;
    }

    p.msg {
      margin-top: 24px;
    }
  }

  .green-vertical-line {
    background: #4da94e;

    @include media-mobile {
      width: 100%;
      height: 1px;

      margin: {
        top: 5px;
        bottom: 5px;
      }
    }

    @include media-tablet {
      width: 100%;
      height: 1px;

      margin: {
        top: 5px;
        bottom: 5px;
      }
    }

    @include media-pc {
      width: 1px;
      height: 30wh;
    }
  }
}
</style>