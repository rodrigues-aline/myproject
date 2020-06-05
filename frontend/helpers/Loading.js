export default {
  show (store, status) {
    store.commit('loading/set', status)
  }
}
