<script setup>
import Button from '@cp/Button.vue'

const {student} = defineProps(['student'])

const emit = defineEmits(['after-delete'])

function deleteStudent() {
  // validate
  if (!student?.id) return
  // delete
  fetch(
    import.meta.env.VITE_API_BASE_URL + '/student/remove?student_id=' + String(student.id), {
      method: 'DELETE',
    }
  ).then(resp => resp.json()).then(j => {
    if (j.code != 200) {
      alert(j.message)
    }
    emit('after-delete')
  })
}
</script>

<template>
  <div id="delete-panel" v-if="student">
      <p>姓名：{{ student.name }}</p>
      <p>学号: {{ student.id }}</p>
      <p>学院: {{ student.college }}</p>
      <p>绩点: {{ student.gpa }}</p>
      <Button variant="primary" @click="deleteStudent">删除</Button>
  </div>
  <div id="delete-panel" v-else>
    <p>请选择一个学生。</p>
  </div>
</template>


<style scoped>
#delete-panel {
  margin: var(--spacingVerticalM) 0;
  max-width: 414px;
}

#delete-panel * {
  font-size: var(--fontSizeBase400);
}

</style>