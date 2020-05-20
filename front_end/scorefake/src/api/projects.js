import request from '@/utils/request'

export function fetchProjects(data) {
  console.log(data)
  let uri = `/projects/fetch`
  if ((data.limit && data.page) || data.initiatorId) {
    uri += `?`
    if (data.limit && data.page) {
      uri += `limit=${data.limit}&page=${data.page}&`
    }
    if (data.initiatorId) {
      uri += `initiatorId=${data.initiatorId}`
    }
  }
  console.log(uri);

  return request({
    url: uri,
    method: 'get'
  })
}

export function addProject(data) {
  console.log(data)
  const { name, sort, endTime, need, intro, tags } = data
  console.log('sb', name, sort, endTime, need, intro, tags)
  return request({
    url: '/projects/add',
    method: 'post',
    data
  })
}

export function fetchProInfo(data) {
  console.log(data)
  const { id } = data
  return request({
    url: `/projects/info?id=${id}`,
    method: 'get'
  })
}

export function fetchRequestUsers(data) {
  const { pro_id } = data
  return request({
    url: `/projects/requestUsers?pro_id=${pro_id}`,
    method: 'get'
  })
}