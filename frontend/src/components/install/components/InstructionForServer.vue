<template>
    <div class="instruction" id="server_buy_instruction">
        <template v-if="selected_provider === 'vultr'">
            <div class="block registration">
                <div
                    class="registration-inside block-inside space-between-first-level-li unordered-signs"
                >
                    <h1>{{ $i18n.t(`${tc}.registration.registration_in_X`, { provider: 'Vultr' }) }}</h1>

                    <ol>
                        <li>
                            {{ $i18n.t(`${tc}.registration.go_to_site_and_press.goto`) }}
                            <span
                                class="link"
                                @click="visit_link(referral_link.vultr)"
                            >{{ $i18n.t(`${tc}.registration.go_to_site_and_press.site`) }}</span>
                            {{ $i18n.t(`${tc}.registration.go_to_site_and_press.and_press_the_button`) }}
                            <ol>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.depending_on_size_of_the_screen`) }}</li>
                            </ol>
                        </li>
                        <li>
                            {{ $i18n.t(`${tc}.registration.vultr.in_form_account_create_insert_email`) }}
                            <ol>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.note_password_must_contain_at_least`) }}</li>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.if_necessary_pass_captcha`) }}</li>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.when_the_form_is_completed`) }}</li>
                            </ol>
                        </li>
                        <li>
                            {{ $i18n.t(`${tc}.registration.vultr.in_billing_section`) }}
                            <ol>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.possible_to_use_payment_cards`) }}</li>
                                <li>{{ $i18n.t(`${tc}.registration.vultr.also_possible_to_use`) }}</li>
                            </ol>
                        </li>
                        <li>{{ $i18n.t(`${tc}.registration.vultr.possible_verification_in_tech_support_is_required`) }}</li>
                    </ol>
                </div>
            </div>

            <div class="block server_buying">
                <div class="server_buying-inside block-inside">
                    <h1>{{ $i18n.t(`${tc}.server_buying.server_buying_in_X`, { provider: 'Vultr' }) }}</h1>

                    <ol>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_cloud_compute`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_desired_loc`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_ubuntu`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_tarif`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_ssh_keys`) }}</li>
                        <div class="code">
                            <div class="code-label">ssh pub key</div>
                            <div class="code-instruction">
                                <div class="code-instruction-inside">{{ ssh_key_pub }}</div>
                            </div>
                        </div>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.choose_server_name`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.press_deploy`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.wait_for_completion`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.vultr.copy_ip`) }}</li>
                    </ol>
                </div>
            </div>
        </template>
        <template v-else-if="selected_provider === 'linode'">
            <div class="block registration">
                <div
                    class="registration-inside block-inside space-between-first-level-li unordered-signs"
                >
                    <h1>{{ $i18n.t(`${tc}.registration.registration_in_X`, { provider: 'Linode' }) }}</h1>

                    <ol>
                        <li>
                            {{ $i18n.t(`${tc}.registration.go_to_site_and_press.goto`) }}
                            <span
                                class="link"
                                @click="visit_link(referral_link.linode)"
                            >{{ $i18n.t(`${tc}.registration.go_to_site_and_press.site`) }}</span>
                            {{ $i18n.t(`${tc}.registration.linode.press_sign_up`) }}
                            <ol>
                                <li>{{ $i18n.t(`${tc}.registration.linode.depending_on_the_screen_size`) }}</li>
                            </ol>
                        </li>
                        <li>
                            {{ $i18n.t(`${tc}.registration.linode.insert_account_details`) }}
                            <ol>
                                <li>{{ $i18n.t(`${tc}.registration.linode.email_and_new_password`) }}</li>
                                <li>{{ $i18n.t(`${tc}.registration.linode.or_use_oauth`) }}</li>
                            </ol>
                        </li>
                        <li>{{ $i18n.t(`${tc}.registration.linode.go_to_link_in_email`) }}</li>
                        <li>{{ $i18n.t(`${tc}.registration.linode.insert_payment_details`) }}</li>
                    </ol>
                </div>
            </div>
            <div class="block server_buying">
                <div class="server_buying-inside block-inside">
                    <h1>{{ $i18n.t(`${tc}.server_buying.server_buying_in_X`, { provider: 'Linode' }) }}</h1>

                    <ol>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.press_create`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.choose_distro`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.choose_location`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.choose_tarif`) }}</li>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.choose_password`) }}</li>
                        <li>
                            {{ $i18n.t(`${tc}.server_buying.linode.choose_ssh_keys`) }}:
                            <div class="code">
                                <div class="code-label">ssh pub key</div>
                                <div class="code-instruction">
                                    <div class="code-instruction-inside">{{ ssh_key_pub }}</div>
                                </div>
                            </div>
                        </li>
                        <li>{{ $i18n.t(`${tc}.server_buying.linode.wait_to_complete`) }}</li>
                    </ol>
                </div>
            </div>
        </template>

        <!-- Shared instruction -->
        <div class="block server_install">
            <div
                class="server_install-inside sub-numbered-lists block-inside space-between-first-level-li"
            >
                <h1>{{ $i18n.t(`${tc}.vpn_installation.title`) }}</h1>

                <ol>
                    <li>{{ $i18n.t(`${tc}.vpn_installation.return_to_page_with_server_install`, { 'server_installation': $i18n.t(`shared.nav_bar.server_install`) }) }}</li>
                    <li
                        v-html="$i18n.t(`${tc}.vpn_installation.choose_I_have_server`, { 'i_have_a_server': $i18n.t(`install.intro.i_have_server.title`) })"
                    ></li>
                    <li>
                        {{ $i18n.t(`${tc}.vpn_installation.in_section_to_insert_data`, { 'install_VPN_on_server': $i18n.t(`install.MainField.to_install_VPN_to_server`) }) }}
                        <ol>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.choose_SSH`) }}</li>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.insert_copied_IP`) }}</li>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.leave_login_as_default_root`) }}</li>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.press_submit`, { 'submit': $i18n.t(`install.InputServerForm.install_vpn_to_server`) }) }}</li>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.wait_for_installation`) }}</li>
                        </ol>
                    </li>
                    <li>{{ $i18n.t(`${tc}.vpn_installation.in_section_to_download_configs_do_it`, { 'download_configs': $i18n.t(`install.MainField.download_config_files`) }) }}</li>
                    <li>
                        {{ $i18n.t(`${tc}.vpn_installation.in_section_to_download_client_app`) }}
                        <ol>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.choose_device_type`) }}</li>
                            <li>{{ $i18n.t(`${tc}.vpn_installation.apply_configs_to_client`) }}</li>
                        </ol>
                    </li>
                </ol>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    data() {
        return {
            tc: "install.InstructionForServer"
        }
    },
    components: {
    },
    computed: {
        selected_provider() {
            return this.$store.state.selected_provider
        },
        ssh_key_pub() {
            return this.$store.state.keys.public
        },
        referral_link() {
            return this.$store.state.referral_link
        },
    },
    methods: {
        visit_link(url) {
            window.location.href = url;
        }
    },
    async mounted() {
        
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.instruction {
    @include instruction();
}
</style>