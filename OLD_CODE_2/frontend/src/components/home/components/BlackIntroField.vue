<template>
  <NavBar />
  <div class="black_field"></div>
  <div class="unlimied_black_field">
    <div class="flex-main">
      <div class="beginning"></div>
      <div class="flex-box logo-central flex-box-PC">
        <div class="logo-wrapper">
          <LogoCentral />
        </div>
      </div>
      <div class="flex-box phrase-create flex-box-PC">
        {{
          $i18n.t('home.intro.create_VPN_on_your_server')
        }}
      </div>
      <div class="flex-box gray-line-box flex-box-PC">
        <div class="gray-line-between-phrases"></div>
      </div>
      <div class="flex-box phrase-product-description flex-box-PC">
        {{
          $i18n.t('home.intro.vpn_constructor')
        }}
      </div>

      <div class="flex-box flex-box-rubik flex-box-MOBILE">
        <img alt="shapevpn logo colorful cube at the center of screen, mobile version" src="@/assets/images/rubik_intro_mobile.png" />
      </div>
      <div class="flex-box flex-box-create_personal_vpn flex-box-MOBILE">
        {{
          $i18n.t('home.intro.create_personal_vpn')
        }}
      </div>

      <div class="flex-button">
        <ButtonCreateVPN />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/shared/components/NavBar.vue'
import ButtonCreateVPN from '@/components/home/components/ButtonCreateVPN.vue'
import LogoCentral from '@/components/shared/assets/LogoCentral.vue'

export default {
  components: {
    NavBar,
    ButtonCreateVPN,
    LogoCentral,
  },
  computed: {
  },
  mounted() {

  },
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.black_field {
  background-color: $color-black;

  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  margin: 0px;
  padding: 0px;

  overflow: visible;

  height: 100vh;
  opacity: 1;
  z-index: -1;
}

.unlimied_black_field {
  height: calc(100vh - 100px);

  @include media-width-split-small(800px) {
    height: calc(100vh - 100px);
  }

  z-index: 1000;

  width: 100%;
  margin: 0px;
  padding: 0px;
  .flex-main {
    height: 100%;
    width: 100%;
    display: flex;

    flex-direction: column;
    flex-wrap: nowrap;
    justify-content: center;
    align-content: center;
    align-items: center;

    .beginning {
      flex-basis: 150px;
      flex-shrink: 2;
    }

    .flex-box {
      &-MOBILE {
        display: none;
      }
      @include media-width-split-small(650px) {
        &-PC {
          display: none;
        }
        &-MOBILE {
          display: block;
        }
        &-create_personal_vpn {
          margin-top: 54px;
          margin-bottom: 60px;
          @include font-main(
            $size: 20px,
            $color: #4da94e,
            $spacing: 0.01em,
            $height: 166%
          );
        }
      }
    }
    .logo-central {
      flex-basis: 252px+ 70px;

      @include media-height-mobile() {
        width: 0px;
        display: none;
        flex-basis: 0px;
        height: 0px;
      }

      .logo-wrapper {
        @include media-height-mobile() {
          width: 0px;
        }
        @include media-height-tablet() {
          width: 240px;
        }
        @include media-height-pc() {
          width: 266px;
        }

        width: auto;
      }
    }

    .phrase-create {
      padding: {
        left: 20px;
        right: 20px;
      }
      width: 100%;
      text-align: center;

      @include font-main(
        $height: 125.5%,
        $size-enabled: false,
        $color: $color-white
      );

      @include media-mobile() {
        font-size: 38px;
      }
      @include media-tablet() {
        font-size: 42px;
      }
      @include media-pc() {
        font-size: 46px;
      }

      margin: {
        left: 25px;
        right: 25px;
      }
      @include media-width-split-small(650px) {
        margin: {
          top: 25px;
          bottom: 25px;
        }
      }

      flex-basis: 58px+40px;
    }
    .gray-line-box {
      flex-basis: 31px;
      width: 100%;

      .gray-line-between-phrases {
        margin-left: auto;
        margin-right: auto;
        width: 80%;
        max-width: 520px;

        height: 1px;
        background: rgba(176, 176, 176, 0.7);
      }
    }

    .phrase-product-description {
      flex-basis: 38px + 90px;
      @include font-main(
        $height: 146%,
        $color: darken($color-green, 5%),
        $spacing: 0.09em,
        $size-enabled: false
      );

      font-size: 26px;

      text-align: center;
    }
    .flex-button {
      flex-basis: 200px;
    }
  }
}
</style>