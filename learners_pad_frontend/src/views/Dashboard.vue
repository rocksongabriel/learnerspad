<template>
  <div>
    <h1 class="font-bold text-black text-4xl">Dashboard</h1>
    <p>Welcome {{ user.username }}</p>
    <button
      class="
        bg-red-800
        text-2xl
        font-bold font-serif
        hover:bg-red-500
        text-white
        px-4
        py-2
        m-3
      "
      @click="logout()"
    >
      Log out
    </button>
  </div>
</template>

<script>
/* eslint-disable */
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Dashboard",
  data() {
    return {

    }
  },
  computed: {
    ...mapGetters(["user"]),
  },
  methods: {
    ...mapActions(["logout"])
  },
  created() {
    console.log(this.user);
  }
};
</script>

<style scoped></style>
