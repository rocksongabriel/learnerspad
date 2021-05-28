<template>
  <div class="mt-12 md:mt-32">
    <form @submit.prevent class="flex justify-around">
      <div class="p-8 bg-white shadow-2xl">
        <!-- The avatar container -->
        <div class="flex justify-around my-2">
          <img
            src="../assets/avatar6.png"
            alt=""
            class="rounded-full bg-gray-200 p-2 shadow-xl"
            style="height: 60px; width: 60px"
          />
        </div>

        <!-- welcome message -->
        <h1 class="text-center text-2xl text-gray-700 font-bold">
          Welcome Back
        </h1>

        <!-- username -->
        <div class="my-4">
          <label for="username1" class="form-label-1">Username</label>
          <input
            type="text"
            name="usrname"
            id="username1"
            class="form-input-1"
            v-model.trim="loginForm.username"
          />
        </div>

        <!-- password -->
        <div class="my-2">
          <label for="password1" class="form-label-1">Password</label>
          <input
            type="password"
            name="password"
            id="password1"
            class="form-input-1"
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
