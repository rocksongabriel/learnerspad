<template>
  <div class="flex">
    <!-- side navigation bar -->
    <!-- TODO - make the navbars mobile responsive -->
    <SideNavBar />

    <div class="w-full ml-20">
      <!-- top navigation bar of the dashboard -->
      <TopNavBar class="" />

      <!-- working area of the dashboard -->
      <div class="p-4">
        <h1 class="font-bold text-black text-4xl">Dashboard</h1>
        <p>Welcome {{ user.username }}</p>
        <p>Username: {{ user.username }}</p>
        <p>Id: {{ user.id }}</p>
        <p>Bio: {{ user.bio }}</p>
        <p>Account type: {{ user.type }}</p>
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

        <p class="text-lg font-thin text-gray-800">
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem laborum quos error sapiente quibusdam iste maxime
          asperiores repellat molestiae labore molestias dicta ipsum vitae atque
          repudiandae a, voluptates accusamus est. Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Minus atque minima perspiciatis impedit
          consectetur eveniet alias, maiores nemo animi accusamus. Fugiat,
          aperiam! Aut ratione natus voluptatum. Quisquam possimus voluptate
          doloribus. Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Aut aperiam ipsa in magni similique, debitis harum nesciunt et soluta
          beatae obcaecati temporibus quia dicta reiciendis natus aspernatur hic
          repudiandae earum. Lorem ipsum dolor sit amet, consectetur adipisicing
          elit. Beatae amet voluptates id, quas dignissimos voluptatibus
          distinctio illo consequuntur vero atque? Aperiam, ipsa. Cupiditate
          blanditiis eveniet officia, architecto dolorem consequatur alias?
        </p>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { mapActions, mapGetters } from "vuex";
import TopNavBar from "../components/dashboard/TopNavBar";
import SideNavBar from "../components/dashboard/SideNavBar";

export default {
  name: "Dashboard",
  data() {
    return {

    }
  },
  components: {
    TopNavBar,
    SideNavBar,
  },
  computed: {
    ...mapGetters(["user"]),
  },
  methods: {
    ...mapActions(["logout"])
  },
};
</script>

<style scoped></style>
