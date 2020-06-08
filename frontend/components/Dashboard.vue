<template>
  <v-container>
    <h1>Pesquisa de Opinião Política</h1>
    <br/><v-divider></v-divider><br/>
    <v-row>
      <v-col v-for="(chart, i) in chartsAll" :key="i" cols="12" lg="4" md="6" sm="12" xs="12">
        <v-card class="pa-2" outlined tile>
          <p class="text-center">{{chart.question}}</p>
          <doughnut-chart v-if="loaded" :chartdata="chart" :options="optionsAll" height="250"/>
        </v-card>
      </v-col>
    </v-row>
    <br/>
    <h2>Perguntas por Gênero</h2>
    <br/><v-divider></v-divider><br/>
    <v-row>
      <v-col v-for="(chart, i) in chartsGender" :key="i" cols="12" lg="6" md="12" sm="12" xs="12">
        <v-card class="pa-2" outlined tile>
          <p class="text-center">{{chart.question}}</p>
          <bar-chart v-if="loaded" :chartdata="chart.data" :options="optionsGender" height="250"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import BarChart from '~/components/BarChart.vue'
import DoughnutChart from '~/components/DoughnutChart.vue'

export default {
  props: ['dashboard'],
  components: { BarChart, DoughnutChart },
  data () {
    return {
      chartsAll: [],
      optionsAll: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {fontColor: '#FFF', usePointStyle: true, fontSize: 13}
        }
      },
      chartsGender: [],
      optionsGender: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {fontColor: '#FFF', usePointStyle: true, fontSize: 13}
        },
        scales: {
          xAxes: [{
            gridLines: {
              offsetGridLines: true
            }
          }]
        }
      },
      loaded: true
    }
  },
  created () {
    const backgroundColor = ['Blue', 'Red', 'Purple']
    // All questions
    const self = this
    this.dashboard.questions.forEach((q, i) => {
      self.chartsAll.push({
        question: q.question,
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor,
            borderColor: backgroundColor,
            hoverBackgroundColor: backgroundColor,
            borderWidth: 1
          }
        ]
      })
      self.dashboard.answers.forEach((a) => {
        if (q.id === a.question_id) {
          self.chartsAll[i].labels.push(a.answer)
          const total = self.dashboard.dashboard.reduce((sum, d) => {
            if ((d.questions[q.id] !== undefined) && (d.questions[q.id].answer === a.id)) {
              sum = sum + 1
            }
            return sum
          }, 0)
          self.chartsAll[i].datasets[0].data.push(total)
        }
      })
    })

    // Gender
    this.dashboard.questions.forEach((q, i) => {
      if (q.id !== 1) {
        let color = 0
        const genders_id = []
        self.chartsGender.push({question: q.question, data: {labels: [], datasets: []}})
        // Labels
        self.dashboard.answers.forEach((a) => {
          if (a.question_id === 1) {
            genders_id.push(a.id)
            self.chartsGender[i - 1].data.datasets.push({data: [], label: a.answer, backgroundColor: backgroundColor[color], hoverBackgroundColor: backgroundColor[color]})
            color = color + 1
          } else if (a.question_id === q.id) {
            self.chartsGender[i - 1].data.labels.push(a.answer.substring(0, 20))
          }
        })
        self.dashboard.answers.forEach((a) => {
          if (q.id === a.question_id) {
            genders_id.forEach((gender, x) => {
              const total = self.dashboard.dashboard.reduce((sum, d) => {
                if ((d.questions[q.id] !== undefined) && (d.questions[q.id].answer === a.id) && (d.questions[1].answer === gender)) {
                  sum = sum + 1
                }
                return sum
              }, 0)
              self.chartsGender[i - 1].data.datasets[x].data.push(total)
            })
          }
        })
      }
    })
  }
}
</script>

<style>
</style>
