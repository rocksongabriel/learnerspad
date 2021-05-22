<template>
  <div class="p-8">
    <h1 class="font-bold text-5xl text-red-700">Signup</h1>

    <form @submit.prevent>
      <label for="username">Username</label> <br />
      <input
        class="border border-black p-2"
        type="text"
        name="username"
        id="username"
        v-model.trim="signupForm.username"
      />
      <br />

      <label for="email">Email</label> <br />
      <input
        class="border border-black p-2"
        type="email"
        name="email"
        id="email"
        v-model.trim="signupForm.email"
      />
      <br />

      <label for="password">Password</label> <br />
      <input
        class="border border-black p-2"
        type="password"
        name="password"
        id="password"
        v-model.trim="signupForm.password"
      />
      <br />
      <button
        class="my-2 mx-1 py-2 px-4 bg-blue-500 focus:bg-red-600 font-bold"
        @click="setUserType('student')"
      >
        Student
      </button>
      <button
        class="my-2 mx-1 py-2 px-4 bg-blue-500 focus:bg-red-600 font-bold"
        @click="setUserType('developer')"
      >
        Developer
      </button>
      <br /><br />
      <div class="flex">
        <button
          class="
            py-2
            justify-center
            px-4
            bg-green-600
            text-white
            font-bold
            hover:bg-black
            focus:bg-green-800
          "
          type="submit"
          @click="signup()"
        >
          Signup
        </button>
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
