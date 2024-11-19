<script setup>
import { ref } from 'vue'
import Button from '@cp/Button.vue'
import TextArea from '@cp/TextArea.vue'

const emit = defineEmits(['after-create'])

const name = ref('')
const id = ref('')
const college = ref('')
const gpa = ref('')

function createStudent(student) {
  // validate
  if (student.name == '') {
    alert('姓名不能为空！')
    return
  }
  if (student.id.toString() !== parseInt(student.id).toString()) {
    alert('学号必须是 8 位数字！')
    return
  }
  if (student.college == '') {
    alert('学院不能为空！')
    return
  }
  if (student.gpa.toString() !== parseFloat(student.gpa).toString()) {
    alert('绩点必须是数字！')
    return
  }
  // create
  fetch(
    import.meta.env.VITE_API_BASE_URL + '/student/add', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(student)
    }
  ).then(resp => resp.json()).then(j => {
    if (j.code != 200) {
      alert(j.message)
    }
    emit('after-create')
  })
}
</script>

<template>
  <div id="create-panel">
      <label>姓名：</label>
      <TextArea v-model="name" placeholder="先锋鸡"/>
      <label>学号：</label>
      <TextArea v-model="id" placeholder="19230001"/>
      <label>学院：</label>
      <TextArea v-model="college" placeholder="计算机学院"/>
      <label>绩点：</label>
      <TextArea v-model="gpa" placeholder="5.0"/>
      <Button variant="primary" @click="createStudent({name, id, college, gpa})">添加</Button>
  </div>
</template>


<style scoped>
#create-panel {
  margin: var(--spacingVerticalM) 0;
  display: grid;
  /*上次学的 grid*/
  grid-template-columns: 1fr 7fr;
  gap: var(--spacingHorizontalM);
  max-width: 414px;
  align-items: center
}

#create-panel * {
  font-size: var(--fontSizeBase400);
}

#create-panel span {
  display: flex;
  align-items: center;
}
</style>