// used in store/modules/user.js

export function getJwtPayload(jwt) {
  console.log(jwt)
  var indexOfDot = jwt.indexOf('.')
  var tmp = jwt.substring(indexOfDot + 1, jwt.length - 1)
  console.log(tmp, indexOfDot)
  indexOfDot = tmp.indexOf('.')
  var payload = tmp.substring(0, indexOfDot)
  console.log(payload, indexOfDot, tmp)
  return window.atob(payload)
}

/**
   *
   userInfo format:
   {
    "user_name": "admin",
    "scope": [
      "read",
      "write"
    ],
    "exp": 1576826361,
    "authorities": [
      "AUTH_USER",
      "AUTH_ADMIN"
    ],
    "jti": "61aab180-0286-4139-b598-386508c938ed",
    "tenant": 1,
    "client_id": "client"
  }
   * @param {*} jwt
   */
export function getUserInfo(jwt) {
  const jwtPayload = getJwtPayload(jwt)
  // console.log(jwtPayload)
  // alert(JSON.stringify(jwtPayload));
  // TODO:改为，如果尚未存入sessionStorage，先将解码之后的用户信息存入sessionStorage
  return JSON.parse(jwtPayload)
}
