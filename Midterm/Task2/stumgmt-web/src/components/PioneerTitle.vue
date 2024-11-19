<script setup>
import Chicken from '@/assets/pioneer-chicken.png'
</script>

<template>
    <h1 class="pioneer-title">
        <img class="pioneer-chicken" :src="Chicken" alt="Pioneer Chicken" />
        <slot></slot>
    </h1>
</template>

<style scoped>
.pioneer-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: var(--fontSizeHero800);
    font-weight: var(--fontWeightBold);
}

.pioneer-chicken {
    transition: transform 0.5s var(--curveEasyEase);
    width: 48px;
    height: 48px;
    border-radius: 50%;
}

.pioneer-chicken:hover {
    transform: scale(1.1) rotate(360deg);
}
</style>