<script setup>
import { ref } from 'vue'

import PioneerTitle from '@cp/PioneerTitle.vue'
import CRUDButtons from '@cp/CRUDButtons.vue'
import StudentList from '@cp/StudentList.vue'
import Footer from '@cp/Footer.vue'

import ReadPanel from '@cp/ReadPanel.vue'

const mode = ref('read')
const currentStudent = ref(null)

const queryProps = ref({
  queryBy: '',
  queryValue: '',
  orderBy: '',
  reverse: false
})

function setQuery(props) {
  if (props.queryValue == '') props.queryBy = ''
  if (props.queryBy == 'id') {
    if (isNaN(props.queryValue)) {
      alert('学号必须是数字！')
      return
    }
    else if (props.queryValue.length != 8) {
      alert('学号长度必须是8位！')
      return
    }
  }
  if (props.queryBy == 'gpa' && isNaN(props.queryValue)) {
    alert('绩点必须是数字！')
    return
  }
  for (const key in props) {
    queryProps.value[key] = props[key]
  }
}
</script>

<template>
  <PioneerTitle>先锋学生管理系统</PioneerTitle>
  <CRUDButtons @create="mode = 'create'" @read="mode = 'read'" @update="mode = 'update'" @delete="mode = 'delete'" />
  <ReadPanel v-if="mode === 'read'" @set-query="setQuery" />
  <StudentList :query_by="queryProps.queryBy" :value="queryProps.queryValue" :order_by="queryProps.orderBy"
    :reverse="queryProps.reverse" @set-current-student="currentStudent = $event" />
  <Footer />
</template>

<style scoped></style>
