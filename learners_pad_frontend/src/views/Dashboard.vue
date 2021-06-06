<template>
  <div class="flex">
    <!-- side navigation bar -->
    <SideNavBar />

    <div class="w-full sm:ml-20">
      <!-- top navigation bar of the dashboard -->
      <TopNavBar class="" />

      <!-- working area of the dashboard -->
      <div class="px-2 md:px-8 py-4">
        <!-- the dashboard content will be here -->
        <div v-if="$route.name == 'Dashboard'">
          <transition
            enter-active-class="animate__animated animate__fadeIn"
            leave-active-class="animate__animated animate__fadeOut"
          >
            <div>This is the content of the dashboard</div>
          </transition>
        </div>

        <!-- child routes will be loaded here -->
        <div>
          <transition
            mode="out-in"
            enter-active-class="animate__animated animate__fadeIn animate__faster"
            leave-active-class="animate__animated animate__fadeOut animate__faster"
          >
            <router-view /><!-- load child routes here -->
          </transition>
        </div>
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
