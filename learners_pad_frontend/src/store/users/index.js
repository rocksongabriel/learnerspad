import axios from "axios";

const state = {
  userData: {},
};

const actions = {
  async login({ commit }, form) {
    // log the user in
    let url = "http://localhost:8000/api/users/account/developer/login/"; // change this url and make it generic
    const res = await axios.post(url, form);

    // commit data to state
    commit("UPDATE_USER_DATA", res.data);

    console.log(res);
  },
};

const mutations = {
  UPDATE_USER_DATA(state, payload) {
    state.userData = payload;
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
