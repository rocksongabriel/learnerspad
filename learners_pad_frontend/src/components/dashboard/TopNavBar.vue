<template>
  <nav class="bg-gray-300 shadow-xl">
    <!-- outer containment -->
    <div class="py-4 px-2 md:px-10 flex justify-between w-full">
      <!-- logo -->
      <div><span class="font-bold text-base md:text-xl">learnerspad</span></div>

      <!-- primary nav -->
      <!-- TODO - add avatar to the profile button -->
      <div>
        <button class="text-blue-900 font-bold">profile</button>
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
