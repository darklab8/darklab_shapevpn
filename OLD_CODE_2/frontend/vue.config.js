const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({

  publicPath: '/', // process.env.VUE_APP_ROOT || '/',

  transpileDependencies: true,

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableLegacy: false,
      runtimeOnly: false,
      compositionOnly: false,
      fullInstall: true
    }
  }
})
