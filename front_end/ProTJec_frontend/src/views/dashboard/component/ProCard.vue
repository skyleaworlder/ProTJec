<template>
  <el-card class="proj-card" :class="getColor(sort)" shadow="always">
    <div slot="header" class="card-header">
      <span>{{ name }}</span>
      <router-link :to="'/projects/'+id">
        <el-tag
          class="right-tag"
          :type="getButtonColor(sort)"
          size="mini"
        >查看详情</el-tag>
      </router-link>
    </div>

    <div class="card-content">
      <el-col :span="7">
        <div class="card-content-left">
          <span style="padding-left: 10px; font-size: 50px">{{ need }}</span>
          <span style="padding-left: 5px">Waiting...</span>
          <div style="padding: 5px; text-align: right; color: #999">
            火速加入！<br> 一起来做项目吧！
          </div>
        </div>
      </el-col>
      <el-col :span="17">
        <div class="card-content-right">
          {{ intro }}
        </div>
      </el-col>
    </div>
    <div class="time">
      <span class="releaseTime"> 发布时间：{{ releaseTime }} </span>
    </div>
  </el-card>
</template>

<script>

import '@/styles/procard.scss'

export default {
  name: 'ProCard',
  props: {
    name: { type: String, required: true },
    sort: { type: String, required: true },
    id: { type: Number, required: true },
    need: { type: Number, required: true },
    intro: { type: String, required: true },
    releaseTime: { type: String, required: true }
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
    }
  }
}
</script>

<style lang="scss">
</style>

<style lang="scss" scoped>
</style>
