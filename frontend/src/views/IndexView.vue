<script setup>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
</script>

<template>
  <el-container>
    <el-header class="header">
      <Header/>
    </el-header>
    <el-main class="main">
      <router-view></router-view>
    </el-main>
    <el-footer>
      <Footer/>
    </el-footer>
  </el-container>
</template>

<style>
.header {
  width: 80%;
  height: 42px;
  padding: 0;
  margin: 48px auto 12px;
}

.main {
  width: 80%;
  height: 860px;
  /*background-color: azure;*/
  margin: 25px auto;
}

.el-main {
  /* 取消布局里面main层的padding*/
  --el-main-padding: 0;
}
.el-footer {
  margin-bottom: 48px;
}
</style>
