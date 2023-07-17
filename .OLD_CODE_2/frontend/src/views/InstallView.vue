<template>
    <MainField />
    <footer></footer>
</template>

<script>
import MainField from "@/components/install/MainField.vue";

export default {
    name: 'InstallView',
    mounted() {
        window.scrollTo(0, 0);

        document.title = this.$store.state.brand + " - Install Wireguard to Ubuntu 20.04";
        document.querySelector('meta[name="description"]').setAttribute("content", "The page contains instructions on how to get a server and interface to install Wireguard to Ubuntu 20.04 server and client devices.");
    },
    components: {
        MainField
    },
    computed: {
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
</style>