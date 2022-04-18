<template>
  <div align="center">
    <section>
      <h1>Rock-Paper-Scissors</h1>
      <br/>

      <p class="text-primary"> Rock beats scissors, scissors beat paper, paper beats rock. </p>
      <br/>
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
    </section>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
      user: null,
    };
  },
  created: function() {
    this.user = this.$store.getters.stateUser.full_name
  },
  methods: {
    startGame () {
      console.log('start')
    },
  },
};
</script>
