import request from '@/utils/request'

export function login(data) {
  const { no, password } = data
  // console.log(no, password);
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function updateUsrInfo(data) {
  const { id, no, inst, grade, document, chat, avatar } = data
  return request({
    url: '/info/update',
    method:'post',
    data
  })
}

export function refreshToken(data) {
  const { no } = data
  return request({
    url: `/info/token?no=${no}`,
    method:"get"
  })
}

export function getInfo(data) {
  const { usr_id } = data
  const uri = `/info/get?id=${usr_id}`;
  return request({
    url: uri,
    method: 'get'
  })
}

/*

export function logout() {
  return request({
    url: '/vue-element-admin/user/logout',
    method: 'post'
  })
}

*/
