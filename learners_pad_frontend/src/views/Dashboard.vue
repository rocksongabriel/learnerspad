<template>
  <div class="flex">
    <!-- side navigation bar -->
    <!-- TODO - make the navbars mobile responsive -->
    <SideNavBar/>

    <div class="w-full">
      <!-- top navigation bar of the dashboard -->
      <TopNavBar />

      <!-- working area of the dashboard -->
      <div class="p-4">
        <h1 class="font-bold text-black text-4xl">Dashboard</h1>
        <p>Welcome {{ user.username }}</p>
        <p>Username: {{ user.username }}</p>
        <p>Id: {{ user.id }}</p>
        <p>Bio: {{ user.bio }}</p>
        <p>Account type: {{ user.type }}</p>
        <button
          class="
            bg-red-800
            text-2xl
            font-bold font-serif
            hover:bg-red-500
            text-white
            px-4
            py-2
            m-3
          "
          @click="logout()"
        >
          Log out
        </button>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { mapActions, mapGetters } from "vuex";
import TopNavBar from "../components/dashboard/TopNavBar";
import SideNavBar from "../components/dashboard/SideNavBar";

export default {
  name: "Dashboard",
  data() {
    return {

    }
  },
  components: {
    TopNavBar,
    SideNavBar,
  },
  computed: {
    ...mapGetters(["user"]),
  },
  methods: {
    ...mapActions(["logout"])
  },
};
</script>

<style scoped></style>
