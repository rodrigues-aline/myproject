<template>
  <div>
    <v-container>
        <v-btn :to="{name: 'questions'}" ripple color="indigo darken-4">Responder Questionário</v-btn>
    </v-container>
    <dashboard :dashboard="dashboard"></dashboard>
    </div>
</template>

<script>

import dashboard from '~/components/Dashboard.vue'

export default {
  props: ['dashboard'],
  components: {
    dashboard
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
