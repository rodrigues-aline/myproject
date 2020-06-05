export const state = () => ({
  loading: {}
})

export const mutations = {
  set (state, newstate) {
    state.loading = {show: newstate}
  }
}

export const getters = {
}

export const actions = {
}
