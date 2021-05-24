<template>
  <nav class="bg-gray-600">
    <!-- container for nav -->
    <div class="flex justify-between py-2 px-2 md:px-10 w-full">
      <div class="flex items-center space-x-7">
        <!-- logo -->
        <div class="font-bold font-sans text-2xl text-gray-900">
          LearnersPad
        </div>

        <!-- primary nav -->
        <div class="space-x-3 text-2xl text-gray-700 hidden md:flex">
          <router-link class="hover:text-gray-900" :to="{ name: 'Home' }"
            >home</router-link
          >
          <router-link class="hover:text-gray-900" :to="{ name: 'Features' }"
            >features</router-link
          >
        </div>
      </div>

      <!-- secondary nav -->
      <div class="flex items-center space-x-3 text-2xl text-gray-800">
        <router-link
          class="hover:text-gray-900 hidden md:flex"
          :to="{ name: 'Login' }"
          >login</router-link
        >
        <router-link
          class="
            bg-blue-800
            hover:bg-blue-700
            py-2
            px-2
            rounded
            shadow-md
            text-white
            hover:text-gray-200
          "
          :to="{ name: 'Signup' }"
          >signup</router-link
        >
        <!-- mobile nav button -->
        <div class="space-y-1.5 cursor-pointer md:hidden" @click="toggleMenu()">
          <div class="h-1 w-8 bg-black"></div>
          <div class="h-1 w-8 bg-black"></div>
          <div class="h-1 w-8 bg-black"></div>
        </div>
      </div>
    </div>

    <!-- Mobile nav -->
    <div
      class="px-1 hidden space-y-3 text-2xl md:hidden bg-gray-200 mobile-menu"
    >
      <router-link
        class="hover:text-gray-900 hover:bg-gray-300 p-2"
        :to="{ name: 'Home' }"
        @click.native="toggleMenu()"
        >home</router-link
      >
      <router-link
        class="hover:text-gray-900 hover:bg-gray-300 p-2"
        :to="{ name: 'Features' }"
        @click.native="toggleMenu()"
        >features</router-link
      >
      <router-link
        class="hover:text-gray-900 hover:bg-gray-300 p-2"
        :to="{ name: 'Login' }"
        @click.native="toggleMenu()"
        >login</router-link
      >
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {};
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
