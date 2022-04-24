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
        <div v-if="!finished">
          <p>Computer's picks: <strong>{{ computedSeletced }} </strong></p>
          <button id="rock" @click="onChoice">rock</button>
          <button id="paper" @click="onChoice">paper</button>
          <button id="scissors" @click="onChoice">scissors</button>
          <p>your choice: {{ selected }}</p>

          <h2> {{ resultMessage }} </h2>
        </div>
        
        <div v-else>
          <div>{{ result }}</div>
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
      selected: "",
      computedSeletced: "",
      finished: false,
      resultMessage: "",
    };
  },
  created: function() {
    this.user = this.$store.getters.stateUser.full_name
  },
  computed: {    
  },
  methods: {
    startGame () {
      this.gamesPlayed = 1
    },
    onChoice(e) {
      const computerChoiceIndex = Math.floor(Math.random() * choices.length);
      this.computedSeletced = choices[computerChoiceIndex];
      this.selected = e.currentTarget.id;
      this.gamesPlayed ++
      if (this.gamesPlayed === 10){
        this.finished = true
      } else {
        this.resultMessage = this.game(this.computedSeletced, this.selected);
      }
    },
    play() {      
      if (!this.selected) {        
        return;
      }
      const computerChoiceIndex = Math.floor(Math.random() * choices.length);
      this.computedSeletced = choices[computerChoiceIndex];
    },
    game(computedSeletced, selected) {

      if (computedSeletced === selected) {
        return "it's a tie"
      } else {
        if (
          (computedSeletced === "rock" && selected === "scissors") ||
          (computedSeletced === "paper" && selected === "rock") ||
          (computedSeletced === "scissors" && selected === "paper")
        ) {
          return "Computer won"
        }
        return "You won!"
      }
    },
  },
};
</script>
