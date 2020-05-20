<template>
  <div class="post">
    <div class="user-block">
      <img class="img-circle" :src="responder.avatar">
      <span class="username text-muted">{{ responder.name }}</span>
      <span class="description">{{ responder.inst }} - {{ responder.rsp_time }}</span>
    </div>
    <p>{{ responder.document }}</p>
    <ul class="list-inline">
      <li>
        <span class="link-black text-sm">
          <i class="el-icon-share" />
          同意
        </span>
      </li>
      <li>
        <span class="link-black text-sm">
          <svg-icon icon-class="like" />
          拒绝
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ReqPost',
  props: {
    responder: { type: Object, required: true }
  }
}
</script>


<style lang="scss" scoped>
.user-activity {
  .pro-zone {
    overflow: hidden;
    padding: 0 0 40px 0;
    border-bottom: 1px solid #d2d6de;
  }
  .user-block {

    .username,
    .description {
      display: block;
      margin-left: 50px;
      padding: 2px 0;
    }

    .username{
      font-size: 16px;
      color: #000;
    }

    :after {
      clear: both;
    }

    .img-circle {
      border-radius: 50%;
      width: 40px;
      height: 40px;
      float: left;
    }

    span {
      font-weight: 500;
      font-size: 12px;
    }
  }

  .post {
    font-size: 14px;
    border-bottom: 1px solid #d2d6de;
    margin: 15px 0 15px 0;
    padding: 15px 0 15px 0;
    color: #666;

    .image {
      width: 100%;
      height: 100%;

    }

    .user-images {
      padding-top: 20px;
    }
  }

  .list-inline {
    padding-left: 0;
    margin-left: -5px;
    list-style: none;

    li {
      display: inline-block;
      padding-right: 5px;
      padding-left: 5px;
      font-size: 13px;
    }

    .link-black {

      &:hover,
      &:focus {
        color: #999;
      }
    }
  }

}

.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}
</style>
