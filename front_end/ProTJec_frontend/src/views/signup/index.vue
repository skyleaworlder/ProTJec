<template>
  <div class="app-main">
    <el-form ref="signupForm" class="signup-form" :model="signupForm" :rules="loginRules">
      <!--<img alt="Vue logo" height="100px" src="../assets/logo.png">-->
      <div class="login-title">
        <h1>ProTJec</h1>
      </div>
      <el-form-item prop="no">
        <span>
          <i class="el-icon-user-solid" />
        </span>
        <el-input ref="no" v-model="signupForm.no"
          placeholder="学号" name="no"
          :trigger-on-focus="false" clearable/>
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="capsLock on" placement="right" manual>
        <el-form-item prop="password">
          <span><i class="el-icon-notebook-2" /></span>
          <el-input :key="passwordType" ref="password" v-model="signupForm.password"
            placeholder="密码"
            :type="passwordType" :trigger-on-focus="false"
            name="password"
            show-password clearable
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false" />
        </el-form-item>
      </el-tooltip>
      <el-form-item prop="validPwd">
        <span><i class="el-icon-notebook-2" /></span>
        <el-input :key="passwordType" ref="validPwd" v-model="signupForm.validPwd"
          placeholder="确认密码"
          :type="passwordType" :trigger-on-focus="false"
          name="validPwd"
          show-password clearable />
      </el-form-item>

      <el-form-item prop="usr_name">
        <span><i class="el-icon-user" /></span>
        <el-input ref="usr_name" v-model="signupForm.usr_name"
          placeholder="用户名"
          clearable />
      </el-form-item>

      <el-row :gutter="15">
        <el-col :span="13">
          <el-form-item prop="usr_inst">
            <span><i class="el-icon-notebook-2" /></span>
            <el-select ref="inst" v-model.trim="signupForm.usr_inst">
              <el-option v-for="ins in instArr" :key="ins.key" :value="ins.key" :label="ins.key" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-button style="width:100%; height:45px" type="primary"
            @click="resetSignup">
            重置</el-button>
        </el-col>
      </el-row>

      <el-row :gutter="15">
        <el-col :span="13">
          <el-form-item prop="usr_grade">
            <span><i class="el-icon-notebook-2" /></span>
            <el-select ref="grade" v-model.trim="signupForm.usr_grade">
              <el-option v-for="grad in gradeOption" :key="grad" :value="grad" :label="grad" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-button :loading="loading" style="width:100%; height:45px" type="primary" @click="handleLogin">
            注册</el-button>
        </el-col>
      </el-row>

      <div style="padding:0px 0 5px 0; color:#888; font-size:12px">
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
import { signup } from '@/api/user'
import { Message } from 'element-ui'
import { validNo, validateUsrName, validateUsrInst, validateUsrGrade } from '@/utils/validate'

const instArr = [
  {key: '医学院'},{key: '口腔医学院'},{key: '生命科学与技术学院'},{key: '数学科学学院'},{key: '海洋与地球科学学院'},
  {key: '化学科学与工程学院'},{key: '航空航天与力学学院'},{key: '中德工程学院'},{key: '中德学院'},{key: '物理科学与工程学院'},
  {key: '经济与管理学院'},{key: '交通运输工程学院'},{key: '测绘与地理信息学院'},{key: '机械与能源工程学院'},{key: '建筑与城市规划学院'},
  {key: '汽车学院'},{key: '土木工程学院'},{key: '中法工程和管理学院'},{key: '马克思主义学院'},{key: '人文学院'},
  {key: '设计创意学院'},{key: '外国语学院'},{key: '法学院'},{key: '铁道与城市轨道交通研究院'},{key: '电子与信息工程学院'},
  {key: '艺术与传媒学院'},{key: '政治与国际关系学院'},{key: '软件学院'},{key: '材料科学与工程学院'},{key: '环境科学与工程学院'},
]
const gradeOption = [2020,2019,2018,2017,2016,2015,2014,2013]

export default {
  name: 'Signup',
  data() {
    const validateNo = (rule, value, callback) => {
      if (!validNo(value)) {
        callback(new Error('学号不合乎规范'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码必须大于 6 位'))
      } else {
        callback()
      }
    }
    const validateValidPwd = (rule, value, callback) => {
      console.log(value, this.signupForm.password);
      
      if (value.length < 6 || this.signupForm.password != value) {
        callback(new Error('密码不符合规范'))
      } else {
        callback()
      }
    }
    return {
      instArr,
      gradeOption,
      signupForm: {
        no: '',
        password: '',
        validPwd: '',
        usr_name: '',
        usr_inst: '',
        usr_grade: ''
      },
      loginRules: {
        no: [{ required: true, trigger: 'blur', validator: validateNo }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }],
        validPwd: [{ required: true, trigger: 'blur', validator: validateValidPwd }],
        usr_name: [{ required: true, trigger: 'blur', validator: validateUsrName }],
        usr_inst: [{ required: true, trigger: 'blur', validator: validateUsrInst }],
        usr_grade: [{ required: true, trigger: 'blur', validator: validateUsrGrade }],
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
    if (this.signupForm.no === '') {
      this.$refs.no.focus()
    } else if (this.signupForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    resetSignup() {
      this.signupForm = {
        no: '',
        password: '',
        validPwd: '',
        usr_name: '',
        usr_inst: '',
        usr_grade: ''
      }
    },
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
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
      this.$refs.signupForm.validate(valid => {
        if (valid) {
          const data = {
            no: this.signupForm.no,
            pwd: this.signupForm.password,
            name: this.signupForm.usr_name,
            inst: this.signupForm.usr_inst,
            grade: this.signupForm.usr_grade
          }
          signup(data).then(response => {
            console.log(response, "signup");
            const { data, status } = response.data
            if (status == 'SET_SUCCESS') {
              Message({ type:"success", message:"注册成功", duration:1500 })
              this.resetSignup()
              this.$router.push({ path: '/login' })
            } else {
              Message({ type:"error", message:"注册失败", duration:1500 })
            }
          }).catch(err => {
            Message({ type:"info", message:err, duration:1500 })
          })
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
    }
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
  .signup-form {
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

  input::-webkit-input-placeholder {
    color: #777;
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
  .signup-form {
    position: relative;
    background-color: rgba(255, 255, 255, 0.6);
    width: $form_width;
    height: 100%;
    max-width: 100%;
    margin: 40px 20px;
    padding: 80px 30px 180px 30px;
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
