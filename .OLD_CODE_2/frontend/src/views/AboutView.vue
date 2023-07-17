<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>

  <div class="hello_i18n">
    <HelloI18n />
  </div>
</template>

<script>
import HelloI18n from '@/components/examples/HelloI18n.vue'

export default {
  name: 'AboutView',
  components: {
    HelloI18n
  }
}
</script>