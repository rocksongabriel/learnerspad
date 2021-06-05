<template>
  <nav class="bg-gray-900 shadow-xl">
    <!-- outer containment -->
    <div class="flex justify-between py-4 px-2 md:px-8 w-full">
      <!-- logo -->
      <div>
        <router-link
          :to="{ name: 'Home' }"
          class="font-bold text-yellow-500 md:text-2xl"
          >learnerspad</router-link
        >
      </div>

      <!-- primary nav -->
      <!-- TODO - add avatar to the profile button -->
      <div>
        <p class="text-gray-100">
          Welcome
          <span class="font-bold text-lg text-gray-300">{{
            user.username
          }}</span>
        </p>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "TopNavBar",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["user"]),
  },
};
</script>
