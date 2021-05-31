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

<style>

@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600;1,800&display=swap');

:root {
  font-size: 16px;
  font-family: 'Raleway', sans-serif;
}

body::-webkit-scrollbar {
  width: 0.8rem;
}

body::-webkit-scrollbar-track {
  background: #1e1e24;
}

body::-webkit-scrollbar-thumb {
  background: #6649b8;
}

</style>
