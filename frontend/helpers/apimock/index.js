import { zuck } from './db_people'
import { dashboard } from './db_dashboard'
import { questions } from './db_questions'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = {authenticated: keepLoggedIn}
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  dashboard () {
    return mockasync({dashboard: dashboard.dashboard, questions: questions.questions, answers: questions.answers})
  },
  list_questions () {
    return mockasync(questions)
  },
  add_answers (answers) {
    return mockasync(answers)
  }
}
