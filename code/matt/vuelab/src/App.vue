<script setup>
import { ref, computed, onMounted } from 'vue'

// We use ref because it's mutable - i.e, you can assign new values to .value(which we'll do later)
// It is also reactive - i.e, any read operations to .value is tracked.
// We'll throw a value++ on there and instead of it being 0 once it's referenced it'll become 1 and so on
const wins = ref(0)
const losses = ref(0)
const draws = ref(0)

// the choice we choose
const choice = ref(null)
// the choice the computer chooses
const computerChoice = ref(null)
// The verdict that will display text on the screen
const verdict = ref(null)

// Now we're going to set outcomes equal to an object
const outcomes = {
  // If rock hits whatnot
  rock: {
    rock: 'draw',
    paper: 'loss',
    scissors: 'win',
  },
  // If paper hits whatnot
  paper: {
    rock: 'win',
    paper: 'draw',
    scissors: 'loss',
  },
  // If scissors hits whatnot
  scissors: {
    rock: 'loss',
    paper: 'win',
    scissors: 'draw',
  }
}

// equal to a computed value because we need to see changes
const winPercentage = computed(() => {
  // then we add up all of the games
  const total = wins.value + draws.value + losses.value
  // then we get our percentage value
  return total ? (wins.value / total) * 100 : 0 // just incase are game is at zero
})

// we're passing through our choice in here
const play = c => {
  choice.value = c

  // This is for our computer and it's choices
  const choices = ['rock', 'paper', 'scissors']
  // Random selction between the three choices that are presented on line 48
  const random = Math.floor(Math.random() * choices.length)
  // Then we do the final step which is assigning it to the computer player
  computerChoice.value = choices[random]

  // Now we give our outcome by going all the way back up and grabbing '''c''' then our '''computerchoice'''
  // who wins and who loses
  const outcome = outcomes[c][computerChoice.value]

  // if statements that will print out text
  if (outcome === 'win') {
    // adding to the value each time we win, lose, or draw
    wins.value++
    // if statements that will print out text
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

// saving the local storage
const SaveGame = () => {
  localStorage.setItem('wins', wins.value)
  localStorage.setItem('losses', losses.value)
  localStorage.setItem('draws', draws.value)
}

// set our local storage
const LoadGame = () => {
  wins.value = localStorage.getItem('wins')
  losses.value = localStorage.getItem('losses')
  draws.value = localStorage.getItem('draws')
}
//  set all the values to null because we set all values to soemthing that is unavailable
const ResetRound = () => {
  choice.value = null
  computerChoice.value = null
  verdict.value = null
}

// Then we throw this bad boy on for key presses
onMounted(() => {
  LoadGame()
  window.addEventListener('keypress', e => {
    // if the person clicks 'r' then we'll reset the round
    if (e.key === 'r') {
      ResetRound()
    }
  })
})


</script>
  
<template>
  <div class="bg-gray-700 text-white text-center min-j-screen flex flec-col">
    <header class="container mx-auto p-6">
      <h1 class="text-4xl font-bold"> Rock, Paper, Scissors</h1>
    </header>
  </div>

  <body>


    <main class="container mx-auto p-6 flex-1">
      <!-- This means we haven't made a choice yet -->
      <div v-if="choice === null" class="flex items-center justify-center -mx-6">

        <button @click="play('rock')" class="bg-white rounded-full shadow-lg w-64 p-12 mx-6 
          transition-colors duration-300 hover:bg-red-500">
          <img src="https://www.pngitem.com/pimgs/m/45-452491_rock-paper-scissors-rock-hd-png-download.png" alt="rock"
            class="w-full h-full">
        </button>

        <button @click="play('paper')" class="bg-white rounded-full shadow-lg w-64 p-12 mx-6 
          transition-colors duration-300 hover:bg-yellow-500">
          <img src="https://www.clipartmax.com/png/middle/428-4288895_rock-paper-scissors-sign.png" alt="paper"
            class="w-full h-full">
        </button>

        <button @click="play('scissors')" class="bg-white rounded-full shadow-lg w-64 p-12 mx-6 
          transition-colors duration-300 hover:bg-blue-500">
          <img src="https://www.kindpng.com/picc/m/83-830031_transparent-scissors-clip-art-icon-rock-paper-scissors.png"
            alt="scissors" class="w-full h-full">
        </button>
      </div>
      <div v-else>
        <div class="text-3xl mb-4">
          You picked <span class="text-blue-500">{{choice}}</span>
        </div>

        <div class="text-3xl mb-4">
          Computer picked <span class="text-red-500">{{computerChoice}}</span>
        </div>

        <div class="text-6xl mb-12">
          {{ verdict }}
        </div>

        <button @click="ResetRound" class="bg-gray-500 text-lg py-2 px-4">Reset</button>


      </div>
    </main>
  </body>


</template>
  
  <!-- They way we get this to begin with is in the following -->
  
  <!-- 1 -->
  <!-- npm create vite@latest . -- --template vue -->
  <!-- this gives us vs.code, public, src, .gitingnore, index.html, package.json, readme.md, vite.config.js -->
  
  <!-- 2 -->
  <!-- npm i -D tailwindcss postcss autoprefixer -->
  <!-- this gives us node_modules and package-lock.json -->
  
  <!-- 3 -->
  <!-- npx tailwindcss init -p -->
  <!-- this gives us postcss.config.js and tailwind.config.js -->
  
  <!-- 4 -->
  <!-- from there go into your src folder and create a new file called main.css -->
  <!-- Paste in @tailwind base; -->
  <!-- Paste in @tailwind components; -->
  <!-- Paste in @tailwind utilities; -->
  
  <!-- 5 -->
  <!-- from there go into your tailwind.config.js file -->
  <!-- inside of that file you'll see a ''' content: [], ''' -->
  <!-- go inside your [] (the square brackets and type this inside of it) -->
  <!-- [
    "./index.html",
    "./src/**/*.{vue}"
    ] -->
  
  <!-- 6 -->
  <!-- also inside of your src folder you can delete the components file and assets file-->
  
  <!-- 7 -->
  <!-- You can go inside of your App.vue file inside of your src folder and delete everything inside of your -->
  <!-- template block, your script block, and the entire style block itself(unlike in the other blocks where you) -->
  <!-- just deleted what was inside of them. -->
  
  <!-- 8 -->
  <!-- npm run dev -->
  
  <!-- 9 -->
  <!-- style will not look as intended, so go into your main.js file (located in your src folder) -->
  <!-- underneath the import App from ./App.vue, type this -->
  <!-- import './main,css' which will in return add your default -->
  
  <!-- 10 -->
  <!-- begin writing your JS code inside your App.vue -->
  