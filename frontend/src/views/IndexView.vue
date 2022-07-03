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
    </el-main>
      <Footer></Footer>
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
  background-color: azure;
  margin: 12px auto;
}
</style>
