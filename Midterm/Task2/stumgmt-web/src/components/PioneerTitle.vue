<script setup>
import Chicken from '@/assets/pioneer-chicken.png'
const {subtitle} = defineProps(['subtitle'])
</script>

<template>
    <div class="pioneer-title">
        <img class="pioneer-chicken" :src="Chicken" alt="Pioneer Chicken" />
        <div>
        <h1><slot></slot></h1>
        <span>{{subtitle}}</span>
        </div>
    </div>
</template>

<style scoped>
.pioneer-title {
    display: flex;
    align-items: center;
    gap: 10px;
    height: 100px;
    margin-bottom: var(--spacingVerticalL);
}
.pioneer-title h1 {
    font-size: var(--fontSizeHero800);
    font-weight: var(--fontWeightBold);
    margin: 0px;
}
.pioneer-title span {
    color: var(--colorNeutralForeground4);
}

.pioneer-chicken {
    transition: transform 0.5s var(--curveEasyEase);
    width: 72px;
    height: 72px;
    border-radius: 50%;
}

.pioneer-chicken:hover {
    transform: scale(1.1) rotate(360deg);
}
</style>