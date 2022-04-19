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
        <font-awesome-icon icon="fa-solid fa-user-secret" />
      </div>
      <div
      v-else
      >
      <h1>Round # {{ gamesPlayed }}</h1>
      <div>
        <p>Computer's picks: {{ computedSeletced }}</p>
        <button @click="selected = 'rock'">rock</button>
        <button @click="selected = 'paper'">paper</button>
        <button @click="selected = 'scissors'">scissors</button>
      </div>
      <button @click="play">play</button>
      <p>your choice: {{ selected }}</p>
      <div>{{ result }}</div>
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
    };
  },
  created: function() {
    this.user = this.$store.getters.stateUser.full_name
  },
  computed: {
    result() {
      const { computedSeletced, selected } = this;
      if (computedSeletced === selected) {
        return `it's a tie`;
      } else {
        if (
          (computedSeletced === "rock" && selected === "scissors") ||
          (computedSeletced === "paper" && selected === "rock") ||
          (computedSeletced === "scissors" && selected === "paper")
        ) {
          return "computer won";
        }
        return "player won";
      }
    },
  },
  methods: {
    startGame () {
      this.gamesPlayed = 1
    },
    play() {
      if (!this.selected) {
        return;
      }
      const computerChoiceIndex = Math.floor(Math.random() * choices.length);
      this.computedSeletced = choices[computerChoiceIndex];
    },
  },
};
</script>
