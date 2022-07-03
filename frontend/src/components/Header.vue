<script setup>
// 获取后端传递过来的菜单栏

// 模拟数据
const menus = [
  {
    "id": "1",
    "name": "首页"
  },
  {
    "id": "2",
    "name": "登录"
  },
  {
    "id": "3",
    "name": "注册"
  },
]
import {ref} from 'vue'

const activeIndex = ref('1')
const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      text-color="#999999"
      active-text-color="#ffffff"
      background-color="1f2a32"
      :ellipsis="false"
      @select="handleSelect"
  >
    <img src="@/assets/images/python-logo@2x.png" class="python-logo">
    <div class="flex-grow"/>
    <el-menu-item v-for="menu in menus" :index="menu.id" v-bind:key="menu.id">{{ menu.name }}</el-menu-item>
  </el-menu>

</template>

<style scoped>
.el-menu-demo {
  background-color: #273643;
}

.python-logo {
  width: 217px;
  height: 61px;
}

.flex-grow {
  flex-grow: 1;
}

.el-menu-item {
  width: 121px;
}
.el-menu-item:not(.is-disabled):hover {
  outline: 0;
  background-color: #1f2a32;
}
</style>