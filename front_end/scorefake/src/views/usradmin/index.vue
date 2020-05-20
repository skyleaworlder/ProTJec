<template>
  <div class="pro-container">
    <!-- 表格 div/main/contain/header|table-->
    <el-main>
      <el-container>
        <el-header
          style="height:100%;"
        >
          用户管理：
        </el-header>
        <el-table
          :header-cell-style="{background:'#ddf0e6',color:'#606266'}"
          :data="tableData"
          max-height="300"
          style="width: 100%"
        >
          <el-table-column
            prop="index"
            label="序号"
            width="90"
            type="index"
            align="center"
            :index="index"
          />
          <el-table-column
            prop="name"
            label="工程名称"
            width="100"
            align="center"
          />
          <el-table-column
            prop="time"
            label="创建时间"
            width="150"
            align="center"
          />
          <el-table-column
            prop="unit"
            label="单位"
            width="180"
            align="center"
          />
          <el-table-column
            label="操作"
            align="center"
          >
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="deleteRow(scope.$index, scope.row)"
              >
                删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-container>

      <el-container>
        <el-image
          v-for="url in urls"
          :key="url"
          :src="url"
          :fit="fit"
          lazy
        />
      </el-container>
    </el-main>

  </div>
</template>

<script>
export default {
  name: 'ProAdmin',
  data() {
    return {
      activeIndex: '1',
      tableData: [{
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '设计烧烤架'
      }, {
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '构造烧烤架'
      }, {
        time: '2016-05-02',
        unit: '环球烤红薯有限公司',
        name: '购买红薯'
      }, {
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
  methods: {
    deleteRow(index, row) {
      console.log(index, row)
      this.tableData.splice(index, 1)
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
