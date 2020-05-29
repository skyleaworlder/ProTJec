<template>
  <el-card class="req-card" :class="getColor(proInfo.sort)">
    <div slot="header" class="card-header">
      <span>{{ proInfo.name }}</span>
        <el-tag class="right-tag" size="mini"
          :type="getButtonColor(proInfo.sort)"
          @click.native="sb">
          详情</el-tag>
    </div>

    <div class="card-content">
      <el-col :span="24">
        <div class="card-content-left" style=" text-align:center">
          <span style="padding-left: 10px; font-size: 90px;">{{ proInfo.need }}</span>
          <span>Waiting...</span>
        </div>
      </el-col>
    </div>
  </el-card>
</template>

<script>

import '@/styles/reqcard.scss'

export default {
  name: 'ReqCard',
  props: {
    proInfo: { type: Object, required: true },
    callback: { type: Function, required: true }
  },
  methods: {
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
    },
    sb() {
      this.$props.callback(this.$props.proInfo)
      console.log(this.$props.proInfo.id)
    }
  }
}
</script>

<style lang="scss">
</style>

<style lang="scss" scoped>
</style>
