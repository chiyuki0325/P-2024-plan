<script setup>
import { ref } from 'vue'
import Button from '@cp/Button.vue'
import TextArea from '@cp/TextArea.vue'
import Select from '@cp/Select.vue'
const emit = defineEmits(['set-query'])

const queryBy = ref('')
const queryValue = ref('')
const orderBy = ref('')
const reverse = ref(true)
</script>

<template>
  <div id="read-panel">
    <Select v-model="queryBy">
      <option value="">请选择查询条件</option>
      <option value="name">姓名</option>
      <option value="id">学号</option>
      <option value="college">学院</option>
      <option value="gpa">绩点</option>
    </Select>
    <TextArea placeholder="查询值" v-model="queryValue" />
    <Select v-model="orderBy">
      <option value="">请选择排序条件</option>
      <option value="name">姓名</option>
      <option value="id">学号</option>
      <option value="college">学院</option>
      <option value="gpa">绩点</option>
    </Select>
    <span>
      <input type="checkbox" v-model="reverse" />
      <label>倒序</label>
    </span>
    <Button variant="primary" @click="emit('set-query', { queryBy, queryValue, orderBy, reverse })">查询</Button>
  </div>
</template>


<style scoped>
#read-panel {
  margin: var(--spacingVerticalM) 0;
  display: grid;
  /*上次学的 grid*/
  grid-template-columns: 1fr 2fr;
  gap: var(--spacingHorizontalM);
  max-width: 600px;
}

#read-panel * {
  font-size: var(--fontSizeBase400);
}

#read-panel span {
  display: flex;
  align-items: center;
}

input[type="checkbox"] {
  width: 24px;
  height: 24px;

}
</style>