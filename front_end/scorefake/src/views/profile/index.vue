<template>
  <div class="profile-container">
    <div v-if="user">
      <el-row :gutter="20">

        <el-col :span="6" :xs="24">
          <user-card :user="user" />
        </el-col>

        <el-col :span="18" :xs="24">
          <el-card>
            <el-tabs v-model="activeTab">
              <el-tab-pane v-if="accountVisible"
                label="Activity" name="activity">
                <activity />
              </el-tab-pane>
              <el-tab-pane label="Timeline" name="timeline">
                <timeline />
              </el-tab-pane>
              <!-- TODO: 想用一个变量解决，如何办到？？？ -->
              <el-tab-pane v-if="accountVisible" label="Account" name="account">
                <account :user="user" />
              </el-tab-pane>
            </el-tabs>
          </el-card>
        </el-col>

      </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import UserCard from './components/UserCard'
import Activity from './components/Activity'
import Timeline from './components/Timeline'
import Account from './components/Account'
import { getInfo } from '@/api/user'
import { Message } from 'element-ui'

export default {
  name: 'Profile',
  components: { UserCard, Activity, Timeline, Account },
  data() {
    return {
      user: {
        no: '',
        name: '',
        grade: '',
        inst: '',
        avatar: '',
        document: '',
        chat: ''
      },
      own: true,
      activeTab: 'timeline',
      loading: false,
      accountVisible: false
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])
  },
  created() {
    this.getUser()
    console.log(this.user, "profile created")
    this.accountVisible = (this.$route.params.id == this.$store.state.user.id) ? true:false
  },
 
  methods: {
    getUser() {
      const usr_id = this.$route.params.id
      getInfo({ usr_id }).then(response => {
        this.loading = true
        if (response.data.status == 'GET_SUCCESS') {
          const data = {
            no: response.data.data['no'],
            name: response.data.data['name'],
            grade: response.data.data['grade'],
            inst: response.data.data['inst'],
            avatar: response.data.data['avatar'],
            document: response.data.data['document'],
            chat: response.data.data['chat']
          }
          this.user = data
        } else {
          Message({
            message: '用户信息读取错误，请退出并刷新页面！',
            type: 'error',
            duration: 1500
          })
        }
      }, setTimeout(() => {
        this.loading = false
      }, 1.5 * 1000)).catch(error => {
        Message({
          message: String(error),
          type: 'error',
          duration: 1500
        })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.profile-container {
  padding: 20px;
}
</style>