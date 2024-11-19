<script setup>
import {ref, onMounted} from 'vue'

const props = defineProps({
    'query-by': {
        type: String,
        default: ''
    },
    'value': {
        type: String,
        default: ''
    },
    'order-by': {
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

onMounted(function () {
    loading.value = true
    fetch(import.meta.env.VITE_API_BASE_URL + '/students')
        .then(response => response.json())
        .then(data => {
            students.value = data.students
            loading.value = false
        })
})
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
                    <tr v-for="student in students" :key="student.id">
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
tr, td {
    font-family: var(--fontFamilyNumeric);
    height: var(--lineHeightBase400);

    vertical-align: middle;
    font-size: var(--fontSizeBase400);
}
</style>