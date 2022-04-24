<template>
  <div align="center">
    <section>
      <h1>Rock-Paper-Scissors</h1>
      <br/>

      <p class="text-primary"> Rock beats scissors, scissors beat paper, paper beats rock. </p>
      <br/>
      <div id="welcome"
      v-if="gamesPlayed === 0"
      >
        <p>
          Race to 5 wins. Bonus points for fewer matches to reach 5
          wins using the formula 10 - # of matches. If computer gets 5
          wins first, you get zero points.
        </p>
        
        <h2>Good luck {{ user }}!</h2>
        <br/>
        <button 
        class="btn btn-success"
        @click="startGame"
        >Press to start
        </button>
        
      </div>
      <div
      v-else
      >
      
        <h1>Round # {{ gamesPlayed }}</h1>
        
          <table>
            <tr>
              <th>Computer</th>
              <th>{{ user }}</th>              
            </tr>
            <tr>
              <td>{{ computerWon }}</td>
              <td>{{ playerWon }}</td>
            </tr>            
          </table>
          <div :disabled="finished">
            <h1> {{finished}} </h1>
            <p>Computer's picks: <strong>{{ computedSeletced }} </strong></p>
            <button :disabled="finished" id="rock" @click="onChoice">rock</button>
            <button :disabled="finished" id="paper" @click="onChoice">paper</button>
            <button :disabled="finished" id="scissors" @click="onChoice">scissors</button>
            <p>your choice: {{ selected }}</p>

            <h2> {{ resultMessage }} </h2>
          </div>
        
        
        <div v-if="finished">
          <div>{{ result }}</div>
          <button 
          class="btn btn-success"
          @click="startGame"
          >Start again
          </button>
        </div>
      </div>
    
    </section>


    

  </div>
</template>

<script>
const choices = ["rock", "paper", "scissors"];
export default {
  name: 'Dashboard',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
      user: null,
      gamesPlayed: 0,
      playerWon: 0,
      computerWon: 0,
      selected: "",
      computedSeletced: "",      
      finished: false,
      resultMessage: "",
      result: "",
    };
  },
  created: function() {
    this.user = this.$store.getters.stateUser.full_name
  },
  watch: {
  },
  methods: {
    startGame () {
      this.gamesPlayed = 1
      this.playerWon = 0
      this.computerWon = 0
      this.selected = ""
      this.computedSeletced = ""
      this.finished = false
      this.resultMessage = ""
      this.result = ""
    },
    onChoice (e) {
      const computerChoiceIndex = Math.floor(Math.random() * choices.length)
      this.computedSeletced = choices[computerChoiceIndex]
      this.selected = e.currentTarget.id
      this.game(this.computedSeletced, this.selected)      
      this.gamesPlayed ++
      if (this.gamesPlayed == 10){
        this.finished = true
      }
    },    
    gameResult (){
      if (this.playerWon >= 5) {
        this.result = "You are the winner!!"
        this.finished = true
      } else if (this.computerWon == 5) {
        this.result = "You lost this round"
        this.finished = true
      }      
    },
    game(computedSeletced, selected) {
      if (computedSeletced === selected) {
        this.resultMessage = "it's a tie"
      } else {
        if (
          (computedSeletced === "rock" && selected === "scissors") ||
          (computedSeletced === "paper" && selected === "rock") ||
          (computedSeletced === "scissors" && selected === "paper")
        ) {
          this.computerWon ++
          this.resultMessage = "Computer won"
        }
        this.playerWon ++
        this.resultMessage == "You won!"
      }
      this.gameResult();
    },
  },
};
</script>
