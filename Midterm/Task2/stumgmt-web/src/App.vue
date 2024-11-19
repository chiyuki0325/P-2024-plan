<script setup>
import { ref } from 'vue'

import PioneerTitle from '@cp/PioneerTitle.vue'
import CRUDButtons from '@cp/CRUDButtons.vue'
import StudentList from '@cp/StudentList.vue'
import Footer from '@cp/Footer.vue'

import CreatePanel from '@cp/CreatePanel.vue'
import DeletePanel from '@cp/DeletePanel.vue'
import UpdatePanel from '@cp/UpdatePanel.vue'
import ReadPanel from '@cp/ReadPanel.vue'

const mode = ref('')
const currentStudent = ref(null)
const updateStudentList = ref(0)

const queryProps = ref({
  queryBy: '',
  queryValue: '',
  orderBy: '',
  reverse: false
})

function setQuery(props) {
  // validate
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
  // set
  for (const key in props) {
    queryProps.value[key] = props[key]
  }
}
</script>

<template>
  <PioneerTitle subtitle="要成为一个合格的牛马，首先 ...">先锋学生管理系统</PioneerTitle>
  <div class="side-by-side">
    <StudentList :query_by="queryProps.queryBy" :value="queryProps.queryValue" :order_by="queryProps.orderBy"
      :reverse="queryProps.reverse" @set-current-student="currentStudent = $event" :key="updateStudentList" />
    <div>
      <CRUDButtons @create="mode = 'create'" @read="mode = 'read'" @update="mode = 'update'"
        @delete="mode = 'delete'" />
      <CreatePanel v-if="mode === 'create'" @after-create="updateStudentList++" />
      <DeletePanel v-else-if="mode === 'delete'" :student="currentStudent" @after-delete="updateStudentList++" />
      <UpdatePanel v-else-if="mode === 'update'" :student="currentStudent" @after-update="updateStudentList++" />
      <ReadPanel v-else-if="mode === 'read'" @set-query="setQuery" />
      <p v-else>
        欢迎使用先锋学生管理系统！请选择一个功能。
      </p>
    </div>
  </div>
  <Footer />

</template>

<style scoped>
.side-by-side {
  display: flex;
  gap: var(--spacingHorizontalXXXL);
}
</style>
