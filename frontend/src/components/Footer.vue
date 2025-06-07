<template>
  <div class="footer">
    <span class="left-item">
      Copyright ©PythonTalk from 2022
    </span>
    <a href="https://github.com/codists/python-talk" target="_blank" class="right-item">
      <img src="@/assets/images/GitHub-Mark-Light-32px.png" class="github-logo" alt="python-talk repository">
    </a>
  </div>
</template>

<style scoped>
.footer {
  width: 80%;
  height: 80px;
  background-color: #2b5b84;
  color: white;
  line-height: 80px;
  text-align: center;
  margin: 12px auto;
}

.left-item {
  display: inline-block;
  height: 100%;
  margin-right: 20px;
}

.right-item {
  display: inline-block;
  vertical-align: middle;
}

img {
  display: block;
}
</style>