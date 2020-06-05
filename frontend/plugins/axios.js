import axios from 'axios'

axios.defaults.headers.common.tabid = (Math.random() * 1e8).toFixed(0)
console.log(process.env.BASE_URL)
export default axios.create({
  xsrfHeaderName: 'X-CSRFToken',
  xsrfCookieName: 'csrftoken',
  baseURL: process.env.BASE_URL,
  withCredentials: true
})
