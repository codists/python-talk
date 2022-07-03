<script setup>
import {ref} from 'vue'
import {reactive} from 'vue'

const labelPosition = ref('top')
const registerForm = reactive(
    {
      email: '',
      username: '',
      password: '',
      checkPass: ''
    }
)
const resetForm = () => {
  console.log('submit!')
}
</script>

<template>
    <div class="common-layout" >
    <el-container>
      <el-main>
        <h1>注册</h1>
        <el-form
            ref="ruleFormRef"
            :label-position="labelPosition"
            :model="registerForm"
            status-icon
            :rules="rules"
            label-width="120px"
            class="demo-ruleForm"
        >
          <el-form-item label="邮箱" prop="email" class="item">
            <el-input v-model.email="registerForm.age" placeholder="E-mail address"/>
          </el-form-item>
          <el-form-item label="用户名" prop="username">
            <el-input v-model.username="registerForm.age" placeholder="Username"/>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="registerForm.pass" type="password" autocomplete="off" placeholder="Password"/>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPass">
            <el-input
                v-model="registerForm.checkPass"
                type="password"
                autocomplete="off"
                placeholder="Password(again)"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="default" @click="resetForm()">提交 »</el-button>
          </el-form-item>
        </el-form>
      </el-main>

      <el-aside width="200px">
        <h2 class="widget-title">已有账号？</h2>
        <p>如果您已经帐户，请点击“登录”</p>
<!--        <el-button type="default" class="loginBtn">登录</el-button>-->
        <p>
          <a class="loginBtn">登录</a>
        </p>
      </el-aside>
    </el-container>
  </div>
</template>
<style scoped>
.el-main {
  margin-right: 10%;
}

/*文字基本设置*/
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

.widget-title {
  color: #999999;
  font-size: 1.5em;
  line-height: 1.5em;
}
p {
  color: #999999;
}
.loginBtn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  color: #4D4D4D;
  background-color: #CCCCCC;
  border-radius: 5px;
}

.loginBtn:hover {
  background-color: #d9d9d9;
}

.el-aside {
  border-top: 5px solid #e6e8ea;
  padding: 1.25em;
}
</style>