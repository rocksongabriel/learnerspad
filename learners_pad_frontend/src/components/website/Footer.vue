<template>
  <footer class="bg-gray-900 text-white mt-12">
    <!-- outer container -->
    <div class="pt-10 pb-2">
      <!-- inner containers -->

      <!-- contain the icons to your profiles -->
      <div
        class="
          flex
          justify-between
          md:justify-around
          text-3xl
          md:text-4xl
          py-4
          mx-2
          md:mx-10
          px-4
          border-b-4 border-purple-300
        "
      >
        <a href=""><font-awesome-icon :icon="['fab', 'github']" /></a>
        <a href=""><font-awesome-icon :icon="['fab', 'linkedin']" /></a>
        <a href=""> <font-awesome-icon :icon="['fab', 'twitter']" /></a>
        <a href=""><font-awesome-icon :icon="['fab', 'dev']" /></a>
      </div>

      <!-- Personal Projects -->
      <div class="my-10">
        <h1 class="text-center text-xl text-gray-500">
          Other Personal Projects
        </h1>
        <div class="flex justify-around my-2">
          <!-- individual personal project box -->
          <a
            href="#"
            class="
              text-bold text-gray-200 text-2xl
              border-2 border-gray-400
              p-3
              font-bold
              hover:bg-gray-400
              hover:text-black
              hover:border-gray-800
            "
          >
            my-clients-data
          </a>
        </div>
      </div>

      <!-- Information on me -->
      <div class="">
        <h1 class="text-center text-gray-200 font-bold text-2xl">
          Gabriel Rockson
        </h1>
        <p class="text-center text-lg font-thin text-gray-300">
          <span class="text-2xl">&copy;</span> Copyright 2021
        </p>
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
