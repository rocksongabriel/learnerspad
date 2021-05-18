import Vue from "vue";
import Vuex from "vuex";
import usersModule from "@/store/users/index.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    usersModule,
  },
});
