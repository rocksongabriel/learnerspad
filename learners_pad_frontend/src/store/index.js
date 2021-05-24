import Vue from "vue";
import Vuex from "vuex";
import usersModule from "@/store/users/index.js";
import createPersistedState from "vuex-persistedstate";
import SecureLS from "secure-ls";

var ls = new SecureLS({ encodingType: "aes", isCompression: false });

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    usersModule,
  },
  plugins: [
    createPersistedState({
      key: "learnerspad",
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      },
    }),
  ],
});
