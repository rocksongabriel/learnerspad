<template>
  <nav class="bg-gray-300 shadow-xl">
    <!-- outer containment -->
    <div class="py-2 px-2 md:px-10 flex justify-between w-full">
      <!-- logo -->
      <div><span class="font-bold text-lg md:text-xl">learnerspad</span></div>

      <!-- primary nav -->
      <!-- TODO - add avatar to the profile button -->
      <div>
        <button class="px-2 md:px-4 py-1 bg-blue-600 shadow-xl text-white">
          profile
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TopNavBar",
  data() {
    return {};
  },
};
</script>
