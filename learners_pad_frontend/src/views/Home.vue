<template>
  <div class="bg-gray-200">
    <!-- Navbar -->
    <Navbar />

    <!-- Content of the homepage -->
    <div class="mx-4 md:mx-8 lg:mx-16" v-show="$route.path == '/'">
      <font-awesome-icon icon="github" />
      <h1
        class="
          text-6xl
          font-bold font-sans
          md:text-8xl
          lg:text-9xl
          text-center
          py-4
          lg:py-10
        "
      >
        Wanna Learn Faster, Use LearnersPad to Achieve That
      </h1>
    </div>

    <!-- Website related content will be loaded here -->
    <div class="w-full" style="min-height: 80vh">
      <router-view />
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import Navbar from "../components/website/Navbar";
import Footer from "../components/website/Footer";

export default {
  name: "Home",
  components: {
    Navbar,
    Footer,
  },
};
</script>
