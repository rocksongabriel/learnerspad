<template>
  <div id="app" style="scroll-behavior: smooth">
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>
/* eslint-disable */

import { mapGetters, mapActions } from "vuex";
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
  methods: {
    ...mapActions(["remove_user_error_messages"]),
  },
  mounted() {
    // automatically send the user to the dashboard if they  are logged in
    // this works when an authenticated user tries to access the login page or the signup page
    // !-- this is not working, work on it
    if (this.isAuthenticated) {
      if (this.$route.name == "Login" || this.$route.name == "Signup") {
        if (this.$route.name !== "Dashboard") {
        router.push({name: "Dashboard"});
      }
      }
    }
  },
  created() {
    // remove the error messages
    this.remove_user_error_messages();
  }
};
</script>

<style></style>
