<template>
  <div class="white_field">
    <section class="heading">
      <h1>{{ header }}</h1>
      <div class="text">
        <p v-for="subheader in subheaders" :key="subheader.id"
        >{{ subheader }}</p>
      </div>
    </section>
    <section class="statements">
      <article v-for="statement in statements" :key="statement.id">
        <div class="horizontal_line"></div>
        <div class="flexbox-container">
          <div class="flexbox-item vertical_line"></div>
          <div class="flexbox-item heading" :style="{ 'flex-basis': header_width + '%' }" v-html="statement.heading"></div>
          <div class="flexbox-item space-between"></div>
          <div class="flexbox-item content" v-html="statement.content"></div>
        </div>
      </article>
    </section>
  </div>
</template>

<script>

export default {
  props: {
    header: String,
    subheaders: Array,
    statements: Array,
    header_width: Number
  },
  components: {

  },
  computed: {

  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

* {
  margin: 0;
  padding: 0;
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
    @include font-main($height: 142%, $size: 15px);

    margin-bottom: 15px;
  }
}

.statements {
  margin-bottom: 134px;

  article {
    .horizontal_line {
      height: 1px;
      width: 100%;
      background: #d2d2d2;
    }

    .flexbox-container {
      display: flex;

      align-items: flex-start;

      @include media-width-split-small(750px) {
        flex-direction: row;
        flex-wrap: wrap;

        .heading {
          flex-basis: 200px;
          box-sizing: border-box;
          order: -1;
        }

        .content {
          flex-basis: 100%;
          box-sizing: border-box;
          margin-bottom: 43px;
        }

        .vertical_line {
          height: 1px;
          width: 100%;
          background: $color-green;
        }
      }

      @include media-width-split-big(750px) {
        flex-direction: row;

        .heading {
          margin-bottom: 43px;
          margin-top: 43px;
        }

        .content {
          flex-basis: 90%;
          margin-bottom: 43px;
          margin-top: 43px;
          margin-left: 43px;
        }

        .vertical_line {
          margin-top: 43px;
          margin-bottom: 43px;

          height: 60px;
          width: 1px;
          background: $color-green;
          margin-right: 27px;
        }
      }

      .flexbox-item {
        margin-top: 20px;
      }

      .heading {
        margin-right: 43px;

        @include font-main($height: 30px, $size: 20px);
      }

      .content {
        @include font-main($height: 142%, $size: 15px);
      }

      .space-between {
        flex-basis: 0px;
        flex-grow: 1;
      }
    }
  }
}

.white_field {
  background-color: $color-white;
  width: 100%;
}
</style>


