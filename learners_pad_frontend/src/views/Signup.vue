<template>
  <div class="my-10">
    <form @submit.prevent class="flex justify-around">
      <div
        class="
          p-5
          bg-gray-200
          border border-gray-300
          shadow-2xl
          w-4/5
          md:w-2/5
          lg:w-1/3
        "
      >
        <!-- The avatar -->
        <div class="flex justify-around my-2">
          <img
            src="../assets/avatar7.png"
            alt=""
            class="rounded-full bg-gray-200"
            style="height: 80px; width: 80px"
          />
        </div>

        <!-- Welcome message -->
        <h1 class="text-gray-600 text-2xl text-center">
          We are glad to have you
        </h1>

        <div class="my-2">
          <label for="username" class="form-label-1">Username</label> <br />
          <input
            class="form-input-1"
            type="text"
            name="username"
            id="username"
            v-model.trim="signupForm.username"
          />
        </div>

        <div class="my-2">
          <label for="email" class="form-label-1">Email</label> <br />
          <input
            class="form-input-1"
            type="email"
            name="email"
            id="email"
            v-model.trim="signupForm.email"
          />
        </div>

        <div class="my-2">
          <label for="password" class="form-label-1">Password</label> <br />
          <input
            class="form-input-1"
            type="password"
            name="password"
            id="password"
            v-model.trim="signupForm.password"
          />
        </div>

        <div class="">
          <button class="form-btn-2" type="submit" @click="signup()">
            Signup
          </button>

          <div class="flex justify-around">
            <router-link class="text-blue-800 text-xl" :to="{ name: 'Login' }"
              >already having an account</router-link
            >
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      signupForm: {
        username: "",
        email: "",
        password: "",
        user_type: "",
      },
    };
  },
  methods: {
    async signup() {
      let signupFormData = new FormData();
      signupFormData.set("username", this.signupForm.username);
      signupFormData.set("email", this.signupForm.email);
      signupFormData.set("password", this.signupForm.password);
      signupFormData.set("user_type", this.signupForm.user_type);

      try {
        await this.$store.dispatch("signup", signupFormData);
        this.signupForm.username = "";
        this.signupForm.email = "";
        this.signupForm.password = "";
        this.signupForm.user_type = "";
      } catch (error) {
        console.log(error);
      }
    },
    setUserType(type) {
      this.signupForm.user_type = type;
      console.log(this.signupForm.user_type);
    },
  },
};
</script>

<style scoped></style>
