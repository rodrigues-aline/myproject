import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_questions () {
    return get('/api/list_questions')
  },
  add_answers (answers) {
    return post('/api/add_answers', {answers})
  },
  dashboard () {
    return get('/api/dashboard')
  }
}
