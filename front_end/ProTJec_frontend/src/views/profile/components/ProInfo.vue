<template>
  <div class="proinfo-container">
    <el-form ref="proInfo" :model="tmpInfo" :rules="rules">
      
      <el-form-item prop="name" label="项目名称">
          <template v-if="edit && usr_id==vis_id">
            <el-input ref="name" v-model="tmpInfo.name"
              size="small" placeholder="请输入项目名称" style="width:300px" />
          </template>
          <span v-else> {{ tmpInfo.name }}</span>
      </el-form-item>

      
      <el-form-item prop="sort" label="项目分类">
          <template v-if="edit && usr_id==vis_id">
            <el-select v-model="tmpInfo.sort" ref="sort"
              size="small" placeholder="请选择项目种类" >
              <el-option v-for="type in proTypes" :key="type.key" :label="type.displayName" :value="type.key" />
            </el-select>
          </template>
          <span v-else> {{ tmpInfo.sort }}</span>
      </el-form-item>

      
      <el-form-item prop="need" label="需求人数">
          <template v-if="edit && usr_id==vis_id">
            <el-input-number ref="need" v-model="tmpInfo.need" :min="1" :max="10" />
          </template>
          <span v-else> {{ tmpInfo.need }}</span>
      </el-form-item>


      <el-form-item prop="intro" label="项目简介">
          <template v-if="edit && usr_id==vis_id">
            <el-input ref="intro" v-model="tmpInfo.intro"
              type="textarea" :rows="6"
            />
          </template>
          <span v-else> {{ tmpInfo.intro }}</span>
      </el-form-item>

    </el-form>

    
    <div v-if="edit">
      <el-button type="primary" style="float:right;margin:5px"
        @click="cancelUpdate">
        取消提交</el-button>
      <el-button type="primary" style="float:right;margin:5px"
        @click="update">
        确认提交</el-button>
    </div>
    <el-button v-else type="primary" style="float:right;margin:5px"
      @click="startedit">
      修改项目信息</el-button>
  </div>
</template>

<script>
import { validateName, validateSort, validateNeed, validateIntro } from '@/utils/validate'
import { updateProject } from '@/api/projects'
import { Message } from 'element-ui'

const proTypes = [
  { key: '理工', displayName: '理工' },
  { key: '社科', displayName: '社科' },
  { key: '文史', displayName: '文史' },
  { key: '经管', displayName: '经管' },
  { key: '设计', displayName: '设计' },
  { key: '其他', displayName: '其他' }
]

export default {
  name: 'ProInfo',
  props: {
    proInfo: { type: Object, required: true },
    usr_id: { required: true },
    vis_id: { required: true }
  },
  data() {
    return {
      proTypes,
      tmpInfo: {
        id: this.proInfo.id,
        name: this.proInfo.name,
        sort: this.proInfo.sort,
        intro: this.proInfo.intro,
        need: this.proInfo.need
      },
      edit: false,
      rules: {
        name: [{ required: true, trigger: 'change', validator: validateName }],
        sort: [{ required: true, trigger: 'change', validator: validateSort }],
        need: [{ required: true, trigger: 'change', validator: validateNeed }],
        intro: [{ required: true, trigger: 'change', validator: validateIntro }]
      }
    }
  },
  watch: {
    proInfo(newv, oldv) {
      this.tmpInfo = newv
      this.edit = false
    }
  },
  methods: {
    startedit() {
      this.edit = true
    },
    update() {
      updateProject(this.tmpInfo).then(response => {
        console.log(response, "update");
        const { data } = response
        if (data.status == 'PROJ_SUCCESS') {
          Message({ type:"success", message:"项目信息修改成功", duration:1500 })
        } else {
          Message({ type:"error", message:"项目信息修改失败", duration:1500 })
        }
        this.edit = false
      }).catch(err => {
        Message({ type:"error", message:err, duration:1500 })
      })
    },
    cancelUpdate() {
      this.edit = false
      Message({ type:"success", message:"取消修改成功", duration:1500 })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>