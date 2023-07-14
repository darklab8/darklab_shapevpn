<template>
  <router-link to="/install" class="router_link">
    <div class="button-create-vpn">
      <p>
        {{
          $i18n.t('home.button_create.start')
        }}
      </p>
    </div>
  </router-link>
</template>

<style lang="scss" scoped>
@import "@/assets/_style.scss";

.button-create-vpn {
  @include font-main(
    $weight: 300,
    $size: 14px,
    $height: 123%,
    $spacing: 0.04em,
    $color: $color-white
  );

  text-transform: uppercase;

  width: 240px;
  height: $button-create-vpn-height;

  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  box-sizing: border-box;
  border-radius: 3px;

  &:not(:hover) {
    border: 1px solid $color-white;
  }

  &:hover {
    background-color: darken($color-green, 10%);
    border: 1px solid darken($color-green, 10%);
  }

  &:active {
    background-color: darken($color-green, 20%);
    border: 1px solid darken($color-green, 20%);
  }
}
</style>