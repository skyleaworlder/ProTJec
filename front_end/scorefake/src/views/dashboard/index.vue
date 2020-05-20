<template>
  <div class="dash-container">
    <!-- 表格 div/main/contain/header|table-->

    <el-col :gutter="20" :offset="5">
      <el-row
        v-for="elem in projects"
        :key="elem.name"
        :span="12"
      >
        <pro-card
          :id="elem.id"
          :name="elem.name"
          :sort="elem.sort"
          :release-time="elem.releaseTime"
          :need="elem.need"
          :intro="elem.intro"
        />
      </el-row>
      <el-pagination :page-size="projectsQuery.limit" :current-page.sync="projectsQuery.page" :total="proTotal"
        style="padding:20px" layout="prev, pager, next, jumper"
        @current-change="pageChange" />
    </el-col>
    as
  </div>
</template>

<script>

import ProCard from './component/ProCard'
import { fetchProjects } from '@/api/projects'

export default {
  name: 'Dashboard',
  components: { ProCard },
  data() {
    return {
      projects: '',
      projectsLoading: false,
      projectsQuery: {
        limit: 2,
        page: 1
      },
      proTotal: 0
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
      console.log('ljgsb')
      this.projectsLoading = true
      fetchProjects(this.projectsQuery).then(response => {
        console.log(response, 'respon')

        const { status, data } = response.data
        if (status === 'GET_SUCCESS') {
          this.projects = data.projects
          this.proTotal = data.total
        } else {
        }
      },setTimeout(() => {
        this.projectsLoading = false
      }, 1.5 * 1000))
    },
    pageChange(newPage) {
      console.log(newPage,"newpage");
      this.initProjects()
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
</style>
