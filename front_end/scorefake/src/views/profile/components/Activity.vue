<template>
  <div class="user-activity">
    <div class="pro-zone" v-if="myProjects">
      <el-col :gutter="20" :offset="0">
        <el-col v-for="elem in myProjects" :key="elem.name"
          :xs="12" :sm="12" :lg="8">
          <req-card
            :id="elem.id"
            :name="elem.name"
            :sort="elem.sort"
            :need="elem.need"
            :callback="getRequest" />
        </el-col>
      </el-col>
      <el-row v-if="myProjects.length==0">
        <div class="none-req">
          暂时没有项目，
          <router-link :to="'/'"><span style="color:blue;">
            点我看看吧！</span></router-link>
        </div>
      </el-row>
    </div>
    <div class="req-zone" v-if="requests">
      <el-row v-for="res in requests" :key="res.id">
        <req-post
          :responder="res"
          :pro_id="chosenProId"
          @flush="getAllProInfoIInit"
          @reqflush="getRequest" />
      </el-row>
      <el-row v-if="requests.length==0">
        <div class="none-req" v-if="chosenProName" >
          项目 {{ chosenProName }} 暂时没有申请</div>
        <div class="none-req" v-else>
          请点击 项目卡片 的 “查看申请” 键</div>
      </el-row>
    </div>
    <div v-else>
      sd
    </div>
  </div>
</template>

<script>
import ReqCard from './ReqCard'
import ReqPost from './ReqPost'
import { Message } from 'element-ui'
import { fetchProjects, fetchRequestUsers } from '@/api/projects'
const avatarPrefix = '?imageView2/1/w/80/h/80'
const carouselPrefix = '?imageView2/2/h/440'

export default {
  name: 'Activity',
  components: { ReqCard, ReqPost },
  data() {
    return {
      carouselImages: [
        'https://wpimg.wallstcn.com/9679ffb0-9e0b-4451-9916-e21992218054.jpg',
        'https://wpimg.wallstcn.com/bcce3734-0837-4b9f-9261-351ef384f75a.jpg',
        'https://wpimg.wallstcn.com/d1d7b033-d75e-4cd6-ae39-fcd5f1c0a7c5.jpg',
        'https://wpimg.wallstcn.com/50530061-851b-4ca5-9dc5-2fead928a939.jpg'
      ],
      avatarPrefix,
      carouselPrefix,
      select: {
        limit: 4,
        page: 1
      },
      myProjects: [],
      requests: [],
      chosenProId: undefined,
      chosenProName: undefined
    }
  },
  created() {
    this.getAllProInfoIInit()
  },
  methods: {
    getAllProInfoIInit() {
      const data = {
        limit: this.select.limit,
        page: this.select.page,
        initiatorId: this.$route.params.id
      }
      fetchProjects(data).then(response => {
        const { data } = response
        if (data.status == 'GET_SUCCESS') {
          this.myProjects = data.data.projects
        } else if (data.status == 'PROJ_UNEXIST') {
          this.myProjects = []
        }
        console.log(response, this.myProjects, "mypro");
      })
    },

    getRequest(pro_id, pro_name) {
      const data = {
        pro_id: pro_id
      }
      this.chosenProId = pro_id
      this.chosenProName = pro_name
      fetchRequestUsers(data).then(response => {
        const { data } = response
        if (data.status === 'GET_SUCCESS') {
          this.requests = data.data
        } else {
          this.requests = []
        }
        console.log(this.requests);
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.user-activity {
  .pro-zone {
    overflow: hidden;
    padding: 0 0 40px 0;
    border-bottom: 1px solid #d2d6de;
  }
  .user-block {

    .username,
    .description {
      display: block;
      margin-left: 50px;
      padding: 2px 0;
    }

    .username{
      font-size: 16px;
      color: #000;
    }

    :after {
      clear: both;
    }

    .img-circle {
      border-radius: 50%;
      width: 40px;
      height: 40px;
      float: left;
    }

    span {
      font-weight: 500;
      font-size: 12px;
    }
  }

  .post {
    font-size: 14px;
    border-bottom: 1px solid #d2d6de;
    margin: 15px 0 15px 0;
    padding: 15px 0 15px 0;
    color: #666;

    .image {
      width: 100%;
      height: 100%;

    }

    .user-images {
      padding-top: 20px;
    }
  }

  .list-inline {
    padding-left: 0;
    margin-left: -5px;
    list-style: none;

    li {
      display: inline-block;
      padding-right: 5px;
      padding-left: 5px;
      font-size: 13px;
    }

    .link-black {

      &:hover,
      &:focus {
        color: #999;
      }
    }
  }

  .none-req {
    width:500px;
    text-align:center;
    margin:0 auto;
    padding: 40px;
    color:#666;
    font-size: 15px;
  }
}

.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}
</style>
