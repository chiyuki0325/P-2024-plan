<script setup>
import {ref} from 'vue'

import PioneerTitle from '@cp/PioneerTitle.vue'
import CRUDButtons from '@cp/CRUDButtons.vue'
import StudentList from '@cp/StudentList.vue'
import Footer from '@cp/Footer.vue'

import ReadPanel from '@cp/ReadPanel.vue'

const mode = ref('read')
const currentStudent = ref(null)
</script>

<template>
  <PioneerTitle>先锋学生管理系统</PioneerTitle>
  <CRUDButtons
    @create="mode.value = 'create'"
    @read="mode.value = 'read'"
    @update="mode.value = 'update'"
    @delete="mode.value = 'delete'"
  />
  <ReadPanel v-if="mode === 'read'" />
  <StudentList />
  <Footer />
</template>

<style scoped>
</style>
