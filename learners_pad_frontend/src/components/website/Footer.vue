<template>
  <footer class="bg-gray-900 text-white">
    <div
      class="
        flex
        justify-between
        py-8
        px-2
        flex-col
        md:flex-row
        text-center
        text-lg
      "
    >
      <!-- built by text -->
      <div class="flex items-center my-3 md:my-0 w-full justify-around">
        built with love: Gabriel Rockson
      </div>

      <!-- links -->
      <div class="flex flex-col my-3 md:my-0 w-full space-y-1">
        <a href="#">my website</a>
        <a href="#">my github</a>
        <a href="#">follow me</a>
      </div>

      <!-- links -->
      <div
        class="flex my-3 md:my-0 w-full space-y-1 items-center justify-around"
      >
        copyright &copy; 2021
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {};
  },
};
</script>
