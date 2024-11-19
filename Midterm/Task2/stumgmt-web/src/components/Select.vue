<script setup>
const {modelValue} = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <select :value="modelValue" @change="emit('update:modelValue', $event.target.value)">
    <slot></slot>
  </select>
</template>

<style scoped>
select {
    -moz-box-align: center;
    align-items: center;
    box-sizing: border-box;
    display: inline-flex;
    -moz-box-pack: center;
    justify-content: center;
    text-decoration-line: none;
    vertical-align: middle;
    margin: 0px;
    overflow: hidden;
    border: var(--strokeWidthThin) solid;
    border-color: var(--colorNeutralStroke1);
    background-color: var(--colorNeutralBackground1);
    font-family: var(--fontFamilyBase);
    outline-style: none;
    padding: 5px var(--spacingHorizontalM);
    min-width: 96px;
    border-radius: var(--borderRadiusMedium);
    font-size: var(--fontSizeBase300);
    line-height: var(--lineHeightBase300);
    transition-duration: var(--durationFaster);
    transition-property: background-color, border-color, color;
    transition-timing-function: var(--curveEasyEase);
    height: 36px
}
</style>