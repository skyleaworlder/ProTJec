<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of logs" :key="index" :timestamp="item.time" placement="top">
        <el-card>
          <h4>{{ item.comment }}</h4>
          <p>{{ item.time }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
import { fetchLogs } from '@/api/user'
import { Message } from 'element-ui'

export default {
  data() {
    return {
      select: {
        limit: 5,
        offset: 0
      },
      logs: []
    }
  },
  created() {
    this.getLogs()
  },
  methods: {
    getLogs() {
      const params = {
        usr_id: this.$store.state.user.id,
        limit: this.select.limit,
        offset: this.select.offset
      }
      fetchLogs(params).then(response => {
        const { data, status } = response.data
        if (status == 'GET_SUCCESS') {
          // a way to concat array
          this.logs.push(...data.loginLogs)
        } else {
          Message({ type:"error", message:"获取日志错误，请刷新后重试", duration:1500 })
        }
      }).catch(err => {
        Message({ type:"error", message:err, duration:1500 })
      })
    }
  }
}
</script>
