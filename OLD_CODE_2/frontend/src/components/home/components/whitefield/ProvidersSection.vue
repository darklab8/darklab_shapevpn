<template>
    <div class="provider_choice">
        <section class="buttons">
            <div class="flexed-provider-buttons">
                <div
                    :class="[selected_provider == 'vultr' ? 'button-active' : 'button-not-active', 'button']"
                    @click="visit_link(referral_link.vultr)"
                    :style="button_active"
                >
                    <div class="logo">
                        <LogoVultrVue />
                    </div>
                </div>
            </div>
        </section>
    </div>

    <div class="action-buttons" v-if="selected_provider == 'vultr'">
        <div
            class="action-button action-button-green-active"
            @click="visit_link(referral_link.vultr)"
        >{{ $i18n.t('home.white_field.provider_section.buttons.to_go_to_vultr') }}</div>

        <router-link
            :to="{ path: '/install', query: { anchor: 'instruction', provider: 'vultr' } }"
            class="router_link action-button action-button-green-active"
        >
            <div
                class
            >{{ $i18n.t('home.white_field.provider_section.buttons.to_look_instruction') }}</div>
        </router-link>
    </div>
    <div class="action-buttons" v-else-if="selected_provider == 'linode'">
        <div
            class="action-button action-button-green-active"
            @click="visit_link(referral_link.linode)"
        >{{ $i18n.t('home.white_field.provider_section.buttons.to_go_to_linode') }}</div>

        <router-link
            :to="{ path: '/install', query: { anchor: 'instruction', provider: 'linode' } }"
            class="router_link action-button action-button-green-active"
        >
            <div
                class
            >{{ $i18n.t('home.white_field.provider_section.buttons.to_look_instruction') }}</div>
        </router-link>
    </div>
    <div class="action-buttons" v-else-if="selected_provider == 'none'">
        <div
            class="action-button action-button-not-active"
        >{{ $i18n.t('home.white_field.provider_section.buttons.to_go_to_provider') }}</div>
        <div
            class="action-button action-button-not-active"
        >{{ $i18n.t('home.white_field.provider_section.buttons.to_look_instruction') }}</div>
    </div>
</template>
<script>
import LogoVultrVue from "@/components/install/assets/LogoVultr.vue";

export default {
    data() {
        return {
            selected_provider: 'vultr'
        }
    },
    components: {
        LogoVultrVue,
    },
    computed: {
        button_active: function() {

        return {
          'background-image': 'url("/check_mark.svg")',
      }
      },
        referral_link() {
            return this.$store.state.referral_link
        },
    },
    methods: {
        SetVultr() {
            if (this.selected_provider == 'vultr') {
                this.selected_provider = 'none'
            } else {
                this.selected_provider = 'vultr'
            }
        },
        SetLinode() {
            if (this.selected_provider == 'linode') {
                this.selected_provider = 'none'
            } else {
                this.selected_provider = 'linode'
            }
        },
        visit_link(url) {
            window.open(url, '_blank');

        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

h3 {
    @include flex-center();
}

.provider_choice {
    @include margin-auto();

    section.buttons {
        @include margin-auto();

        .flexed-provider-buttons {
            @include provider-buttons();
        }
    }
}

.container-wrapper {
    width: 100%;
    margin-top: 80px;
    margin-bottom: 40px;

    background: #f3f3f3;

    section {
        margin-top: 66px;
        margin-bottom: 50px;
    }

    .languages_and_payments {
        @include margin-auto();
        @include languages_and_payments();
    }
}

.action-buttons {
    @include margin-auto();

    padding: {
        left: 20px;
        right: 20px;
    }

    padding-top: 15px;
    padding-bottom: 15px;

    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;

    width: 100%;

    .action-button {
        @include action-button();
    }

    .action-button-green-active {
        @include action-button-green-active();
    }

    .action-button-not-active {
        @include action-button-not-active();
    }

    .action-button-gray-active {
        @include action-button-gray-active();
    }
}
</style>