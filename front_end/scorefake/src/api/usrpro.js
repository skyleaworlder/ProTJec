import request from '@/utils/request'

export function agreeJoinPro(data) {
  const { usr_id, pro_id } = data;
  return request({
    url: `/join/agree?id=${usr_id}`,
    method: 'post',
    data
  })
}

export function requestJoin(data) {
  const { usr_id, pro_id } = data;
  return request({
    url: `/join/pro?id=${usr_id}`,
    method: 'post',
    data
  })
}