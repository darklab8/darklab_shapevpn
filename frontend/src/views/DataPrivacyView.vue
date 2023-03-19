<template>
    <div class="min_heighter">
        <NavBar />

        <DataPrivacy />

        <BlackFooter />
    </div>
</template>

<script>
import NavBar from "@/components/shared/components/NavBar.vue";
import DataPrivacy from "@/components/extra/DataPrivacy.vue";
import BlackFooter from "../components/shared/components/BlackFooter.vue";


export default {
    name: 'PoliticsView',
    mounted() {
        window.scrollTo(0, 0);
        document.title = this.$store.state.brand + " - Data Privacy Agreement";
        document.querySelector('meta[name="description"]').setAttribute("content", "The page contains a description of information stored during ShapeVPN usage.");
    },
    components: {
        NavBar,
        DataPrivacy,
        BlackFooter
    },
    computed: {
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.min_heighter {
    min-height: 100vh;
    background-color: black;
}
</style>