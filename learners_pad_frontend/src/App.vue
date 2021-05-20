<template>
  <div id="app" class="">
    <div id="nav">
      <router-link
        :to="{ name: 'Home' }"
        class="text-blue-700 text-lg font-sans underline"
        >Home</router-link
      >
      |
      <router-link
        :to="{ name: 'Signup' }"
        class="text-blue-700 text-lg font-sans underline"
        >Signup</router-link
      >
      |
      <router-link
        :to="{ name: 'Login' }"
        class="text-blue-700 text-lg font-sans underline"
        >Login</router-link
      >
      |
      <router-link
        :to="{ name: 'Dashboard' }"
        class="text-blue-700 text-lg font-sans underline"
        >Dashboard</router-link
      >
    </div>

    <router-view />
  </div>
</template>

<script>
/* eslint-disable */

import { mapGetters } from "vuex";
import router from "@/router/";

export default {
  name: "App",
  data() {
    return {};
  },
  computed: {
    ...mapGetters([
      "isAuthenticated",
    ])
  },
  mounted() {
    // automatically send the user to the dashboard if they  are logged in
    if (this.isAuthenticated) {
      if (this.$route.name !== "Dashboard") {
        router.push({name: "Dashboard"});
      }
    }
  }
};
</script>

<style></style>
