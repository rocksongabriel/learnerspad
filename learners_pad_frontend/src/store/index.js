import Vue from "vue";
import Vuex from "vuex";
import usersModule from "@/store/users/index.js";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    usersModule,
  },
  plugins: [createPersistedState()],
});
