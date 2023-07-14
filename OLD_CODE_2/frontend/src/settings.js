export const API = process.env.VUE_APP_BACKEND_URL || 'http://localhost:8000';

export const LOCALE = process.env.VUE_APP_I18N_LOCALE || 'en';
export const FALLBACK_LOCALE = process.env.VUE_APP_I18N_FALLBACK_LOCALE || 'en';

export const URL_VULTR_INSTRUCTION_BUYING_SERVER = process.env.VUE_APP_URL_VULTR_INSTRUCTION_BUYING_SERVER || '/vultr_instruction.mp4';