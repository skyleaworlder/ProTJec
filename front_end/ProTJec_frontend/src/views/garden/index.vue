<template>
  <div class="garden-container">
    <div style="padding-left:30px">
      <el-row>
        <el-col v-for="link in links" :key="link.url"
          :lg="{offset:1,span:6}"
          :sm="{offset:2,span:8}"
          :xs="{offset:1,span:12}"
          class="adv-container" style="padding-top:20px">
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
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: [
        {
          pic: require('./assets/jiying0.png'),
          title: '不看看 CXCY 吗？',
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
        },
        {
          pic: require('./assets/jiying3.png'),
          title: '好像现在要上课了',
          subtitle: '同济大学教务系统',
          url: 'http://1.tongji.edu.cn',
          click: '看看课表'
        },
        {
          pic: require('./assets/jiying4.png'),
          title: '该学习了',
          subtitle: '西南一微信公众号',
          url: 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU1MjI5MzUwNg==&scene=124#wechat_redirect',
          click: '先洗个澡'
        },
        {
          pic: require('./assets/jiying6.jpg'),
          title: '作业今天截止',
          subtitle: '同济大学Canvas',
          url: 'http://canvas.tongji.edu.cn/',
          click: '一键补完'
        },
        {
          pic: require('./assets/jiying7.jpg'),
          title: '期中退课',
          subtitle: '同济大学4m3',
          url: 'http://4m3.tongji.edu.cn/',
          click: '好的'
        },
        {
          pic: require('./assets/jiying5.png'),
          title: '起床了',
          subtitle: '同济大学Course',
          url: 'http://courses.tongji.edu.cn',
          click: 'zooooom'
        },
        {
          pic: require('./assets/jiying8.png'),
          title: '建模就完事儿了',
          subtitle: '同济大学数学建模',
          url: 'https://math.tongji.edu.cn/model/',
          click: '开吹'
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.garden-container {
  margin-top: 20px;
}
</style>