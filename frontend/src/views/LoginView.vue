<template>
<h1>登录</h1>
  <el-form :model="form">
    <el-form-item>
      <el-input placeholder="请输入邮箱" v-model.email="form.email" />
    </el-form-item>
    <el-form-item>
      <el-input placeholder="请输入密码" v-model.password="form.password" />
    </el-form-item>

    <el-form-item>
      <el-button class="forgotPassword" type="default" @click="onForgotPassword"
        >忘记密码</el-button
      >
      <el-button type="default" @click="onLogin">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { reactive } from "vue";

const form = reactive({
  email: "",
  password: "",
});

const onLogin = () => {
  console.log(form);
};

const onForgotPassword = () => {};
</script>

<style scoped>
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
</style>