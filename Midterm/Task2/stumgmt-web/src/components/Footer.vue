<script setup>
import FastAPI from '@/assets/fastapi.svg'
</script>

<template>
    <footer class="footer">
        <span>由 </span><span class="vue">Vue.js</span><span> 和 </span><img :src="FastAPI" /><span>FastAPI 强力驱动</span>
    </footer>
</template>

<style scoped>
.footer {
    font-size: var(--fontSizeBase400);
    font-weight: var(--fontWeightSemibold);
    margin-top: var(--spacingVerticalL);
}
.footer img {
    height: 1.2em;
    width: 1.2em;
    vertical-align: middle;
}
</style>