<template>
    <div class="video">
        <video id="video1" controls>
            <source :src="URL_VULTR_INSTRUCTION_BUYING_SERVER" type="video/mp4" />
        </video>
        <div
            :class="[video_is_not_launched ? '' : 'button-hidden', 'button-play']"
            @click="playVideo"
        >
            <PlayButton />
        </div>
        <div :class="[video_is_not_launched ? '' : 'background-hidden', 'background']"></div>
    </div>
</template>

<script>
import { URL_VULTR_INSTRUCTION_BUYING_SERVER } from '@/settings.js'
import PlayButton from "../assets/PlayButton.vue"

export default {
    data() {
        return {
            video_is_not_launched: true,
        };
    },
    components: {
        PlayButton,
    },
    computed: {
        selected_provider() {
            return this.$store.state.selected_provider
        },
        URL_VULTR_INSTRUCTION_BUYING_SERVER() {
            return URL_VULTR_INSTRUCTION_BUYING_SERVER
        }
    },
    methods: {
        playVideo() {
            var myVideo = document.getElementById("video1");

            if (myVideo.paused)
                myVideo.play();
            else
                myVideo.pause();

            this.video_is_not_launched = false;
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

h1 {
    margin-bottom: 60px;
}

.video {
    width: 100%;

    position: relative;
    max-height: 900px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);

    #video1 {
        width: 100%;
    }

    .button-play {
        cursor: pointer;
        position: absolute;

        border-radius: 50%;

        top: calc(50% - 135px / 2);
        left: calc(50% - 140px / 2);

        box-sizing: border-box;

        z-index: 2;
        opacity: 0.7;
        transition: {
            property: transform;
            duration: 2s;
            timing-function: easy-out;
        }
    }

    .button-hidden {
        transform: scale(0);
    }

    .background {
        background-color: rgba(0, 0, 0, 0.6);
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        position: absolute;

        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 1;
        transition: {
            property: opacity transform;
            duration: 2s 0s;
            timing-function: easy-out;
        }
    }
    .background-hidden {
        opacity: 0;
        transform: scale(0);
    }
}
</style>