/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validNo(str) {
  for (let index = 0; index < str.length; index++) {
    if (str[index] < '0' || str[index] > '9') {
      return false
    }
  }
  if (str.length <= 4 || str.length >= 8) {
    return false
  } else {
    return true
  }
}

/**
 * @param {string} url
 * @returns {Boolean}
 */
export function validURL(url) {
  const reg = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/
  return reg.test(url)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validLowerCase(str) {
  const reg = /^[a-z]+$/
  return reg.test(str)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUpperCase(str) {
  const reg = /^[A-Z]+$/
  return reg.test(str)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validAlphabets(str) {
  const reg = /^[A-Za-z]+$/
  return reg.test(str)
}

/**
 * @param {string} email
 * @returns {Boolean}
 */
export function validEmail(email) {
  const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  return reg.test(email)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function isString(str) {
  if (typeof str === 'string' || str instanceof String) {
    return true
  }
  return false
}

/**
 * @param {Array} arg
 * @returns {Boolean}
 */
export function isArray(arg) {
  if (typeof Array.isArray === 'undefined') {
    return Object.prototype.toString.call(arg) === '[object Array]'
  }
  return Array.isArray(arg)
}


export const validateName = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('项目名称不能为空'))
  } else {
    callback()
  }
}
export const validateSort = (rule, value, callback) => {
  console.log(value);
  
  if (value.length <= 0) {
    callback(new Error('项目分类不能为空'))
  } else {
    callback()
  }
}
export const validateTime = (rule, value, callback) => {
  if (!value && value.length <= 0) {
    callback(new Error('项目终止时间不能为空'))
  } else {
    callback()
  }
}
export const validateNeed = (rule, value, callback) => {
  if (value && value >= 1 && value <= 10) {
    callback()
  } else {
    callback(new Error('项目需求人数不能为空'))
  }
}
export const validateIntro = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('项目简介不能为空'))
  } else {
    callback()
  }
}
export const validateUsrName = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('用户名不能为空'))
  } else {
    callback()
  }
}
export const validateUsrInst = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('学院不能为空'))
  } else {
    callback()
  }
}
export const validateUsrGrade = (rule, value, callback) => {
  if (value.length <= 0) {
    callback(new Error('年级不能为空'))
  } else {
    callback()
  }
}