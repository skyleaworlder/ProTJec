<template>
  <div style="padding: 30px">
    <el-backtop />
  <el-card :class="getColor(proInfo.sort)" style="min-width:600px; width: 50%; margin: 0 auto" class="pro-card-info">
    <div slot="header" style="font-size:40px">
      {{ proInfo.name }}
    </div>

    <div class="pro-info-avatar">
      <el-col :span="8" class="initiator">
        <span class="init-title">首倡者</span>
        <div><router-link :to="'/profile/'+proInfo.initiator[0].id">
          <span><img :src="proInfo.initiator[0].avatar" class="card-image"></span>
        </router-link></div>
      </el-col>
      <el-col :offset="2" :span="14" class="responders">
        <span class="resp-title">支持者</span>
        <div v-for="(resp,index) in proInfo.responder" :key="index">
          <span><router-link :to="'/profile/'+resp.id">
            <img :src="resp.avatar" class="card-image">
          </router-link></span>
        </div>
      </el-col>
    </div>

    <div class="pro-intro">
      <div class="pro-intro-title">
        <i class="el-icon-postcard" />
        <span style="padding-left:5px">项目介绍</span>
      </div>
      <div class="pro-intro-content">
        {{ proInfo.intro }}
      </div>
      <div class="pro-intro-content">
        <span v-for="tag in proInfo.tags" :key="tag.tag_id"><router-link :to="'/proshow/'+ tag.tag_id">
          <el-tag :type="getButtonColor(proInfo.sort)" style="margin-right:5px">
            {{ tag.tag_name }}</el-tag>
        </router-link></span>
      </div>
    </div>

    <div class="pro-need">
      <div class="pro-need-title">
        <svg-icon icon-class="peoples" />
        <span style="padding-left:5px">需求人数</span>
        <div style="text-align: center">
          <span style="font-size:80px">{{ proInfo.need }}</span>
          <span style="font-size:20px">waiting...</span>
        </div>
      </div>
    </div>

    <div class="pro-info-other">
      <el-col :span="12" class="pro-info-time">
        <div class="pro-time-title">
          <i class="el-icon-time" />
          <span style="padding-left:5px">时间相关</span>
        </div>
        <div class="pro-time-content">
          <el-timeline>
            <el-timeline-item :timestamp="proInfo.releaseTime">
              项目发布
            </el-timeline-item>
            <el-timeline-item :timestamp="proInfo.endTime">
              招募结束
            </el-timeline-item>
          </el-timeline>
        </div>
      </el-col>

      <el-col :offset="2" :span="10" class="pro-info-sort">
        <div class="pro-sort-title">
          <i class="el-icon-coin" />
          <span style="padding-left:5px">项目分类</span>
        </div>
        <div class="pro-sort-content">
          <div style="text-align:center;font-family:KaiTi;font-size:60px">{{ proInfo.sort }}</div>
        </div>
      </el-col>
    </div>

    <div class="join">
      <el-button :type="getButtonColor(proInfo.sort)" class="join-btn"
        @click="dialogVisible=true" :disabled="proInfo.need<=0">
        加入我们！
      </el-button>
    </div>
  </el-card>


  <el-dialog title="提示信息" :visible.sync="dialogVisible"
    width="30%">
    <span>我们是 {{ proInfo.name }} 项目组。<br> 您愿意加入我们吗？</span>
    <span slot="footer" class="dialog-footer">
      <el-button @click="joinPro()"
        :type="getButtonColor(proInfo.sort)">
        是的，我愿意！</el-button>
      <el-button @click="dialogVisible=false">
        还是再考虑下。</el-button>
    </span>
  </el-dialog>

  </div>
</template>

<script>
import '@/styles/proinfo.scss'
import { fetchProInfo } from '@/api/projects'
import { requestJoin } from '@/api/usrpro'
import { Message } from 'element-ui'

export default {
  data() {
    return {
      loading: false,
      dialogVisible: false,
      tmpavatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif?imageView2/1/w/80/h/80',
      proInfo: {
        name: '',
        initiator: {
          id: '0',
          no: '',
          name: '',
          inst: '',
          avatar: ''
        },
        tags: [],
        responder: [{id: '0'}],
        sort: '',
        releaseTime: '',
        endTime: '',
        need: '',
        intro: ''
      }
    }
  },

  created() {
    this.getInfo()
  },

  methods: {
    test() {
      console.log(this.proInfo.need);
      
    },
    validId(id) {
      for (let index = 0; index < this.proInfo.responder.length; index += 1) {
        if (this.proInfo.responder[index].id == id) {
          return false
        }
      }
      // initiator is array, perhaps in case of several initiators
      for (let index = 0; index < this.proInfo.initiator.length; index++) {
        if (id == this.proInfo.initiator[index].id) {
          return false
        }
      }
      return true
    },

    getInfo() {
      const id = this.$route.params.id
      fetchProInfo({ id }).then(response => {
        this.loading = true
        console.log(response);
        this.proInfo = response.data.data
      }, setTimeout(() => {
        this.loading = false
      }, 1.5 * 1000))
    },

    joinPro() {
      const usr_id = this.$store.state.user.id
      const pro_id = this.$route.params.id
      console.log(usr_id, pro_id, "user_id, pro_id");
      console.log(this.dialogVisible)
      if (this.validId(usr_id)) {
        this.loading = true
        requestJoin({ usr_id, pro_id }).then(response => {
          const { data } = response
          if (data.status === 'REQ_SUCCESS') {
            Message({type: 'success', message: '申请成功，请等待同意', duration: 1500})
          } else if (data.status === 'REQ_EXIST') {
            Message({type: 'warning', message: '申请正在审核，请不要再这么做', duration: 1500})
          }
          console.log(response, "join response")
          this.dialogVisible = false
          this.getInfo()
        }, setTimeout(() => {
          this.loading = false
        }, 1.5 * 1000))
      } else {
        Message({message: '您已经参与了这个项目！', type: 'error', duration: 1500})
        this.dialogVisible = false
      }
    },

    getColor(sort) {
      if (sort === '理工') {
        return 'blue-card'
      } else if (sort === '经管') {
        return 'yellow-card'
      } else if (sort === '文史' || sort === '社科') {
        return 'red-card'
      } else if (sort === '设计') {
        return 'green-card'
      } else {
        return 'green-card'
      }
    },
    getButtonColor(sort) {
      if (sort === '理工') {
        return 'primary'
      } else if (sort === '经管') {
        return 'warning'
      } else if (sort === '文史' || sort === '社科') {
        return 'danger'
      } else if (sort === '设计') {
        return 'success'
      } else {
        return 'success'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.pro-card {
  width: 50%;
  margin: 0 auto;
}
</style>