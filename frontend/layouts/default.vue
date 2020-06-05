<template>
  <v-app id="inspire">
    <toolbar :state="layout" />
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <le-footer />
    <v-snackbar
      :timeout="snack.timeout"
      :color="snack.color"
      bottom
      v-model="snack.visible"
    >
      {{snack.text}}
      <v-btn dark text @click.native="closeSnack">Close</v-btn>
    </v-snackbar>
    <v-overlay :value="loading.show == true">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar.vue'
import footer from '~/components/footer.vue'
export default {
  components: {
    toolbar,
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: true
    }
  }),
  computed: {
    snack () {
      return JSON.parse(JSON.stringify(this.$store.state.snack.snack))
    },
    loading () {
      return this.$store.state.loading.loading
    }
  },
  methods: {
    closeSnack () {
      this.$store.commit('snack/hide')
    }
  }
}
</script>
