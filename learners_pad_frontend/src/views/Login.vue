<template>
  <div class="mt-12 md:mt-32">
    <form @submit.prevent class="flex justify-around">
      <div class="p-8 bg-white shadow-2xl w-4/5 md:w-3/5 lg:w-1/3">
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

        <!-- rendering general errors -->
        <div class="my-3">
          <div v-for="error in userErrorMessages" :key="error">
            <p class="text-sm text-red-600 font-bold">{{ error }}</p>
            <p class="text-sm text-red-500">Check your username and password</p>
          </div>
        </div>

        <!-- username -->
        <div class="my-4">
          <label for="username1" class="form-label-1">Username</label>
          <input
            type="text"
            name="usrname"
            id="username1"
            class="form-input-1"
            :class="{
              'border-2 border-red-600':
                submitted && $v.loginForm.username.$invalid,
            }"
            @blur="$v.loginForm.username.$touch()"
            v-model.trim="loginForm.username"
          />
          <p
            class="text-sm text-red-600 my-1"
            v-if="submitted && $v.loginForm.username.$invalid"
          >
            Username is required
          </p>
        </div>

        <!-- password -->
        <div class="my-2">
          <label for="password1" class="form-label-1">Password</label>
          <input
            type="password"
            name="password"
            id="password1"
            class="form-input-1"
            :class="{
              'border-2 border-red-600':
                submitted && $v.loginForm.password.$invalid,
            }"
            v-model.trim="loginForm.password"
          />
          <p
            class="text-red-600 text-sm my-1"
            v-if="submitted && $v.loginForm.password.$invalid"
          >
            Password is required
          </p>
        </div>

        <div class="my-2">
          <button class="form-btn-1" @click="login()">Login</button>
          <div class="flex justify-around">
            <router-link
              :to="{ name: 'Signup' }"
              class="text-blue-800 text-xl mr-2"
              >Create account</router-link
            >
            |
            <a href="#" class="text-blue-800 text-xl ml-2">Forgot Password</a>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import { mapGetters } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      submitted: false,
    };
  },
  computed: {
    ...mapGetters(["userErrorMessages"]),
  },
  methods: {
    async login() {
      // set submitted to true
      this.submitted = true;
      this.$v.$touch();

      let loginFormData = new FormData();
      loginFormData.set("username", this.loginForm.username);
      loginFormData.set("password", this.loginForm.password);

      if (!this.$v.$error) {
        try {
          await this.$store.dispatch("login", loginFormData);
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
  validations: {
    loginForm: {
      username: { required },
      password: { required },
    },
  },
};
</script>

<style scoped></style>
