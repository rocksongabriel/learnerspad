<template>
  <nav
    class="bg-gray-500 w-full md:w-56 overflow-y-visible"
    style="height: 100vh"
  >
    <!-- outer container -->
    <div class="space-y-5">
      <!-- user avatar and name -->
      <div class="flex justify-around p-4 w-full bg-gray-400">
        <div class="">
          <img
            class="rounded-full bg-white"
            src="../../assets/avatar6.png"
            alt=""
            style="height: 100px; width: 100px"
          />
          <p class="py-2 text-lg font-sans text-black">username here</p>
        </div>
      </div>

      <!-- main navigation -->
      <div class="flex flex-col text-center">
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
        <router-link
          class="px-4 py-2 hover:bg-gray-800 text-gray-900 font-bold hover:text-white text-xl"
          :to="{ name: 'Home' }"
          >Menu Item
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "SideNavBar",
  data() {
    return {};
  },
};
</script>
