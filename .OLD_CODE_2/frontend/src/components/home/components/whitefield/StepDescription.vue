<template>
  <p v-html="msg"></p>
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

p {
  @include font-main($size: 16px, $height: 125.5%, $spacing: 0.05em);

  margin-top: 0;
  margin-bottom: 0;

  @include margin-auto();
  padding: 4px;
}
</style>