<script setup>
// 获取后端传递过来的菜单栏

// 模拟数据
const menus = [
  {
    id: 1,
    path: "",
    name: "首页"
  },
  {
    id: 2,
    path: "login",
    name: "登录"
  },
  {
    id: 3,
    path: "register",
    name: "注册"
  },
]
import {ref} from 'vue'

const activeIndex = ref('1')
const handleSelect = () => {
  console.log('in header.vue')
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
      router
  >
    <img src="@/assets/images/python-logo@2x.png" class="python-logo">
    <div class="flex-grow"/>
    <el-menu-item v-for="menu in menus" :index="menu.path" v-bind:key="menu.id">{{ menu.name }}</el-menu-item>
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

</style>