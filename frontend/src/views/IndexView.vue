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
.el-header {
  width: 100%;     
  margin: 0;      
  padding: 0;
}
.header {
  width: 100%;
  height: 42px;
  padding: 0;
}

.main {
  width: 100%;
  height: 860px;
  /*background-color: azure;*/
  margin: 0px auto;
}

.el-main {
  /* 取消布局里面main层的padding*/
  --el-main-padding: 0;
}
.el-footer {
  width: 100%;     
  margin: 0;      
  padding: 0;
}
</style>
