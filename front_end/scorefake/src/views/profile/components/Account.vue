<template>
  <el-form :rules="modRules" :model="user">
    <el-form-item label="学号">
      <el-input v-model.trim="user.no" :disabled="true" />
    </el-form-item>
    <el-form-item label="用户名" prop="name">
      <el-input ref="name" v-model.trim="user.name" />
    </el-form-item>
    <el-form-item label="所在学院" prop="inst">
      <el-select ref="inst" v-model.trim="user.inst">
        <el-option v-for="ins in instArr" :key="ins.key" :value="ins.key" :label="ins.key" />
      </el-select>
    </el-form-item>
    <el-form-item label="所在年级" prop="grade">
      <el-select ref="grade" v-model.trim="user.grade">
        <el-option v-for="grad in gradeOption" :key="grad" :value="grad" :label="grad" />
      </el-select>
    </el-form-item>
    <el-form-item label="个人简介" prop="document">
      <el-input ref="document" v-model.trim="user.document" />
    </el-form-item>
    <el-form-item label="联系方式" prop="chat">
      <el-input ref="chat" v-model.trim="user.chat"  />
    </el-form-item>
    <el-form-item label="头像地址" prop="avatar">
      <el-input ref="avatar" v-model.trim="user.avatar" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="update">提交更新</el-button>
      <el-button v-if="false" @click="test">sad</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { updateUsrInfo } from '@/api/user'
import { Message } from 'element-ui'
export default {
  data() {
    return {
      instArr: [
        {key: '医学院'},{key: '口腔医学院'},{key: '生命科学与技术学院'},{key: '数学科学学院'},{key: '海洋与地球科学学院'},
        {key: '化学科学与工程学院'},{key: '航空航天与力学学院'},{key: '中德工程学院'},{key: '中德学院'},{key: '物理科学与工程学院'},
        {key: '经济与管理学院'},{key: '交通运输工程学院'},{key: '测绘与地理信息学院'},{key: '机械与能源工程学院'},{key: '建筑与城市规划学院'},
        {key: '汽车学院'},{key: '土木工程学院'},{key: '中法工程和管理学院'},{key: '马克思主义学院'},{key: '人文学院'},
        {key: '设计创意学院'},{key: '外国语学院'},{key: '法学院'},{key: '铁道与城市轨道交通研究院'},{key: '电子与信息工程学院'},
        {key: '艺术与传媒学院'},{key: '政治与国际关系学院'},{key: '软件学院'},{key: '材料科学与工程学院'},{key: '环境科学与工程学院'},
      ],
      modRules: {
        name: [{ required: true, trigger: 'change', message: '用户名不能为空' }],
        avatar: [{ required: true, trigger: 'change', message: '头像不能为空' }],
        inst: [{ required: true, trigger: 'change', message: '请选择正确的学院' }],
        grade: [{ type: 'number', required: true, trigger: 'change', message: '请选择正确的年级' }],
        document: [{ required: true, trigger: 'change', message: '个人简介不能为空' }],
        chat: [{ required: true, trigger: 'change', message: '联系方式不能为空' }]
      },
      tmpUserInfo: {
        name: '',
        no: '',
        avatar: '',
        inst: '',
        grade: '',
        document: '',
        chat: ''
      },
      gradeOption: [2020,2019,2018,2017,2016,2015,2014,2013]
    }
  },
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name: '',
          no: '',
          avatar: '',
          inst: '',
          grade: '',
          document: '',
          chat: ''
        }
      }
    }
  },
  methods: {
    test() {
      console.log(this.$props.user.name);
      const date = new Date()
      console.log(date.getFullYear())
      console.log(this.gradeOption, this.$store.state.user, this.$props.user, this.tmpUserInfo, "tmpinf")
    },
    update() {
      const usr_id = this.$store.state.user.id
      this.tmpUserInfo = this.user
      this.tmpUserInfo["id"] = usr_id
      console.log(this.tmpUserInfo);
      updateUsrInfo(this.tmpUserInfo).then(response => {
        if (response.data.status == 'INFO_SUCCESS') {
          this.tmpUserInfo = response.data.data
          Message({
            message: '修改个人信息成功！',
            type: 'success',
            duration: 1500
          })
          this.$store.dispatch('user/refreshInfo', this.tmpUserInfo.no)
        } else {
          Message({
            message: '修改个人信息出错！',
            type: 'error',
            duration: 1500
          })
        }
      })
    }
  }
}
</script>


<style lang="scss" scoped>
.el-form {
  padding: 30px;
}
</style>