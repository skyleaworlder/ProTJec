<template>
  <div class="add-pro-container">
    <div class="add-pro-title">
      新项目创建
    </div>
    <el-form
      ref="tmpProInfo"
      :model="tmpProInfo"
      :rules="rules"
      class="add-pro-form"
    >
      <el-form-item label="项目名称" prop="name">
        <el-input
          ref="name"
          v-model="tmpProInfo.name"
          placeholder="请输入项目名称"
          class="add-pro-name"
        />
      </el-form-item>
      <el-form-item label="项目种类" prop="sort">
        <el-select
          ref="sort"
          v-model="tmpProInfo.sort"
          placeholder="请选择项目种类"
          class="add-pro-sort"
        >
          <el-option v-for="type in proTypes" :key="type.key" :label="type.displayName" :value="type.key" />
        </el-select>
      </el-form-item>
      <el-form-item label="截止时间" prop="endTime">
        <el-date-picker
          ref="endTime"
          v-model="tmpProInfo.endTime"
          value-format="yyyy-MM-dd HH:mm:ss"
          type="datetime"
          placeholder="请选择征集截至时间"
          class="add-pro-time"
        />
      </el-form-item>
      <el-form-item label="需求人数" prop="need">
        <el-input-number ref="need" v-model="tmpProInfo.need" :min="1" :max="10" />
      </el-form-item>
      <el-form-item label="项目介绍" prop="intro">
        <el-input
          ref="intro"
          v-model="tmpProInfo.intro"
          type="textarea"
          :rows="6"
        />
      </el-form-item>
      <div style="margin-bottom: 20px">
        <label class="el-form-item__label">新增Tags</label>
        <el-tag
          v-for="tag in dynamicTags"
          :key="tag.id"
          closable
          :disable-transitions="false"
          @close="handleCloseTag(tag)"
        >
          {{ tag.name }}</el-tag>
        <el-select
          ref="saveTagInput"
          v-model="inputValue"
          size="small"
          class="input-new-tag"
          @change="handleInputConfirm"
        >
<!-- 接口定义于此，后面没有改过，所以一直都是 id 和 name -->
          <el-option v-for="tag in allTags"
            :key="tag.id" :label="tag.name" :value="{id:tag.id, name:tag.name}" />
        </el-select>
      </div>
    </el-form>
    <div class="btn-container">
      <el-button
        type="primary"
        class="add-pro-btn"
        @click="handleAddPro()"
      >
        提交</el-button>
      <el-button
        type="primary"
        class="add-pro-btn"
        @click="clean()"
      >
        清空</el-button>
    </div>

  </div>
</template>

<script>

import { addProject } from '@/api/projects'
import { fetchAllTags } from '@/api/tags'
import { Message } from 'element-ui'

const proTypes = [
  { key: '理工', displayName: '理工' },
  { key: '社科', displayName: '社科' },
  { key: '文史', displayName: '文史' },
  { key: '经管', displayName: '经管' },
  { key: '设计', displayName: '设计' },
  { key: '其他', displayName: '其他' }
]
const validateName = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('项目名称不能为空'))
  } else {
    callback()
  }
}
const validateSort = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('项目分类不能为空'))
  } else {
    callback()
  }
}
const validateTime = (rule, value, callback) => {
  if (!value && value.length <= 0) {
    callback(new Error('项目终止时间不能为空'))
  } else {
    callback()
  }
}
const validateNeed = (rule, value, callback) => {
  if (value && value >= 1 && value <= 10) {
    callback()
  } else {
    callback(new Error('项目需求人数不能为空'))
  }
}
const validateIntro = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('项目简介不能为空'))
  } else {
    callback()
  }
}
export default {
  name: 'AddPro',
  data() {
    return {
      proTypes,
      inputValue: {},
      inputVisible: false,
      tmpProInfo: {
        usr_id: this.$store.state.user.id,
        name: '',
        sort: '',
        endTime: '',
        need: '',
        intro: ''
      },
      dynamicTags: [],
      rules: {
        name: [{ required: true, trigger: 'change', validator: validateName }],
        sort: [{ required: true, trigger: 'change', validator: validateSort }],
        endTime: [{ required: true, trigger: 'change', validator: validateTime }],
        need: [{ required: true, trigger: 'change', validator: validateNeed }],
        intro: [{ required: true, trigger: 'change', validator: validateIntro }]
      },
      allTags: []
    }
  },
  created() {
    this.getTags()
  },
  methods: {
    fuck() {
      console.log('mounted well fuck!')
    },
    getTags() {
      fetchAllTags().then(response => {
        const data = response.data
        console.log(data, "tagstags");
        
        if (data.status === 'GET_SUCCESS') {
          this.allTags = data.data.tags
          this.inputValue = this.allTags[0]
          console.log(this.allTags);
          
        } else {
          Message({
            message: 'Tags 获取失败',
            type: 'error',
            duration: 1500
          })
        }
      }).catch(error => {
        Message({
          message: error,
          type: 'error',
          duration: 1500
        })
      })
    },
    handleAddPro() {
      const data = {
        usr_id: this.tmpProInfo.usr_id,
        name: this.tmpProInfo.name,
        sort: this.tmpProInfo.sort,
        endTime: this.tmpProInfo.endTime,
        need: this.tmpProInfo.need,
        intro: this.tmpProInfo.intro,
        tags: this.dynamicTags
      }
      console.log(data)
      console.log(this.$refs, 'refs')

      this.$refs.tmpProInfo.validate(valid => {
        if (valid) {
          addProject(data).then(response => {
            const data = response.data
            if (data.status === 'PROJ_SUCCESS') {
              Message({
                message: '项目发布成功',
                type: 'success',
                duration: 5000
              })
              this.clean()
            }
          }).catch(error => {
            Message({
              message: '项目发布失败：' + error,
              type: 'error',
              duration: 5000
            })
          })
        } else {
          Message({
            message: '项目发布失败',
            type: 'error',
            duration: 5000
          })
        }
      })
    },
    clean() {
      this.tmpProInfo = {
        name: '',
        sort: '',
        endTime: '',
        need: '',
        intro: ''
      }
      this.dynamicTags = []
    },

    handleCloseTag(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf((tag), 1))
    },
    showInput() {
      this.inputVisible = true
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus()
      })
    },
    handleInputConfirm() {
      const inputValue = this.inputValue
      console.log(inputValue, this.dynamicTags, "dydydy");

      let isDump = false
      for (let index = 0; index < this.dynamicTags.length; index++) {
        if (this.dynamicTags[index].name == inputValue.name) {
          isDump = true
          Message({message: 'Tags 重复，请不要这样', type: 'warning', duration: 1500})
          break
        }
      }

      if (inputValue && !isDump) {
        this.dynamicTags.push(inputValue)
      }
      this.inputVisible = false
      this.inputValue = {}
    }
  }
}
</script>

<style lang="scss" scoped>

$col-width: 300px;

.add-pro-container {
  margin-top: 40px;
}

.add-pro-title {
  text-align: center;
  font-size: 30px;
}

.add-pro-form {
  padding: 40px 40px 0 40px;

  .add-pro-name {
    width: $col-width;
  }
  .add-pro-sort {
    width: $col-width;
  }
  .add-pro-time {
    width: $col-width;
  }
}

.el-form-item__error {
  padding-left: 80px;
}

.btn-container {
  padding: 0px 40px 0px 40px;
}

.add-pro-btn {
  width: 45%;
  min-width: 100px;
}

.input-new-tag {
  width: 100px;
  margin-left: 10px;
  margin-bottom: 10px;
  vertical-align: bottom;
}
.button-new-tag {
  margin-left: 10px;
  margin-bottom: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
}
.el-tag {
  margin-left: 10px;
  margin-bottom: 10px;
}

</style>
