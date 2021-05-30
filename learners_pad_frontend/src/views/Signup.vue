<template>
  <div class="mt-12 md:mt-24">
    <form @submit.prevent class="flex justify-around">
      <div class="p-8 md:px-12 md:py-8 bg-white shadow-2xl">
        <!-- The avatar -->
        <div class="flex justify-around my-2">
          <img
            src="../assets/avatar7.png"
            alt=""
            class="rounded-full bg-gray-200 p-2 shadow-xl"
            style="height: 60px; width: 60px"
          />
        </div>

        <!-- Welcome message -->
        <h1 class="text-gray-700 text-xl font-bold text-center">
          We are glad to have you
        </h1>

        <!-- username -->
        <div class="my-3">
          <label for="username" class="form-label-1">Username</label> <br />
          <input
            class="form-input-1"
            type="text"
            name="username"
            id="username"
            v-model.trim="signupForm.username"
          />
        </div>

        <!-- email -->
        <div class="my-3">
          <label for="email" class="form-label-1">Email</label> <br />
          <input
            class="form-input-1"
            type="email"
            name="email"
            id="email"
            v-model.trim="signupForm.email"
          />
        </div>

        <!-- account type -->
        <div class="my-3">
          <label for="account_type" class="form-label-1">Account type</label>
          <div class="flex justify-between mt-2">
            <button
              class="
                px-6
                py-2
                text-lg
                border-2 border-purple-600
                text-gray-900
                font-bold
                rounded-md
                hover:bg-purple-600
                bg-purple-600
                hover:text-white
              "
              id="student_type_btn"
              @click="setStudentUserType()"
            >
              Student
            </button>
            <button
              class="
                px-6
                py-2
                text-lg
                border-2 border-blue-600
                font-bold
                text-gray-900
                rounded-md
                hover:bg-blue-600
                hover:text-white
              "
              id="developer_type_btn"
              @click="setDeveloperUserType()"
            >
              Developer
            </button>
          </div>
        </div>

        <!-- password -->
        <div class="my-3">
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
import { required, email, minLength } from "vuelidate/lib/validators";

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
      submitted: false,
    };
  },
  validations: {
    signupForm: {
      username: { required },
      email: { required, email },
      password: {
        required,
        minLength: minLength(6),
      },
      user_type: { required },
    },
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
    setDeveloperUserType() {
      this.signupForm.user_type = "developer"; // set user type

      // alter background colors of buttons
      // set background color on developer type button
      const developer_btn = document.getElementById("developer_type_btn");
      console.log(developer_btn.classList);
      developer_btn.classList.add("bg-blue-600");

      // remove background color on student type button
      const student_btn = document.getElementById("student_type_btn");
      student_btn.classList.remove("bg-purple-600");
    },
    setStudentUserType() {
      this.signupForm.user_type = "student";

      // alter background colors of buttons
      // set background color on student type button
      const student_btn = document.getElementById("student_type_btn");
      student_btn.classList.add("bg-purple-600");

      // remove background color on developer type button
      const developer_btn = document.getElementById("developer_type_btn");
      developer_btn.classList.remove("bg-blue-600");
    },
  },
};
</script>

<style scoped></style>
