<script setup>
import Header from '@/components/Header'
</script>

<template>
  <el-container>
    <el-header class="header">
      <!--      <div class="nav clearfix">-->
      <!--        <div class="left clearfix">-->
      <!--          <div class="logo">-->
      <!--            <img src="@/assets/Python_logo_and_wordmark.svg" alt="lgoo" height="42">-->
      <!--          </div>-->
      <!--          <div class="index"><a href="#">首页</a></div>-->
      <!--        </div>-->

      <!--        <div class="right">-->
      <!--          <ul class="clearfix">-->
      <!--            <li><a href="#">登录</a></li>-->
      <!--            <li><a href="#">注册</a></li>-->
      <!--          </ul>-->
      <!--        </div>-->
      <!--      </div>-->
      <Header/>
    </el-header>
    <el-main class="main">
    </el-main>
    <el-footer class="footer">
      <span>Copyright ©2001-2022.  Github</span>
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

.nav {
  background-color: #273643;
  color: white;
  line-height: 42px;
  height: 42px;
}

.clearfix::after {
  content: '';
  display: table;
  clear: both;
}

.flex-grow {
  flex-grow: 1;
}

.nav .left, .nav .left div {
  float: left;
}

.nav .left .index a {
  display: block;
  color: white;
  text-decoration: none;
  width: 100%;
  padding-left: 55px;
  padding-right: 55px;
}

.nav .right {
  float: right;
}

.nav .right ul li {
  float: left;
  list-style: none;
}

.nav .right ul li a {
  text-align: center;
  color: white;
  text-decoration: none;
  display: block;
  width: 133px;
}

.main {
  width: 80%;
  height: 860px;
  background-color: azure;
  margin: 12px auto;
}

.footer {
  width: 80%;
  height: 80px;
  background-color: #2B5B84;
  color: white;
  line-height: 80px;
  text-align: center;
  margin: 12px auto;
}
</style>

<script setup>
</script>