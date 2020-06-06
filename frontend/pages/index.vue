<template>
    <home :dashboard="dashboard"></home>
</template>

<script>

import home from '~/components/Home.vue'
import api from '~api'

export default {
  components: {
    home
  },
  data () {
    return {
      dashboard: null
    }
  },
  asyncData () {
    return api.dashboard().then(result => {
      debugger
      return {dashboard: result}
    })
  }
}
</script>

<style>
</style>
