<template>
  <nav class="bg-gray-700 w-48" style="height: calc(100vh - 60px)">
    <!-- outer container -->
    <div class="flex flex-col">
      <!-- user avatar and name -->
      <div class="h-36 bg-blue-400">
        <span>user avatar here</span> <br />
        <span>username here</span>
      </div>

      <!-- main navigation -->
      <div class="flex flex-col my-10">
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
        <router-link class="hover:bg-gray-800 hover:text-white py-3 pl-2" :to="{ name: 'Home' }">Menu Item </router-link>
      </div>

      <!-- logout button -->
      <div class="">
        <button class="px-4 py-2 bg-red-600 w-full text-xl font-thin">
          Logout
        </button>
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
