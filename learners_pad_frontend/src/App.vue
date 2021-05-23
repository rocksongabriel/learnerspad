<template>
  <div id="app" class="">
    <Navbar />

    <router-view />
  </div>
</template>

<script>
/* eslint-disable */
import Navbar from "./components/website/Navbar";

import { mapGetters } from "vuex";
import router from "@/router/";

export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    Navbar,
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
