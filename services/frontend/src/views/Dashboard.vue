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
            <p>Computer's picks: <strong>{{ computedSeletced }} </strong></p>
            <button :disabled="finished" id="rock" @click="onChoice">rock</button>
            <button :disabled="finished" id="paper" @click="onChoice">paper</button>
            <button :disabled="finished" id="scissors" @click="onChoice">scissors</button>
            <p>your choice: {{ selected }}</p>

            <h2> {{ resultMessage }} </h2>
          </div>
        
        
        <div v-if="finished">
          <h1>{{ result }}</h1>
          <h2> You got {{ totalPoints }} points </h2>          
        </div>
        <button 
          class="btn btn-success"
          @click="startGame"
          >Start again
        </button>
      </div>
    
    </section>


    

  </div>
</template>

<script>
import { mapActions } from 'vuex';
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
      totalPoints: 0,
    };
  },
  created: function() {
    this.user = this.$store.getters.stateUser.full_name
  },
  methods: {    
    ...mapActions(['updateNote']),
    startGame () {
      console.log(this.$store.getters.stateUser.id)
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
      this.gamesPlayed ++
      this.game(this.computedSeletced, this.selected)      
    },
    async recordResult (totalPoints) {      
      // i should add poinst
      const userId = this.$store.getters.stateUser.id
      const score = this.viewScoreByUser(userId)
      console.log(score)
      try {
        let result = {
          userid: userId,
          points: totalPoints,
        };
        await this.updateNote(result);        
      } catch (error) {
        console.log(error);
      }
    },
    gameResult (){
      if (this.computerWon == 5) {
        this.totalPoints = 0
        this.result = "You lost this round"
        this.finished = true
      } else if (this.playerWon == 5) {
        this.result = "You are the winner!!"
        this.totalPoints = 10 - this.gamesPlayed
        this.finished = true
      }
      if (this.finished) {
        this.recordResult(this.totalPoint)
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
          console.log(this.resultMessage)
          this.resultMessage = "Computer won"
          console.log(this.resultMessage)
        } else {
          this.playerWon ++
          this.resultMessage == "You won!"
        }        
      }
      this.gameResult();
    },
  },
};
</script>