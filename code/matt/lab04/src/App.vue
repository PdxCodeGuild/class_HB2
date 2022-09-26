<script setup>
import { ref, computed, onMounted } from 'vue'

const wins = ref(0)
const losses = ref(0)
const draws = ref(0)

const choice = ref(null)
const computerChoice = ref(null)
const verdict = ref(null)

const outcomes = {
  rock: {
    rock: 'draw',
    paper: 'loss',
    scissors: 'win',
  },
  paper: {
    rock: 'win',
    paper: 'draw',
    scissors: 'loss',
  },
  scissors: {
    rock: 'loss',
    paper: 'win',
    scissors: 'draw',
  }
}

const winPercentage = computed(() => {
  const total = wins.value + draws.value + losses.value
  return total ? (wins.value / total) * 100 : 0
})

const play = c => {
  choice.value = c

  const choices = ['rock', 'paper', 'scissors']
  const random = Math.floor(Math.random() * choices.length)
  computerChoice.value = choices[random]

  const outcome = outcomes[c][computerChoice.value]

  if (outcome === 'win') {
    wins.value++
    verdict.value = 'You win'
  } else if (outcome === 'loss') {
    losses.value++
    verdict.value = 'You lose'
  } else {
    draws.value++
    verdict.value = 'It is a draw'
  }

  SaveGame()
}

const SaveGame = () => {
  localStorage.setItem('wins', wins.value)
  localStorage.setItem('losses', losses.value)
  localStorage.setItem('draws', draws.value)
}

const LoadGame = () => {
  wins.value = localStorage.getItem('wins')
  losses.value = localStorage.getItem('losses')
  draws.value = localStorage.getItem('draws')
}

const ResetRound = () => {
  choice.value = null
  computerChoice.value = null
  verdict.value = null
}

onMounted(() => {
  LoadGame()
  window.addEventListener('keypress', e => {
    if (e.key === 'r') {
      ResetRound()
    }
  })
})


</script>

<template>
  <h1>Hello, World</h1>
</template>


