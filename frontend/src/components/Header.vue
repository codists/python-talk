
<script setup>
// 获取后端传递过来的菜单栏

import { ref, onMounted } from 'vue'
import axios from 'axios'

const menus = ref([])

const activeIndex = ref('/home')


const fetchMenus = async () => {
  try {
    const res = await axios.get('http://26.26.26.1:5000/api/menus/')
    const rawMenus = res.data


    menus.value = rawMenus.filter(item => item.parent_id === null)
  } catch (err) {
    console.error('获取菜单失败', err)
  }
}

const handleSelect = (index) => {
  console.log('menu selected:', index)
}

onMounted(() => {
  fetchMenus()
})
</script>

<!-- 菜单栏 -->
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