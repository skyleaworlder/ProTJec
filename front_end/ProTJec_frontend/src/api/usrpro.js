import request from '@/utils/request'

export function agreeJoinPro(data) {
  const { usr_id, pro_id } = data;
  return request({
    url: `/join/agree`,
    method: 'post',
    params: {
      id: usr_id
    },
    data
  })
}

export function requestJoin(data) {
  const { usr_id, pro_id } = data;
  return request({
    url: `/join/pro`,
    method: 'post',
    params: {
      id: usr_id
    },
    data
  })
}