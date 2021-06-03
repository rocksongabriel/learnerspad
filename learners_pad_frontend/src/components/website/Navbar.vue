<template>
  <nav class="bg-gray-900 shadow-md">
    <!-- container for nav -->
    <div class="flex justify-between py-4 px-2 md:px-10 w-full">
      <div class="flex items-center space-x-7">
        <!-- logo -->
        <div class="text-white text-xl font-bold">
          Learners<span class="text-yellow-500 font-thin">Pad</span>
        </div>

        <!-- primary nav -->
        <div class="space-x-3 text-gray-300 hidden md:flex">
          <router-link class="hover:text-white" :to="{ name: 'Home' }"
            >home</router-link
          >
          <router-link class="hover:text-white" :to="{ name: 'Features' }"
            >features</router-link
          >
        </div>
      </div>

      <!-- secondary nav -->
      <!-- show this if the user is authenticated -->
      <div
        class="flex items-center space-x-3 text-gray-200"
        v-if="isAuthenticated"
      >
        <router-link
          class="
            p-2
            bg-blue-500
            hover:bg-blue-600
            text-black
            font-bold
            rounded-md
            shadow-lg
          "
          :to="{ name: 'Dashboard' }"
          >Dashboard<font-awesome-icon
            class="ml-2 text-gray-800 text-lg animate-pulse"
            :icon="['fas', 'arrow-right']"
        /></router-link>

        <!-- mobile nav button -->
        <!-- <div @click="toggleMenu()">
          <MobileNavButton />
        </div> -->
      </div>

      <!-- show this if the user is not authenticated -->
      <div class="flex items-center space-x-3 text-gray-300" v-else>
        <router-link
          class="hover:text-white hidden md:flex"
          :to="{ name: 'Login' }"
          >login</router-link
        >
        <router-link
          class="
            bg-green-500
            hover:bg-green-600
            py-2
            px-2
            rounded
            shadow-md
            text-gray-900
            hover:text-gray-800
            font-bold
          "
          :to="{ name: 'Signup' }"
          >signup</router-link
        >
        <!-- mobile nav button -->
        <div @click="toggleMenu()">
          <MobileNavButton />
        </div>
      </div>
    </div>

    <!-- Mobile nav -->
    <div
      class="
        px-1
        pb-2
        hidden
        space-y-3
        text-xl
        md:hidden
        bg-gray-900
        text-white
        mobile-menu
        text-center
      "
    >
      <hr class="border-2 border-gray-300" />
      <router-link
        class="hover:bg-gray-700 p-2"
        :to="{ name: 'Home' }"
        @click.native="toggleMenu()"
        >home</router-link
      >
      <router-link
        class="hover:bg-gray-700 p-2"
        :to="{ name: 'Features' }"
        @click.native="toggleMenu()"
        >features</router-link
      >
      <router-link
        class="hover:bg-gray-700 p-2 mb-2"
        :to="{ name: 'Login' }"
        @click.native="toggleMenu()"
        >login</router-link
      >
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";
import MobileNavButton from "../website/buttons/MobileNavButton";

export default {
  name: "Navbar",
  data() {
    return {};
  },
  components: {
    MobileNavButton,
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  methods: {
    toggleMenu() {
      const menu = document.querySelector(".mobile-menu");
      menu.classList.toggle("hidden");
      menu.classList.toggle("flex");
      menu.classList.toggle("flex-col");
    },
  },
};
</script>

<style scoped>
nav {
  font-family: "Open Sans", sans-serif;
}

.mobile-menu {
  transition: all 500ms ease;
}
</style>
