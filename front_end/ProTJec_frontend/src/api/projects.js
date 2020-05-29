import request from '@/utils/request'

export function fetchProjects(data) {
  return request({
    url: `/projects/fetch`,
    method: 'get',
    params: data
  })
}

export function addProject(data) {
  const { name, sort, endTime, need, intro, tags } = data
  // console.log('sb', name, sort, endTime, need, intro, tags)
  return request({
    url: '/projects/add',
    method: 'post',
    data
  })
}

export function updateProject(data) {
  const { id, name, sort, need, intro } = data
  return request({
    url: '/projects/update',
    method: 'post',
    data
  })
}

export function fetchProInfo(data) {
  console.log(data)
  const { id } = data
  return request({
    url: `/projects/info`,
    method: 'get',
    params: {
      id
    }
  })
}

export function fetchRequestUsers(data) {
  const { pro_id } = data
  return request({
    url: `/projects/requestUsers`,
    method: 'get',
    params: {
      pro_id
    }
  })
}

export function changeRequestStatus(data) {
  const { usr_id, pro_id, state } = data
  return request({
    url: `/response/changeState`,
    method:'post',
    data
  })
}