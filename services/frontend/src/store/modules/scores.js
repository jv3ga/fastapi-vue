import axios from 'axios';

const state = {
  scores: null,
  score: null
};

const getters = {
  stateScores: state => state.scores,
  stateScore: state => state.score,
};

const actions = {
  async createScore({dispatch}, score) {
    await axios.post('scores', score);
    await dispatch('getScores');
  },
  async getScores({commit}) {
    let {data} = await axios.get('scores');
    commit('setScores', data);
  },
  async viewScore({commit}, id) {
    let {data} = await axios.get(`score/${id}`);
    commit('setScore', data);
  },
  async viewScoreByUser({commit}, userId) {
    let {data} = await axios.get(`/score/by_user/${userId}`);
    commit('setScore', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateScore({}, score) {
    await axios.patch(`score/${score.id}`, score.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteScore({}, id) {
    await axios.delete(`score/${id}`);
  }
};

const mutations = {
  setScores(state, scores){
    state.scores = scores;
  },
  setScore(state, score){
    state.score = score;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
