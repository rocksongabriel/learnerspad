import { AUTH_HTTP } from "../../../http-common";

const state = {
  userData: {}, // hold the initial data from login
  errorMessages: {}, // hold error messages
};

const actions = {
  async login({ commit }, form) {
    // log the user in
    let url = "api/users/account/login/";
    await AUTH_HTTP.post(url, form)
      .then((res) => {
        // commit data to state
        commit("UPDATE_USER_DATA", res.data);
      })
      .catch((error) => {
        commit("UPDATE_ERROR_MESSAGES", error.response.data);
      });
  },
};

const mutations = {
  UPDATE_USER_DATA(state, payload) {
    state.errorMessages = {}; // set the errors to an empty object
    state.userData = payload;
  },
  UPDATE_ERROR_MESSAGES(state, payload) {
    state.userData = {}; // set the initial user data to an empty object
    state.errorMessages = payload;
  },
};

const getters = {};

const usersModule = {
  state,
  actions,
  mutations,
  getters,
};

export default usersModule;
