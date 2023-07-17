<template>
    <div class="provider_choice" id="server_buy_choice">
        <section class="buttons">
            <div class="flexed-provider-buttons">
                <div
                    :style="button_active"
                    :class="[selected_provider == 'vultr' ? 'button-active' : 'button-not-active', 'button']"
                    @click="visit_link(referral_link.vultr)"
                >
                    <div class="logo">
                        <LogoVultrVue />
                    </div>
                </div>
            </div>

            <div class="provider-becoming-available-buttons" v-if="selected_provider == 'vultr'">
                <div
                    class="action-button action-button-green-active"
                    @click="visit_link(referral_link.vultr)"
                >{{ $i18n.t(`install.InstructionProviderChoice.go_to_provider_X`, { provider: 'Vultr' }) }}</div>
            </div>
            <div
                class="provider-becoming-available-buttons"
                v-else-if="selected_provider == 'linode'"
            >
                <div
                    class="action-button action-button-green-active"
                    @click="visit_link(referral_link.linode)"
                >{{ $i18n.t(`install.InstructionProviderChoice.go_to_provider_X`, { provider: 'Linode' }) }}</div>
            </div>
        </section>
    </div>
</template>
<script>
import LogoVultrVue from "../assets/LogoVultr.vue";


export default {
    components: {
        LogoVultrVue,
    },
    computed: {
        selected_provider() {
            return this.$store.state.selected_provider
        },
        referral_link() {
            return this.$store.state.referral_link
        },
    },
    methods: {
        set_selected_provider(new_provider) {
            this.$store.commit('set_selected_provider', new_provider)
        },
        visit_link(url) {
            window.open(url, '_blank');
        }
    }
}
</script>
<style lang="scss" scoped>
@import "@/assets/_style.scss";

.provider_choice {
    width: 100%;

    section.buttons {
        width: 100%;
        .flexed-provider-buttons {
            @include provider-buttons();
        }

        .provider-becoming-available-buttons {
            @include provider-becoming-available-buttons();
        }
    }
}
</style>