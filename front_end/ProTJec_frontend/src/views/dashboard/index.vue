<template>
  <div class="dash-container">
    <el-backtop />

    <el-row class="search-container">
      <el-col :span="18" :offset="4">
        <el-form :inline="true" :model="projectsQuery">
          <el-form-item label="项目类型" prop="sort">
            <el-select v-model="projectsQuery.sort" ref="sort"
              size="small" placeholder="请选择项目种类" >
              <el-option v-for="type in proTypes" :key="type.key" :label="type.displayName" :value="type.key" />
            </el-select>
          </el-form-item>

          <el-form-item label="项目tag" prop="tagId">
            <el-select v-model="projectsQuery.tagId" ref="tagId"
              size="small" placeholder="请选择tag" >
              <el-option v-for="type in tags" :key="type.id" :label="type.name" :value="type.id" />
            </el-select>
          </el-form-item>

          <el-form-item label="项目状态" prop="state">
            <el-select v-model="projectsQuery.state" ref="state"
              size="small" placeholder="请选择项目状态" >
              <el-option v-for="type in proState" :key="type.key" :label="type.displayName" :value="type.key" />
            </el-select>
          </el-form-item>
            
          <el-button type="primary" size="small"
            @click="startSelect">
            一键搜索</el-button>
        </el-form>

      </el-col>
    </el-row>

    <!-- 表格 div/main/contain/header|table-->
    <el-row>
      <el-col :span="10" :offset="4" style="width:min-content">
        <div v-if="projects.length!=0">
          <el-row v-for="elem in projects" :key="elem.name"
            style="overflow:hidden">
          <!-- min-content make el-row width suitable -->
            <pro-card
              :id="elem.id"
              :name="elem.name"
              :sort="elem.sort"
              :release-time="elem.releaseTime"
              :need="elem.need"
              :intro="elem.intro"
            />
          </el-row>
        </div>
        <div v-else>
          <el-col class="null-res">
            搜索结果为空
          </el-col>
        </div>
        <el-pagination v-if="proTotal!=0" :page-size="projectsQuery.limit" :current-page.sync="projectsQuery.page" :total="proTotal"
          style="padding:20px" layout="prev, pager, next, jumper"
          @current-change="pageChange" />
      </el-col>


      <el-col :offset="1" :span="6" class="adv-container">
        <el-row v-for="link in links" :key="link.url" style="padding-top:20px">
          <el-card :body-style="{ padding:0 }">
            <img :src="link.pic" style="display:block; width:400px; height:200px">
            <div style="padding:15px">
              <div style="padding-bottom:10px">{{ link.title }}</div>
              <span style="font-size:14px;color:#999">
                {{ link.subtitle }}
              </span><span style="float:right">
                <a :href="link.url" style="color: blue">{{ link.click }}</a>
              </span>
            </div>
          </el-card>
        </el-row>
      </el-col>


    </el-row>

    <github-corner />
  </div>
</template>

<script>

import ProCard from './component/ProCard'
import GithubCorner from '@/components/GithubCorner'
import { fetchProjects } from '@/api/projects'
import { fetchAllTags } from '@/api/tags'
import '@/styles/dashboard.scss'

const proTypes = [
  { key: undefined, displayName: '不选择种类' },
  { key: '理工', displayName: '理工' },
  { key: '社科', displayName: '社科' },
  { key: '文史', displayName: '文史' },
  { key: '经管', displayName: '经管' },
  { key: '设计', displayName: '设计' },
  { key: '其他', displayName: '其他' }
]

const proState = [
  { key: 0, displayName: '正在招募' },
  { key: 1, displayName: '正在审核' },
  { key: 2, displayName: '审核失败' },
  { key: 3, displayName: '归档项目' }
]

export default {
  name: 'Dashboard',
  components: { ProCard, GithubCorner },
  data() {
    return {
      proTypes,
      proState,
      projects: '',
      projectsLoading: false,
      projectsQuery: {
        limit: 10,
        page: 1,
        state: 0,
        tagId: undefined,
        sort: undefined
      },
      proTotal: 0,
      tags: [],

      links: [
        {
          pic: require('./assets/jiying0.png'),
          title: '不去大名鼎鼎的 CXCY 看看吗？',
          subtitle:'快去 cxcy 和 Ta 绑在一起',
          url: 'http://cxcy.tongji.edu.cn',
          click: '点我！'
        },
        {
          pic: require('./assets/jiying1.png'),
          title: '同心云已死，OfCourse 当立！',
          subtitle: '开发 3 个月的软工级论坛',
          url: 'https://www.baidu.com',
          click: '没公测呢'
        },
        {
          pic: require('./assets/jiying2.jpg'),
          title: '逛累了，回寝室吧',
          subtitle: '同济大学图书馆入口',
          url: 'http://www.lib.tongji.edu.cn',
          click: '休息一下'
        }
      ]
    }
  },

  // 这段代码不是我写的，网上cv到的
  // ???????wsm????/
  // 我忘了这段代码一开始是用来解决什么问题的了，但是现在用它会给我带来错误，我又是不知道为什么
  // 这次的错误是，在dashboard 和 profile 之间切换，在profile切换到dashboard后，vuex中的数据全部消失
  created() {
    /*
    // 在页面加载时读取sessionStorage
    console.log('created begin')

    if (sessionStorage.getItem('store')) {
      this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(sessionStorage.getItem('store'))))
    }
    // 在页面刷新时将store保存到sessionStorage里
    window.addEventListener('beforeunload', () => {
      sessionStorage.setItem('store', JSON.stringify(this.$store.state))
    })
    console.log('created end', this.projects)
    */
  },

  mounted() {
    /* fix router-default-params failed
    if (typeof(this.$route.params.tagId) != "undefined") {
      this.projectsQuery.tagId = this.$route.params.tagId
    } else if (!this.$route.params.tagId) {
      this.$route.params.tagId = undefined
    }
    console.log(this.projectsQuery, this.$route);
    */
    
    this.initProjects()
    console.log(this.projects, 'mounted')
  },

  methods: {
    initProjects() {
      // 下面这句话出了问题，里面的actions在控制台报错，由于是异步，所以还调了好久
      // 其实不是actions里面的问题，而是request把status的判定从 200 设成了 get_success
      /*
      this.$store.dispatch('projects/setProjects', this.projectsQuery)
      console.log(this.projects, "this.pro");
      this.projects = this.$store.state.projects.projects
      console.log(this.projects, "this.pro");
      */
      this.projectsLoading = true
      fetchProjects(this.projectsQuery).then(response => {
        console.log(response, 'respon')

        const { status, data } = response.data
        if (status === 'GET_SUCCESS') {
          this.projects = data.projects
          this.proTotal = data.total
        } else {
        }
      })
      fetchAllTags().then(response => {
        const { status, data } = response.data
        if (status === 'GET_SUCCESS') {
          this.tags.push({id: undefined, name: "不选择tag"})
          this.tags.push(...data.tags)
        } else {
        }
      },setTimeout(() => {
        this.projectsLoading = false
      }, 1.5 * 1000))
    },
    pageChange(newPage) {
      console.log(newPage,"newpage");
      this.initProjects()
    },

    startSelect() {
      this.projectsLoading = true
      fetchProjects(this.projectsQuery).then(response => {
        const { status, data } = response.data
        console.log(response, "select");
        
        if (status === 'GET_SUCCESS') {
          this.projects = data.projects
          this.proTotal = data.total
        } else if (status == 'PROJ_UNEXIST') {
          this.projects = []
          this.proTotal = 0
        }
      },setTimeout(() => {
        this.projectsLoading = false
      }, 1.5 * 1000))
    }
  }
}
</script>

<style lang="scss">
$container_bg: rgba(240, 242, 245, 1);
$table_title:#026d49;
$sidebar_bg: #ddf0e6;
$table_title_bg: #ddf0e6;
</style>

<style lang="scss" scoped>

.adv-container {
  @media screen and (max-width: 1200px) {
    display: none;
  }
}

.null-res {
  margin:0 auto;
  text-align:center;
  min-width:500px;
  padding: 50px;

  font-size: 20px;
}

</style>
