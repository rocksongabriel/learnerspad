/* eslint-disable */

import jwtInterceptor from "../../../http-common";
import router from "../../router";

const state = {
  loginResponseData: {}, // hold the initial data from login
  errorMessages: {}, // hold error messages
  userData: {},
};

const actions = {
  async login({ commit, dispatch }, form) {
    // log the user in
    let url = "api/users/account/login/";
    await jwtInterceptor.post(url, form)
      .then((res) => {
        // commit data to state
        commit("UPDATE_USER_LOGIN_DATA_RESPONSE", res.data);

        // fetch user data from api
        let payload = {
          "url": res.data["user_retrieve_url"],
          "access_token": res.data["token"]["access"]
        }
        dispatch("fetchUserData", payload);

        // redirect user to dashboard
        router.push({name: "Dashboard"})
      })
      .catch((error) => {
        commit("UPDATE_ERROR_MESSAGES", error.response.data);
      });
  },

  async fetchUserData({ commit }, payload) {
    let url = payload["url"]
    await jwtInterceptor.get(url, {
      headers: {
        "Authorization": `Bearer ${payload["access_token"]}`
      }}).then(
      (res) => {
        // commit the user data to state
        commit("UPDATE_USER_DATA", res.data);
      }
    ).catch((error) => {
      commit("UPDATE_ERROR_MESSAGES", error.response.data);
    })
  },

  async signup({ commit, dispatch }, data) {
    let user_type = data.get("user_type");
    console.log(user_type);
    let url = `api/users/account/${user_type}/create/`
    await jwtInterceptor.post(url, data).then((res) => {
      // print data to console
      console.log(res.data)
      console.log(res);
      if (res.status === 201) {
          // log the user in
          let form = new FormData();
          form.set("username", data.get("username"));
          form.set("password", data.get("password"));

          dispatch("login", form);
      }
    }).catch((error) => {
      commit("UPDATE_ERROR_MESSAGES", error.response.data);
    })
  },

  logout({ commit }) {
    commit("LOGOUT_USER");
    // push the person to the login page
    router.push({name: "Login"})
  },

  remove_user_error_messages({ commit }) {
    commit("REMOVE_ERROR_MESSAGES");
  }
};

const mutations = {
  UPDATE_USER_LOGIN_DATA_RESPONSE(state, payload) {
    state.errorMessages = {}; // set the errors to an empty object
    state.loginResponseData = payload;
  },
  UPDATE_ERROR_MESSAGES(state, payload) {
    state.loginResponseData = {}; // set the initial user data to an empty object
    state.userData = {};
    state.errorMessages = payload;
  },
  UPDATE_USER_DATA(state, payload) {
    state.errorMessages = {};
    state.userData = payload;
  },
  LOGOUT_USER(state) {
    state.loginResponseData = {};
    state.userData = {};
    localStorage.removeItem("vuex"); // remove vuex from local storage
  },
  REMOVE_ERROR_MESSAGES(state) {
    state.errorMessages = {};
  }
};

const getters = {
  userAccessToken: (state) => state.loginResponseData["token"]["access"],
  userRefreshToken: (state) => state.loginResponseData["token"]["refresh"],
  isAuthenticated: (state) => !!state.loginResponseData["token"],
  userRetrieveUrl: (state) => state.loginResponseData["user_retrieve_url"],
  user: (state) => state.userData,
  userErrorMessages: (state) => state.errorMessages,
};

const usersModule = {
  state,
  actions,
  mutations,
  getters,
};

export default usersModule;
