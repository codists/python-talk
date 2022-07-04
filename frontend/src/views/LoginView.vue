<template>
<el-container>
  <el-main> <h1>登录</h1>
  <el-form :model="form" :labelPosition="labelPosition">
    <el-form-item label="登录" >
      <el-input placeholder="Username or Email" v-model.email="form.email"/>
    </el-form-item>
    <el-form-item label="密码">
      <el-input placeholder="Password" v-model.password="form.password"/>
    </el-form-item>

    <el-form-item label="Remember Me">
       <el-checkbox v-model="rememberMe" label="" size="large" />
    </el-form-item>

    <el-form-item>
      <el-button class="forgotPassword" type="default" @click="onForgotPassword">忘记密码</el-button>
      <el-button type="default" @click="onLogin">登录</el-button>
    </el-form-item>
  </el-form></el-main>

  <el-aside width="200px">
    <h2 class="widget-title">注册账号</h2>
    <p>如果您还没有账户，请点击“注册”</p>
    <p>
      <router-link class="registerBtn" to="/register">注册</router-link>
    </p>
  </el-aside>
</el-container>


</template>

<script setup>
import {ref} from 'vue'
import {reactive} from "vue";

const labelPosition = ref('top')

const form = reactive({
  email: '',
  password: '',
  rememberMe: ''
});

const onLogin = () => {
  console.log(form);
};

const onForgotPassword = () => {};
</script>

<style scoped>

.el-main {
  margin-right: 10%;
  margin-top: 12px;
}
h1 {
  color: #3776ab;
  font-family: SourceSansProBold, Arial, sans-serif;
  line-height: 1.75em;
  font-size: 1.75em;
  margin-bottom: 1em;
}


.el-button {
  color: #e6e8ea;
  background-color: #2b5b84;
  width: 88px;
  height: 40px;
}

.el-button:hover {
  background-color: #244e71;
}

.forgotPassword {
  color: #4d4d4d;
  background-color: #cccccc;
  border: none;
}

.forgotPassword:hover {
  color: #2d2d2d;
  background-color: #dedede;
}

.forgotPassword:active {
  opacity: 0.5;
  color: white;
  background-color: #0e0e0e;
}

.widget-title {
  color: #999999;
  font-size: 1.5em;
  line-height: 1.5em;
}

p {
  color: #999999;
}

.registerBtn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  color: #4D4D4D;
  background-color: #CCCCCC;
  border-radius: 5px;
  text-decoration: none;
}

.registerBtn:hover {
  background-color: #d9d9d9;
}

.el-aside {
  margin-top: 20px;
  border-top: 5px solid #e6e8ea;
  padding: 1.25em;
}
</style>