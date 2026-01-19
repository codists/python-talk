<script setup>
// 获取后端传递过来的菜单栏

import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const route = useRoute()

const menus = ref([])

const activeIndex = computed(() => {
  const currentPath = route.path

  // 如果当前是根路径 '/'，则高亮 '/home'
  if (currentPath === '/') {
    return '/home'
  }

  return currentPath
})

const fetchMenus = async () => {
  try {
    const res = await axios.get('http://26.26.26.1:5000/api/menus/')
    const rawMenus = res.data

    // 过滤出一级菜单
    menus.value = rawMenus.filter((item) => item.parent_id === null)
  } catch (err) {
    console.error('获取菜单失败', err)
  }
}

const handleSelect = (index) => {
  console.log('menu selected:', index)
  activeIndex.value = index
  router.push(index)
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
    <img
      src="@/assets/images/python-logo@2x.png"
      class="python-logo"
    />
    <div class="flex-grow" />

    <el-menu-item
      v-for="menu in menus"
      :index="menu.url"
      v-bind:key="menu.id"
    >
      {{ menu.name }}
    </el-menu-item>
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
.el-menu--horizontal .el-menu-item.is-active {
  border-bottom: none !important;
}
</style>
