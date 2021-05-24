<template>
  <div class="my-10">
    <form @submit.prevent class="flex justify-around">
      <div
        class="
          p-5
          bg-gray-200
          border border-gray-300
          drop-shadow-2xl
          w-4/5
          md:w-2/5
          lg:w-1/3
        "
      >
        <div class="flex justify-around my-2">
          <img
            src="../assets/avatar6.png"
            alt=""
            class="rounded-full"
            style="height: 80px; width: 80px"
          />
        </div>

        <h1 class="text-center text-2xl text-gray-600">Welcome Back</h1>

        <div class="my-2">
          <label for="username1" class="form-label-1">Username</label>
          <br />
          <input
            type="text"
            name="usrname"
            id="username1"
            class="form-input-1"
            v-model.trim="loginForm.username"
          />
        </div>

        <div class="my-2">
          <label for="password1" class="text-2xl font-bold text-gray-800"
            >Password</label
          >
          <br />
          <input
            type="password"
            name="password"
            id="password1"
            class="p-3 text-lg w-full border border-gray-900 focus:outline-none"
            v-model.trim="loginForm.password"
          />
        </div>

        <div class="my-2">
          <button class="form-btn-1" @click="login()">Login</button>
          <div class="flex justify-around">
            <router-link
              :to="{ name: 'Signup' }"
              class="text-blue-700 text-lg font-sans underline"
              >Create account</router-link
            >
            |
            <a href="#" class="text-blue-700 text-lg font-sans underline"
              >Forgot Password</a
            >
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async login() {
      let loginFormData = new FormData();
      loginFormData.set("username", this.loginForm.username);
      loginFormData.set("password", this.loginForm.password);

      try {
        await this.$store.dispatch("login", loginFormData);
        this.loginForm.username = "";
        this.loginForm.password = "";
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped></style>
