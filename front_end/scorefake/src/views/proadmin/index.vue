<template>
  <div class="pro-container">
    <!-- 表格 div/main/contain/header|table-->
    <div class="filter-container">
      <el-input
        v-model="rowSelect.name"
        placeholder="工程名称"
        style="width: 200px"
        class="select-input"
        @keyup.enter.native="select"
      />
      <el-input
        v-model="rowSelect.time"
        placeholder="创建时间"
        style="width: 200px"
        class="select-input"
      />
      <el-input
        v-model="rowSelect.unit"
        placeholder="单位"
        style="width: 200px"
        class="select-input"
      />
      <el-button
        class="select-item"
        style="margin-left: 10px"
        type="primary"
        icon="el-search"
        @click="select"
      >查找</el-button>
      <el-button
        class="select-item"
        style="margin-left: 10px;"
        type="primary"
        icon="el-icon-edit"
        @click="insert"
      >
        新增
      </el-button>
    </div>

    <el-main>
      <el-container>
        <el-header
          style="height:100%;"
        >
          工程管理：
        </el-header>
        <el-table
          :header-cell-style="{background:'#ddf0e6',color:'#606266'}"
          :data="tableData"
          max-height="300"
          style="width: 100%"
          fit
          border
          highlight-current-row
          @sort-change="sortChange"
        >
          <el-table-column
            prop="id"
            label="序号"
            width="180"
            align="center"
          />
          <el-table-column
            prop="name"
            label="工程名称"
            width="360"
            align="center"
          />
          <el-table-column
            prop="time"
            label="创建时间"
            width="180"
            align="center"
          />
          <el-table-column
            prop="unit"
            label="单位"
            width="400"
            align="center"
          />
          <el-table-column
            label="操作"
            align="center"
            width="200"
          >
            <template slot-scope="{row, $index}">
              <el-button
                type="primary"
                size="mini"
                @click="deleteRow(row, $index)"
              >
                删除</el-button>
              <el-button
                type="primary"
                size="mini"
                @click="updateRow(row)"
              >
                修改</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-container>

      <pagination
        v-show="total>0"
        :total="total"
        :page.sync="rowSelect.page"
        :limit.sync="rowSelect.limit"
        @pagination="getList"
      />
      <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
        <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
          <el-form-item label="名称" prop="name">
            <el-input v-model="temp.name" />
          </el-form-item>
          <el-form-item label="时间" prop="time">
            <el-date-picker v-model="temp.time" type="datetime" placeholder="Please pick a date" />
          </el-form-item>
          <el-form-item label="单位" prop="unit">
            <el-input v-model="temp.unit" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="Please input" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">
            取消
          </el-button>
          <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
            确认
          </el-button>
        </div>
      </el-dialog>
      <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
        <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
          <el-table-column prop="key" label="Channel" />
          <el-table-column prop="pv" label="Pv" />
        </el-table>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="dialogPvVisible = false">Confirm</el-button>
        </span>
      </el-dialog>

      <el-container>
        <el-image
          v-for="url in urls"
          :key="url"
          :src="url"
          lazy
        />
      </el-container>
    </el-main>
  </div>
</template>

<script>
import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // sec

const calendarTypeOptions = [
  { key: 'CN', display_name: 'China' },
  { key: 'US', display_name: 'USA' },
  { key: 'JP', display_name: 'Japan' },
  { key: 'EU', display_name: 'Eurozone' }
]

// arr to obj, such as { CN : "China", US : "USA" }
const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {
  name: 'ProAdmin',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      total: 0,
      listLoading: true,
      rowSelect: {
        page: 1,
        limit: 20,
        name: undefined,
        time: undefined,
        unit: undefined,
        sort: '+id'
      },
      activeIndex: '1',
      importanceOptions: [1, 2, 3],
      calendarTypeOptions,
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['published', 'draft', 'deleted'],
      showReviewer: false,
      temp: {
        id: undefined,
        importance: 1,
        remark: '',
        name: '',
        time: new Date(),
        unit: '',
        status: 'published'
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        time: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }]
      },
      downloadLoading: false,

      tableData: [{
        id: 1,
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '设计烧烤架'
      }, {
        id: 2,
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '构造烧烤架'
      }, {
        id: 3,
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '购买红薯'
      }, {
        id: 4,
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '烤红薯'
      }],
      urls: [
        require('@/assets/proj/bar.png'),
        require('@/assets/proj/barbar.png'),
        require('@/assets/proj/pie.png')
      ]
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getIndex(index) {
      return index + 1
    },
    deleteRow(row, index) {
      console.log(index, row)
      this.tableData.splice(index, 1)
    },
    /*
    getList() {
      this.listLoading = true
      fetchList(this.rowSelect).then(response => {
        this.list = response.data.items
        console.log(this.list);
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
*/
    getList() {
      this.list = this.tableData
    },
    select() {
      this.rowSelect.page = 1
      // this.getList()
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: 'ćä˝Success',
        type: 'success'
      })
      row.status = status
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.rowSelect.sort = '+id'
      } else {
        this.rowSelect.sort = '-id'
      }
      this.select()
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        importance: 1,
        remark: '',
        timestamp: new Date(),
        title: '',
        status: 'published',
        type: ''
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    insert() {
      console.log(this.$refs['dataForm'])
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.temp.author = 'vue-element-admin'
          createArticle(this.temp).then(() => {
            this.tableData.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    updateRow(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          updateArticle(tempData).then(() => {
            const index = this.tableData.findIndex(v => v.id === this.temp.id)
            console.log(this.temp.id, index, this.temp, tempData)

            this.tableData.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.tableData.splice(index, 1)
    },
    handleFetchPv(pv) {
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
      })
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['timestamp', 'title', 'type', 'importance', 'status']
        const filterVal = ['timestamp', 'title', 'type', 'importance', 'status']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'table-list'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.tableData.map(v => filterVal.map(j => {
        if (j === 'time') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    getSortClass: function(key) {
      const sort = this.rowSelect.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    }
  }
}
</script>

<style lang="scss">

$container_bg: rgba(240, 242, 245, 1);
$table_title:#026d49;
$sidebar_bg: #ddf0e6;
$table_title_font: #fff;
$table_title_bg: #ddf0e6;

.pro-container {
  padding: 0px 0px 0px 0px;
  .filter-container {
    padding-left: 40px;
    padding-top: 20px;
    padding-right: 40px;
    padding-bottom: 0px;
  }
  /* 顶导航栏 */
  .el-container {
    .el-header {
      background-color: $table_title;
      text-align: left;
      height: 100px;
      padding: 10px; /* for table's title*/
      color: $table_title_font;
    }
  }

  /* 侧栏 */
  .el-aside {
    /* 头像 */
    background-color: $sidebar_bg;

    /* 侧导航栏 */
    .el-main {
      background-color: $sidebar_bg;
    }
  }

  .el-main {

    /* 表格外的背景 */
    background-color: $container_bg;

    /* 表格标签合成 */
    .el-container {
      /* 表格间间距 */
      margin: 20px;

      /* 表格 */
      .el-table {
        box-shadow: 10px, #fff;

        /* 表格滑动条上方空白 */
        th.gutter {
          background-color: $table_title_bg;
        };
      }
    }
  }
}

</style>

<style lang="scss" scoped>
</style>
