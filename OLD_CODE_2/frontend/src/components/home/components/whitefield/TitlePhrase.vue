<template>
  <div class="what_you_receive_phrase">
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  props: {
    msg: String
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.what_you_receive_phrase {
  @include font-main($size: 30px, $height: 125.5%, $weight: 500);

  text-align: center;
}
</style>