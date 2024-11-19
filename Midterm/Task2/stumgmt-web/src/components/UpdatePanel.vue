<script setup>
import { ref, watchEffect} from 'vue'
import Button from '@cp/Button.vue'
import TextArea from '@cp/TextArea.vue'

const {student} = defineProps(['student'])
const emit = defineEmits(['after-update'])

const name = ref('')
const id = ref('')
const college = ref('')
const gpa = ref('')

function updateStudent(student) {
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
    const params = new URLSearchParams()
    params.append('student_id', student.id)
    for (const field of ['name', 'college', 'gpa']) {
      if (student[field] != '') {
        params.append(field, student[field])
      }
    }
  fetch(
    import.meta.env.VITE_API_BASE_URL + '/student/update?' + params.toString(), {
      method: 'PATCH',
    }
  ).then(resp => resp.json()).then(j => {
    if (j.code != 200) {
      alert(j.message)
    }
    emit('after-update')
  })
}

watchEffect(function () {
  if (student) {
  // 通过副作用实现，以避免破坏单向数据流
  id.value = student.id
  name.value = student.name
  college.value = student.college
  gpa.value = student.gpa
  }
})
</script>

<template>
  <div id="update-panel" v-if="student">
      <label>姓名：</label>
      <TextArea v-model="name" :placeholder="name"/>
      <label>学号：</label>
      <TextArea v-model="id" :placeholder="id"/>
      <label>学院：</label>
      <TextArea v-model="college" :placeholder="college"/>
      <label>绩点：</label>
      <TextArea v-model="gpa" :placeholder="gpa"/>
      <Button variant="primary" @click="updateStudent({name, id, college, gpa})">更新</Button>
  </div>
  <div id="update--panel" v-else>
    <p>请选择一个学生。</p>
  </div>
</template>


<style scoped>
#update-panel {
  margin: var(--spacingVerticalM) 0;
  display: grid;
  /*上次学的 grid*/
  grid-template-columns: 1fr 7fr;
  gap: var(--spacingHorizontalM);
  max-width: 414px;
  align-items: center
}

#update-panel * {
  font-size: var(--fontSizeBase400);
}

#update-panel span {
  display: flex;
  align-items: center;
}
</style>