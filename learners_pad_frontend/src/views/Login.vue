<template>
  <div class="m-8">
    <h1 class="text-black text-4xl font-bold">Login</h1>
    <form @submit.prevent>
      <label for="username1">Username</label> <br />
      <input
        type="text"
        name="usrname"
        id="username1"
        class="border border-black p-2"
        v-model.trim="loginForm.username"
      />
      <br />

      <label for="password1">Password</label> <br />
      <input
        type="password"
        name="password"
        id="password1"
        class="border border-black p-2"
        v-model.trim="loginForm.password"
      />
      <br />

      <button class="px-4 py-2 m-3 bg-blue-900 text-white" @click="login()">
        Login
      </button>
      <div>
        <a href="#" class="text-blue-700 text-lg font-sans underline"
          >Create account</a
        >
        |
        <a href="#" class="text-blue-700 text-lg font-sans underline"
          >Forgot Password</a
        >
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
