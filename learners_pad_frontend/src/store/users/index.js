/* eslint-disable */

import { AUTH_HTTP_1 } from "../../../http-common";
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
    await AUTH_HTTP_1.post(url, form)
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
    await AUTH_HTTP_1.get(url, {
      headers: {
        "Authorization": `Bearer ${payload["access_token"]}`
      }
    }).then(
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
    await AUTH_HTTP_1.post(url, data).then((res) => {
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
  }
};

const getters = {
  userAccessToken: (state) => state.loginResponseData["token"]["access"],
  userRefreshToken: (state) => state.loginResponseData["token"]["refresh"],
  isAuthenticated: (state) => !!state.loginResponseData["token"],
  userRetrieveUrl: (state) => state.loginResponseData["user_retrieve_url"],
};

const usersModule = {
  state,
  actions,
  mutations,
  getters,
};

export default usersModule;
