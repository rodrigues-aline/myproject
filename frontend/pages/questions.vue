<template>
  <questions :questions="questions" :useranswers="useranswers"></questions>
</template>

<script>

import api from '~api'
import questions from '~/components/Questions.vue'

export default {
  components: {
    questions
  },
  data () {
    return {
      questions: null,
      useranswers: null
    }
  },
  asyncData () {
    return api.list_questions().then(result => {
      const questions = result.questions
      const answers = result.answers
      const new_questions = []
      const user_answers = {age: 0, latitude: 0, longitude: 0, questions: {}}
      questions.forEach((q) => {
        new_questions.push(q)
        user_answers.questions[q.id] = {answer: null}
        new_questions[new_questions.length - 1].answers = []
        answers.forEach((a) => {
          if (q.id === a.question_id) {
            new_questions[new_questions.length - 1].answers.push(a)
          }
        })
      })
      return {questions: new_questions, useranswers: user_answers}
    })
  },
  mounted () {
    if (window.navigator.geolocation) {
      window.navigator.geolocation.getCurrentPosition(position => {
        this.useranswers.latitude = position.coords.latitude
        this.useranswers.longitude = position.coords.longitude
      })
    } else {
      this.useranswers.latitude = 0
      this.useranswers.longitude = 0
    }
  }
}
</script>

<style>
</style>
