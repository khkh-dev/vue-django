import { createStore, ActionContext } from 'vuex'

export default createStore({
  state: { // the state is immutable, and we can't change it directly
    auth: false,
  },
  getters: {},
  mutations: {
    // mutation create a new state and then change the actual state
    setAuthentication(state: {auth: boolean}, auth: boolean) {
      state.auth = auth;
    }
  },
  actions: { // when we create action, we commit changes to a mutation
    setAuthentication(context: ActionContext<any, any>, auth: boolean) {
      context.commit("setAuthentication", auth);
    },
  },
  modules: {},
})
