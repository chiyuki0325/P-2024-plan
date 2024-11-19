<script setup>
const {modelValue, placeholder} = defineProps(['modelValue', 'placeholder'])
const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <span class="fluent-textarea-outer">
    <textarea
        class="fluent-textarea"
        :placeholder="placeholder"
        :value="modelValue"
        @input="emit('update:modelValue', $event.target.value)"
    >
        <slot></slot>
    </textarea>
  </span>
</template>

<style scoped>
.fluent-textarea-outer {
    border-top-color: var(--colorNeutralStroke1);
    border-left-color: var(--colorNeutralStroke1);
    border-right-color: var(--colorNeutralStroke1);
    border-style: solid;
    border-width: var(--strokeWidthThin);
    margin: 0px;
    padding: 0 0 var(--strokeWidthThick) 0;
    position: relative;
    box-sizing: border-box;
    display: inline-flex;
    border-radius: var(--borderRadiusMedium);
    background-color: var(--colorNeutralBackground1);
}
.fluent-textarea-outer:focus-within::after {
    transform: scaleX(1);
  }
.fluent-textarea-outer::after {
    transition-property: transform;
    transform: scaleX(0);
    clip-path: inset(calc(100% - var(--strokeWidthThick)) 0 0 0);
    transition-duration: var(--durationUltraFast);
    transition-delay: var(--curveAccelerateMid);

    border-bottom: var(--strokeWidthThick) solid var(--colorCompoundBrandStroke);
    border-radius: var(--borderRadiusMedium);
    height: max(var(--strokeWidthThick), var(--borderRadiusMedium));
    left: -1px;
    right: -1px;
    bottom: -1px;
    position: absolute;
    content: "";
    box-sizing: border-box;
}

.fluent-textarea {
    resize: none;
    padding-bottom: var(--spacingVerticalSNudge);
    padding-left: calc(
    var(--spacingHorizontalMNudge) + var(--spacingHorizontalXXS)
    );
    padding-right: calc(
    var(--spacingHorizontalMNudge) + var(--spacingHorizontalXXS)
    );
    padding-top: var(--spacingVerticalSNudge);
    outline-style: none;
    max-height: 100%;
    margin-bottom: 0px;
    height: 32px;
    background-color: transparent;
    margin-right: 0px;
    margin-left: 0px;
    box-sizing: border-box;
    -moz-box-flex: 1;
    flex-grow: 1;
    border-bottom-style: none;
    border-left-style: none;
    border-right-style: none;
    border-top-style: none;
    line-height: var(--lineHeightBase300);
    font-weight: var(--fontWeightRegular);
    font-size: var(--fontSizeBase300);
    font-family: var(--fontFamilyBase);
    color: var(--colorNeutralForeground1);
}
</style>