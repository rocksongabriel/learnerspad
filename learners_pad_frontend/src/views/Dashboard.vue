<template>
  <div class="flex">
    <!-- side navigation bar -->
    <!-- TODO - make the navbars mobile responsive -->
    <SideNavBar />

    <div class="w-full sm:ml-20">
      <!-- top navigation bar of the dashboard -->
      <TopNavBar class="" />

      <!-- working area of the dashboard -->
      <div class="px-2 md:px-8 py-4">
        <router-view />
        <!-- load child routes here -->
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
