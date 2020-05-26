<template>
  <div class="app-main">
    <el-form ref="loginForm" class="login-form" :model="loginForm" :rules="loginRules">
      <!--<img alt="Vue logo" height="100px" src="../assets/logo.png">-->
      <div class="login-title">
        <h1>ProTJec</h1>
      </div>
      <el-form-item prop="no">
        <span>
          <i class="el-icon-user-solid" />
        </span>
        <el-input
          ref="no"
          v-model="loginForm.no"
          placeholder="用户名"
          name="no"
          :trigger-on-focus="false"
          clearable
        />
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="capsLock on" placement="right" manual>
        <el-form-item prop="password">
          <span>
            <i class="el-icon-notebook-2" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            placeholder="密码"
            :type="passwordType"
            :trigger-on-focus="false"
            name="password"
            show-password
            clearable
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleLogin"
          />
        </el-form-item>
      </el-tooltip>

      <el-row :gutter="15">
        <el-col :span="12">
          <el-button style="width:100%; height:45px" type="primary">
          注册</el-button>
        </el-col>
        <el-col :span="12">
          <el-button :loading="loading" style="width:100%; height:45px" type="primary" @click="handleLogin">
            登录</el-button>
        </el-col>
      </el-row>

      <div style="padding:20px 0 5px 0; color:#888; font-size:12px">
        ProTJec 化自 "Project"，意为属于 TJU 的项目平台<br />
      </div><div style="padding:0px; color:#888; font-size:12px">
        ProTJec 是一个组队平台，希望你可以轻松找到正确的人<br />
      </div>
        

      <div v-if="window_height>600"
        style="position:fixed ; bottom:10px; left:50%; margin-left:-100px; color:#888">
        Producted By Skyleaworlder
      </div>
    </el-form>
  </div>
</template>

<script>
import { validNo } from '@/utils/validate'
import SocialSign from './components/SocialSignin'
import { Message } from 'element-ui'

export default {
  name: 'Login',
  components: { SocialSign },
  data() {
    const validateNo = (rule, value, callback) => {
      if (!validNo(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        no: '1852409',
        password: '123456'
      },
      loginRules: {
        no: [{ required: true, trigger: 'blur', validator: validateNo }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      redirect: undefined,
      otherQuery: {},
      tel: '',
      window_height: window.innerHeight
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.no === '') {
      this.$refs.no.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    heightcalcu() {
      return window.innerHeight
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          console.log(this.loginForm)
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
              this.loading = false
            })
            .catch((error) => {
              this.loading = false
              Message.error(error || 'Has Error')
              // next(`/login?redirect=${to.path}`)
              // NProgress.done()
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    },
    sendCap() {
      console.log(this.$router)
      console.log(this.$route)
      console.log(this.$refs)
    }
    // afterQRScan() {
    //   if (e.key === 'x-admin-oauth-code') {
    //     const code = getQueryObject(e.newValue)
    //     const codeMap = {
    //       wechat: 'code',
    //       tencent: 'code'
    //     }
    //     const type = codeMap[this.auth_type]
    //     const codeName = code[type]
    //     if (codeName) {
    //       this.$store.dispatch('LoginByThirdparty', codeName).then(() => {
    //         this.$router.push({ path: this.redirect || '/' })
    //       })
    //     } else {
    //       alert('第三方登录失败')
    //     }
    //   }
    // }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#4e9f8e;
$bg2: #cbe2d2;
$dark_gray:#889aa4;
$light_gray:#eee;
$black: #000;
$form_width: 520px;
$cursor: #fff;

/*

*/

/* reset element-ui css */
.app-main {
  // 这里把所有的都变成居中了，艹没加scoped
  // text-align: center;
  color: #2c3e50;

  /* rewrite input in el-row for no and password */
  .login-form {
    .el-input {
      display: inline-block;
      height: 45px;
      width: 85%;

      input {
        background: transparent;
        border: none;
        -webkit-appearance: none;
        border-radius: none;
        padding: 12px 5px 12px 15px;
        color: $black;
        height: 45px;
        caret-color: $cursor;

        &:-webkit-autofill {
          box-shadow: 0 0 0px 1000px $bg inset !important;
          -webkit-text-fill-color: $cursor !important;
        }
      }
    }
  }
}
</style>

<style lang="scss" scoped>
$bg:#4e9f8e;
$bg2: #cbe2d2;
$dark_gray:#889aa4;
$light_gray:#eee;
$black: #000;
$form_width: 520px;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

.app-main {
  background-image: url('./assets/sakura.png');
  text-align: center;
  height: 100%;
  width: 100%;
  overflow: hidden;

  .login-form {
    position: relative;
    background-color: rgba(255, 255, 255, 0.6);
    width: $form_width;
    height: 100%;
    max-width: 100%;
    margin: 40px 20px;
    padding: 180px 30px 180px 30px;
    margin: 0 auto;
    overflow: hidden;
  }

  .el-row {
    .el-input {
      display: inline-block;
      height: 45%;
      width: 75%;
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }

}
</style>
