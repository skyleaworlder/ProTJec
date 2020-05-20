import request from '@/utils/request'

export function fetchAllTags(data) {
  return request({
    url: `/tags`,
    method: 'get'
  })
}