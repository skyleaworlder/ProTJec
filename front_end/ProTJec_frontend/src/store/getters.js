const getters = {
  sidebar: state => state.app.sidebar,
  size: state => state.app.size,
  device: state => state.app.device,

  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,

  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  introduction: state => state.user.introduction,
  roles: state => state.user.roles,
  no: state => state.user.no,
  inst: state => state.user.inst,
  grade: state => state.user.grade,
  document: state => state.user.document,
  chat: state => state.user.chat,

  // long long ago, i mod roles to level, then router load again and again.
  permission_routes: state => state.permission.routes,
  errorLogs: state => state.errorLog.logs

}
export default getters
