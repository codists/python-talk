<script setup>
import {ref} from 'vue'
import {reactive} from 'vue'

const labelPosition = ref('top')

const submitForm = async (formEl) => {
  if (!formEl) return
  await formEl.validate((valid) => {
    if (valid) {
     return true
    } else {
      return false
    }
  })
}
const ruleFormRef = ref()
const registerForm = reactive({
      email: '',
      username: '',
      password: '',
      checkPass: ''
    }
)
const rules = reactive({
  email: [
    {required: true, message: '请输入邮箱', trigger: 'blur'},
    {type: 'email', message: '邮箱格式错误', trigger: ['blur', 'change']}
  ],
  username: [
    {required: true, message: '请输入用户名', trigger: 'blur'},
  ],
  password: [
    {required: true, message: '请输入密码', trigger: 'blur'},
  ],
  checkPass: [
    {required: true, message: '请再次输入密码', trigger: 'blur'},
  ]
})


</script>

<template>
  <div class="common-layout">
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
            <el-input v-model.email="registerForm.email" placeholder="E-mail address"/>
          </el-form-item>
          <el-form-item label="用户名" prop="username">
            <el-input v-model.username="registerForm.username" placeholder="Username"/>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="registerForm.password" type="password" autocomplete="off" placeholder="Password"/>
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
            <el-button type="default" @click="submitForm(ruleFormRef)">提交 »</el-button>
          </el-form-item>
        </el-form>
      </el-main>

      <el-aside width="200px">
        <h2 class="widget-title">已有账号？</h2>
        <p>如果您已经帐户，请点击“登录”</p>
        <p>
          <router-link class="loginBtn" to="/login">登录</router-link>
        </p>
      </el-aside>
    </el-container>
  </div>
</template>
<style scoped>
.el-main {
  margin-right: 10%;
  margin-top: 12px;
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
  text-decoration: none;
}

.loginBtn:hover {
  background-color: #d9d9d9;
}

.el-aside {
  margin-top: 20px;
  border-top: 5px solid #e6e8ea;
  padding: 1.25em;
}
</style>