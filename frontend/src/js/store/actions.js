/**
 * All actions for our store.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/actions.js
 * @exports Object Actions
 */


export default {

    // state.state
    changeState({ commit }, state) {
        commit('changeState', state)
    },
    resetState({ commit }) {
        commit('resetState')
    },

    // state.isLoading
    loading({ commit }) {
        commit('loading')
    },
    loaded({ commit }) {
        commit('loaded')
    },

    // state.apiRequest
    setApiRequest({ commit }) {
        commit('setApiRequest')
    },
    resetApiRequest({ commit }) {
        commit('resetApiRequest')
    },

    // state.toast
    setToastData({ commit }, data) {
        commit('setToastData', data)
    },
    dismissToast({ commit }) {
        commit('dismissToast')
    },
    dismissToastComplete() {},
    
}