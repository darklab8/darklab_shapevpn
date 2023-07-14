<template>
  <BlackIntroField />

  <WhiteField />

  <BlackFooter />
  <footer></footer>
</template>

<script>
import BlackIntroField from "@/components/home/components/BlackIntroField.vue";
import WhiteField from "@/components/home/components/WhiteField.vue";
import BlackFooter from "../components/shared/components/BlackFooter.vue";


export default {
  name: 'HomeView',

  components: {
    BlackIntroField,
    WhiteField,
    BlackFooter
  },
  computed: {
  },
  mounted() {
    document.title = this.$store.state.brand + " - self-hosted VPN";
    document.querySelector('meta[name="description"]').setAttribute("content", "ShapeVPN provides WEB GUI to install Wireguard as a self-hosted VPN to Ubuntu 20.04 server.");
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";
</style>