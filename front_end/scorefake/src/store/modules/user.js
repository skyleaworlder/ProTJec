import { login, refreshToken } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import router, { resetRouter } from '@/router'
import { getUserInfo } from '@/utils/jwt'
import { log } from 'util'
import { Message } from 'element-ui';

const state = {
  token: getToken(),
  name: '',
  avatar: '',
  introduction: '',
  roles: [],
  no: '',
  inst: '',
  grade: '',
  id: '',
  document: '',
  chat: ''
}

const mutations = {
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  },
  SET_NO: (state, no) => {
    state.no = no
  },
  SET_INST: (state, inst) => {
    state.inst = inst
  },
  SET_GRADE: (state, grade) => {
    state.grade = grade
  },
  SET_ID: (state, id) => {
    state.id = id
  },
  SET_CHAT: (state, chat) => {
    state.chat = chat
  },
  SET_DOCUMENT: (state, document) => {
    state.document = document
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    console.log(commit, userInfo, 'userinfo')
    const { no, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ no: no.trim(), password: password }).then(response => {
        // error process using response data status first
        if (response.data.status === 'NAME_PASSWORD_WRONG') {
          reject('Login Error: Name or Password Wrong!')
        } else {

        }

        const { proTJec_token } = response.data
        commit('SET_TOKEN', proTJec_token)
        setToken(proTJec_token)
        console.log(response, 'store/user.js', proTJec_token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      // console.log(resolve, "resolve")
      const token = getToken()
      // console.log(token)
      const userInfo = getUserInfo(token)
      console.log(token, userInfo, "token, userinfo")

      const data = {
        roles: [userInfo.level],
        introduction: '',
        avatar: userInfo.avatar,
        name: userInfo.name,
        no: userInfo.no,
        inst: userInfo.inst,
        grade: userInfo.grade,
        id: userInfo.id,
        chat: userInfo.chat,
        document: userInfo.document
      }
      // console.log(userInfo.level);

      // roles must be a non-empty array
      console.log(data, 'data<-')
      if (!data.roles || data.roles.length <= 0) {
        reject('getInfo: roles must be a non-null array!')
      }
      // console.log(data.roles, 'setroles');

      commit('SET_ROLES', data.roles)
      commit('SET_NAME', data.name)
      commit('SET_AVATAR', data.avatar)
      commit('SET_INTRODUCTION', data.introduction)
      commit('SET_INST', data.inst)
      commit('SET_NO', data.no)
      commit('SET_GRADE', data.grade)
      commit('SET_ID', data.id)
      commit('SET_DOCUMENT', data.document)
      commit('SET_CHAT', data.chat)
      resolve(data) // 这句话是干什么的啊？
    })
  },

  // refresh after update user profile
  refreshInfo({ commit, state, dispatch }, usr_no) {
    console.log("usr_no", usr_no)
    return new Promise((resolve, reject) => {
      const data = {
        no: usr_no
      }
      refreshToken(data).then(response => {
        if (response.data.status === 'GET_SUCCESS') {
          const { proTJec_token } = response.data
          commit('SET_TOKEN', proTJec_token)
          console.log(proTJec_token, "new protj token")
          setToken(proTJec_token)
          dispatch('getInfo')
          resolve(response.data)
          Message({
            message: '更新成功，刷新页面查看效果',
            type: 'success',
            duration: 1500
          })
        } else {
          Message({
            message: 'token 更新失败，请立即退出并重新登录',
            type: 'error',
            duration: 1500
          })
        }
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state, dispatch }) {
    return new Promise((resolve, reject) => {
      console.log('logout')
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      removeToken()
      resetRouter()

      // reset visited views and cached views
      // to fixed https://github.com/PanJiaChen/vue-element-admin/issues/2485
      dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      removeToken()
      resolve()
    })
  },

  // dynamically modify permissions
  changeRoles({ commit, dispatch }, role) {
    return new Promise(async resolve => {
      const token = role + '-token'

      commit('SET_TOKEN', token)
      setToken(token)

      const { roles } = await dispatch('getInfo')

      resetRouter()

      // generate accessible routes map based on roles
      const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })

      // dynamically add accessible routes
      router.addRoutes(accessRoutes)

      // reset visited views and cached views
      dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
