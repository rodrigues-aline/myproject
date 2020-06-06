<template>
  <v-app-bar color="indigo darken-4" dark fixed app clipped-right>
    <v-toolbar-title>
      <v-btn :to="{name: 'index'}" text dark ripple>Home</v-btn>
    </v-toolbar-title>
    <v-spacer />
  </v-app-bar>
</template>

<script>
import Snacks from '~/helpers/Snacks.js'
import api from '~api'

export default {
  props: ['state'],
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    async logout () {
      await api.logout()
      this.$store.commit('auth/setCurrentUser', null)
      Snacks.show(this.$store, {text: 'Até logo!'})
    }
  }
}
</script>
