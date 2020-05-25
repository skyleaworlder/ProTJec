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
    url: `/info/token`,
    method:"get",
    params: {
      no
    }
  })
}

export function getInfo(data) {
  const { usr_id } = data
  const uri = `/info/get`;
  return request({
    url: uri,
    method: 'get',
    params: {
      id: usr_id
    }
  })
}


export function fetchLogs(data) {
  const { usr_id, limit, offset } = data
  return request({
    url: '/login/logs/fetch',
    method: 'get',
    params: {
      usr_id: usr_id,
      limit: limit,
      offset: offset
    }
  })
}
