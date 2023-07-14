<template>
  <div id="top" class="flex-navbar">
    <nav>
      <div class="nav-item rubik">
        <LogoRubik />
      </div>

      <div class="nav-item menu">
        <template v-if="this.$route.name === 'home'">
          <div
            :class="'menu-item FAQ black-text-button menu-item-faq-' + $i18n.locale"
            @click="move_to_anchor('FAQ')"
          >{{ $i18n.t('shared.nav_bar.FAQ') }}</div>
        </template>
        <template v-else>
          <div :class="'menu-item FAQ black-text-button menu-item-faq-' + $i18n.locale">
            <router-link
              :to="{ path: '/', query: { anchor: 'FAQ' } }"
              class="router_link"
            >{{ $i18n.t('shared.nav_bar.FAQ') }}</router-link>
          </div>
        </template>

        <template v-if="this.$route.name === 'install'">
          <div
            class="menu-item black-text-button"
            @click="move_to_anchor('server_buy')"
          >{{ $i18n.t('shared.nav_bar.server_buy') }}</div>
        </template>
        <template v-else>
          <div class="menu-item black-text-button">
            <router-link
              :to="{ path: '/install', query: { anchor: 'server_buy' } }"
              class="router_link"
            >{{ $i18n.t('shared.nav_bar.server_buy') }}</router-link>
          </div>
        </template>

        <template v-if="this.$route.name === 'install'">
          <div
            class="menu-item black-text-button"
            @click="move_to_anchor('server_install')"
          >{{ $i18n.t('shared.nav_bar.server_install') }}</div>
        </template>
        <template v-else>
          <div class="menu-item black-text-button">
            <router-link
              :to="{ path: '/install', query: { anchor: 'server_install' } }"
              class="router_link"
            >{{ $i18n.t('shared.nav_bar.server_install') }}</router-link>
          </div>
        </template>

        <div class="menu-item selector">
          <div class="selector-wrapper">
            <div
              :class="[selector.active ? 'chosen-active' : 'chosen-not-active', 'chosen']"
              @click="selector.active = !selector.active"
            >
              <p>
                {{
                  selector.selected.toUpperCase()
                }}
                <!-- + ' ' + selector.languages.find(obj => {
                  return obj.short === selector.selected
                }).long-->
              </p>
              <figure :class="[selector.active ? 'figure-active' : 'figure-not-active', 'figure']">
                <svg
                  width="12"
                  height="9"
                  viewBox="0 0 12 9"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="M6 9L11.1962 0H0.803848L6 9Z" fill="#747474" />
                </svg>
              </figure>
            </div>
            <div :class="[selector.active ? 'dropdown-active' : 'dropdown-not-active', 'dropdown']">
              <div
                v-for="language in languages"
                :key="language.id"
                class="option"
                @click="set_selected(language.short)"
              >{{ language.long }}</div>
            </div>
          </div>
        </div>

        <template v-if="this.$route.name === 'home'">
          <div
            :class="'menu-item menu-item-home black-text-button menu-item-faq-' + $i18n.locale"
            @click="move_to_anchor('FAQ')"
          >{{ $i18n.t('shared.nav_bar.FAQ') }}</div>
        </template>
        <template v-else>
          <div :class="'menu-item menu-item-home black-text-button menu-item-faq-' + $i18n.locale">
            <router-link
              :to="{ path: '/' }"
              class="router_link"
            >{{ $i18n.t('shared.nav_bar.home') }}</router-link>
          </div>
        </template>
      </div>
    </nav>
  </div>
</template>

<script>
import LogoRubik from '@/components/home/assets/LogoRubik.vue'

export default {
  data() {
    return {

      selector: {
        active: false,
        selected: this.$i18n.locale,
      }
    };
  },
  components: {
    LogoRubik
  },
  computed: {
    selected_user() {
      return this.selector.selected
    },
    languages() {
      let langs = [
        {
          short: "en",
          long: "English"
        }
      ]

      return langs
    }
  },
  mounted() {
    console.log(this.$i18n.locale)

    let locale = sessionStorage.getItem('locale');
    if (locale !== null && locale !== undefined) {
      this.set_selected(locale)
    }
  },
  methods: {
    set_selected(short_language) {
      this.selector.selected = short_language
      this.selector.active = false
      this.$i18n.locale = short_language
      sessionStorage.setItem('locale', short_language);
    },
    move_to_anchor(anchor) {
      this.$store.commit('move_to_anchor', anchor)
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.selector {
  &-wrapper {
    width: 120px;
    @include font-main($size: 14px);

    box-sizing: border-box;

    position: relative;
    top: 0;
    left: 0;
    height: 50px;

    z-index: 5;
    cursor: pointer;

    .chosen {
      @include font-main($size: 14px, $color: $color-white);
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      text-indent: 20px;

      p,
      .figure {
        height: 100%;
      }

      p {
        width: 50%;
        display: flex;
        flex-direction: row;
        align-items: center;
      }
      .figure {
        width: 10%;
        @include flex-center();

        &-not-active {
          transform: translateY(2px);
        }
        &-active {
          transform: rotate(180deg) translateY(0px);
        }
      }
    }

    .dropdown {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;

      &-not-active {
        display: none;
      }

      .option {
        background-color: #fff;
        &:hover {
          background-color: darken(#fff, 5%);
        }

        &:active {
          background-color: darken(#fff, 15%);
        }
      }

      @for $i from 0 through 5 {
        .option:nth-child(#{$i}) {
          position: absolute;

          $number: $i - 1;
          top: +20px + 49px * $number;

          left: 0;

          box-sizing: border-box;

          border: 1px solid #000;

          height: 50px;
          width: 100%;

          display: flex;
          flex-direction: row;
          justify-content: flex-start;
          align-items: center;
          text-indent: 20px;
        }
      }
    }
  }
}

.flex-navbar {
  box-sizing: border-box;

  background-color: $color-black;

  margin-left: 0;
  margin-right: 0;

  margin-top: 0px;
  margin-bottom: 0px;
}

.black-text-button {
  @include black-text-button;
}

@include media-width-split-big(800px) {
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .rubik {
      margin-left: 50px;
    }
    .nav-item {
      padding: 20px;
    }

    .nav-item::nth-child(1) {
    }
    .menu {
      margin-right: 50px;

      width: 100%;

      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-end;

      @include font-main($size: 14px, $color: $color-white);

      .menu-item {
        padding-left: 10px;
        padding-right: 10px;

        &-faq {
          &-en {
            flex-basis: 160px;
            min-width: 50px;
          }
          &-ru {
            flex-basis: 250px;
            min-width: 50px;
          }
        }

        &-home {
          display: none;
        }

        &:nth-child(-n + 3) {
          @include flex-center();
        }

        &:nth-child(2) {
          flex-basis: 200px;
          min-width: 50px;
        }
        &:nth-child(3) {
          flex-basis: 250px;
          min-width: 50px;
        }
        &:nth-child(4) {
          flex-basis: 150px;
          min-width: 50px;
        }
      }
    }
  }
}

@include media-width-split-small(800px) {
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;

    background-color: $color-black;

    .FAQ {
      display: flex;
      justify-content: center;
    }

    .rubik {
      @include flex-center();
      display: none;
    }
    .nav-item {
      padding: {
        top: 20px;
        bottom: 20px;
        left: 15px;
        right: 15px;
      }
      flex-basis: 100%;
      box-sizing: border-box;
    }

    .menu {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-around;


      flex-basis: 100%;

      @include font-main($size: 14px, $color: $color-white);

      .menu-item {
        @include flex-center();

        &:nth-child(1) {
          flex-basis: 100px;
          display: none;
        }
        &:nth-child(2) {
          flex-basis: 200px;
        }
        &:nth-child(3) {
          flex-basis: 100px;
        }
        &:nth-child(4) {
          flex-basis: 50px;
        }

        &-home {
          order: -1;
          flex-basis: 100px;
        }
      }
    }
  }
}
</style>