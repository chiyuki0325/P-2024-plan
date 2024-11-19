<script setup>
import { ref, watchEffect } from 'vue'

const props = defineProps({
  'query_by': {
    type: String,
    default: ''
  },
  'value': {
    type: String,
    default: ''
  },
  'order_by': {
    type: String,
    default: ''
  },
  'reverse': {
    type: Boolean,
    default: false
  },
})

const loading = ref(false)
const students = ref([])
/*
id integer
name string
college string
gpa number
*/

const emit = defineEmits(['set-current-student'])

watchEffect(function () {
  loading.value = true

  const params = new URLSearchParams()
  for (const key in props) {
    if (props[key] !== '') {
      params.append(key, props[key])
    }
  }

  fetch(
    import.meta.env.VITE_API_BASE_URL + '/students?' + params.toString(), {
    method: 'GET',
  }
  )
    .then(response => response.json())
    .then(data => {
      students.value = data.students
      loading.value = false
    })
})

const currentId = ref(null)

function setCurrentStudent(student) {
  currentId.value = student.id
  emit('set-current-student', student)
}
</script>

<template>
  <div class="student-list">
    <div v-if="loading">加载中...</div>
    <div v-else-if="students.length === 0">暂无数据！</div>
    <div v-else>
      <table>
        <thead>
          <tr>
            <th>学号</th>
            <th>姓名</th>
            <th>学院</th>
            <th>绩点</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.id" @click="setCurrentStudent(student)"
            :class="{ 'selected': student.id === currentId }">
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.college }}</td>
            <td>{{ student.gpa }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
tr,
td {
  font-family: var(--fontFamilyNumeric);
  height: var(--lineHeightBase400);

  vertical-align: middle;
  font-size: var(--fontSizeBase400);

}

tr.selected {
  font-weight: var(--fontWeightSemibold);
}

thead {
  margin-bottom: var(--spacingVerticalL);
}
</style>