<script setup>
import Button from '@cp/Button.vue'
const emit = defineEmits(['create', 'read', 'update', 'delete'])
</script>

<template>
  <div class="crud-buttons">
    <Button @click="emit('create')">增</Button>
    <Button @click="emit('delete')">删</Button>
    <Button @click="emit('update')">改</Button>
    <Button @click="emit('read')">查</Button>
  </div>
</template>

<style scoped>
.crud-buttons {
    display: flex;
    gap: 10px;
}
</style>