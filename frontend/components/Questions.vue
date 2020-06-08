<template>
  <v-container>
    <h1>Perguntas</h1>
    <br/><v-divider></v-divider><br/>
    <v-card v-for="(q, i) in questions" :key="q.id" class="pa-2" outlined tile>
      <v-list-item>
        <v-list-item-content>
          <div><b>{{i+1}}</b> - {{q.question}}</div>
          <v-radio-group v-model="useranswers.questions[q.id].answer">
            <v-radio v-for="a in q.answers" :key="a.id" :label="`${a.answer}`" :value="a.id" />
          </v-radio-group>
        </v-list-item-content>
      </v-list-item>
    </v-card>
    <br>
    <v-btn color="indigo darken-4" block large @click="submit()">Enviar Respostas</v-btn>
  </v-container>
</template>

<script>

import api from '~api'
import Loading from '~/helpers/Loading.js'
import Snacks from '~/helpers/Snacks.js'

export default {
  props: ['questions', 'useranswers'],
  data () {
    return {}
  },
  created () {
    if (this.questions.length === 0) {
      Snacks.show(this.$store, {text: 'Não há perguntas para responder', color: 'error'})
      this.$router.push({name: 'index'})
    }
  },
  methods: {
    submit () {
      Snacks.hide(this.$store)
      let form_ok = true
      const questions = Object.keys(this.useranswers.questions)
      for (let key = 0; key < questions.length; key++) {
        if (this.useranswers.questions[questions[key]].answer === null) {
          Snacks.show(this.$store, {text: 'Responda todas as perguntas', color: 'error'})
          form_ok = false
          break
        }
      }
      if (form_ok) {
        Loading.show(this.$store, true)
        api.add_answers(this.useranswers).then(result => {
          Loading.show(this.$store, false)
          Snacks.show(this.$store, {text: 'Questionário respondido com sucesso'})
          this.$router.push({name: 'index'})
        })
      }
    }
  }
}
</script>

<style>
</style>
