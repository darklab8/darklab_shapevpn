<template>
    <section>
        <template v-if="client_download_state === 'windows'">
            <a :href="client_download_urls.windows">
                <div class="button">
                    <div
                        class="button-shell"
                    >{{ $i18n.t(`install.DownloadClientButton.download.windows`) }}</div>
                </div>
            </a>
        </template>
        <template v-if="client_download_state === 'macos'">
            <a :href="client_download_urls.macos">
                <div class="button">
                    <div
                        class="button-shell"
                    >{{ $i18n.t(`install.DownloadClientButton.download.macos`) }}</div>
                </div>
            </a>
        </template>
        <template v-if="client_download_state === 'ios'">
            <a :href="client_download_urls.ios">
                <div class="button">
                    <div
                        class="button-shell"
                    >{{ $i18n.t(`install.DownloadClientButton.download.ios`) }}</div>
                </div>
            </a>
        </template>
        <template v-if="client_download_state === 'android'">
            <a :href="client_download_urls.android">
                <div class="button">
                    <div
                        class="button-shell"
                    >{{ $i18n.t(`install.DownloadClientButton.download.android`) }}</div>
                </div>
            </a>
        </template>
        <template v-if="client_download_state === 'linux'">
            <div class="instruction" id="linux_instruction">
                <h1>{{ $i18n.t(`install.DownloadClientButton.download.linux.full_instruction_checked_in_ubuntu`) }}</h1>
                <ol>
                    <li>{{ $i18n.t(`install.DownloadClientButton.download.linux.install_client_for_chosen_distro`) }}
                        <div class="shell">
                            <div class="shell-instruction">apt install wireguard resolvconf -y</div>
                        </div>
                    </li>
                    <li>{{ $i18n.t(`install.DownloadClientButton.download.linux.put_downloaded_file_at_the_address_in_filesystem`) }} /etc/wireguard/wg0.conf</li>

                    <li>
                        {{ $i18n.t(`install.DownloadClientButton.download.linux.launch_daemon`) }}
                        <div class="shell">
                            <div class="shell-instruction">systemctl start wg-quick@wg0</div>
                        </div>
                    </li>
                    <li>
                        {{ $i18n.t(`install.DownloadClientButton.download.linux.make_an_autolaunch_during_user_startup`) }}
                        <div class="shell">
                            <div class="shell-instruction">systemctl enable wg-quick@wg0</div>
                        </div>
                    </li>
                </ol>
                <br />
                <h1>{{ $i18n.t(`install.DownloadClientButton.download.linux.instruction_for_other_distros`) }}:</h1>
            </div>
            <!-- Ubuntu
        Debian
        Fedora
        Mageia
        Arch
        OpenSUSE/SLE
        Alpine
        Gentoo
        NixOS
        RHEL 8
        CentOS 8
        RHEL 7
        CentOS 7
        FreeBSD
        Void
        EdgeOS
            AstLinux-->

            <div class="distro">
                <div class="distro-label">Debian</div>
                <div class="distro-instruction">$ sudo apt install wireguard</div>
            </div>
            <div class="distro">
                <div class="distro-label">Ubuntu</div>
                <div class="distro-instruction"># apt install wireguard</div>
            </div>
            <div class="distro">
                <div class="distro-label">Fedora</div>
                <div class="distro-instruction">$ sudo dnf install wireguard-tools</div>
            </div>
            <div class="distro">
                <div class="distro-label">Mageia</div>
                <div class="distro-instruction">$ sudo urpmi wireguard-tools</div>
            </div>
            <div class="distro">
                <div class="distro-label">Arch</div>
                <div class="distro-instruction">$ sudo pacman -S wireguard-tools</div>
            </div>
            <div class="distro">
                <div class="distro-label">OpenSUSE/SLE</div>
                <div class="distro-instruction">$ sudo zypper install wireguard-tools</div>
            </div>
            <div class="distro">
                <div class="distro-label">Alpine</div>
                <div class="distro-instruction"># apk add -U wireguard-tools</div>
            </div>
            <div class="distro">
                <div class="distro-label">Gentoo</div>
                <div class="distro-instruction"># emerge wireguard-tools</div>
            </div>
        </template>
    </section>
</template>

<script>
export default {
    components: {
    },
    computed: {
        client_download_state() {
            return this.$store.state.client_download_state
        },
        client_download_urls() {
            return this.$store.state.client_download_urls
        }
    },
    methods: {

    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.instruction {
    @include instruction();

    ol {
        padding-left: 0;
        margin-left: 0;
        text-indent: 0;
        list-style-position: inside;
    }
}

section {
    width: 100%;

    a {
        @include link-reset();
    }

    .button {
        @include flex-center();

        &-shell {
            box-sizing: border-box;
            width: 80%;
            max-width: 600px;
            height: 50px;

            background-color: $color-green;

            &:hover {
                background-color: darken($color-green, 10%);
            }

            &:active {
                background-color: darken($color-green, 20%);
            }

            @include font-main(
                $size: 15px,
                $height: 123%,
                $spacing: -0.02em,
                $color: $color-white
            );

            @include flex-center();
        }
    }

    .distro {
        @include instruction_string();
    }

    .shell {
        @include instruction_string();
        padding-left: 0;
        list-style-position: inside;
    }
}
</style>