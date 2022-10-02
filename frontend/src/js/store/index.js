import { createStore } from 'vuex'

export default createStore({
  state: {
    test: "test",
  },
  getters: {
    test(state) {
      return state.test
    },
  },
  mutations: {
    test(state, test) {
      state.test = test
    },
  },
})