import { createI18n } from "vue-i18n/index";
import * as Settings from '@/settings.js'
// /**
//  * Load locale messages
//  *
//  * The loaded `JSON` locale messages is pre-compiled by `@intlify/vue-i18n-loader`, which is integrated into `vue-cli-plugin-i18n`.
//  * See: https://github.com/intlify/vue-i18n-loader#rocket-i18n-resource-pre-compilation
//  */
function loadLocaleMessages() {
  const locales = require.context('./locales', true, /[A-Za-z0-9-_,\s]+\.json$/i)
  const messages = {}
  locales.keys().forEach(key => {
    const matched = key.match(/([A-Za-z0-9-_]+)\./i)
    if (matched && matched.length > 1) {
      const locale = matched[1]
      messages[locale] = locales(key).default
    }
  })
  return messages
}


export default createI18n({
    //   legacy: false,
    locale: Settings.LOCALE,
    fallbackLocale: Settings.FALLBACK_LOCALE,
    messages: loadLocaleMessages(),
      // fallbackWarn: false,
      //  missingWarn: false
  });




