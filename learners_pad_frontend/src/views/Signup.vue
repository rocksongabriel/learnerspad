<template>
  <div class="mt-12 md:mt-24">
    <form @submit.prevent class="flex justify-around">
      <div
        class="p-8 md:px-12 md:py-8 bg-white shadow-2xl w-4/5 md:w-3/5 lg:w-1/3"
      >
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
            :class="{
              'border-2 border-red-600':
                submitted && !$v.signupForm.username.required,
            }"
            type="text"
            name="username"
            id="username"
            v-model.trim="signupForm.username"
          />

          <!-- rendering errors -->
          <!-- frontend errors -->
          <p
            class="text-red-600 text-sm my-1"
            v-if="submitted && !$v.signupForm.username.required"
          >
            Username is required
          </p>
          <!-- server errors -->
          <div
            v-if="userErrorMessages['username']"
            class="flex flex-wrap w-full"
          >
            <div
              v-for="username_error in userErrorMessages['username']"
              :key="username_error"
            >
              <p class="text-sm text-red-600 my-1">{{ username_error }}</p>
            </div>
          </div>
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
            :class="{
              'border-2 border-red-600':
                submitted && !$v.signupForm.email.required,
            }"
          />
          <!-- rendering errors -->
          <!-- frontend errors -->
          <p
            class="text-red-600 text-sm"
            v-if="submitted && !$v.signupForm.email.required"
          >
            Email is required
          </p>
          <!-- server errors -->
          <div v-if="userErrorMessages['email']" class="flex flex-wrap w-full">
            <div
              v-for="email_error in userErrorMessages['email']"
              :key="email_error"
            >
              <p class="text-sm text-red-600 my-1">{{ email_error }}</p>
            </div>
          </div>
        </div>

        <!-- account type -->
        <div class="my-3">
          <label for="account_type" class="form-label-1">Account type</label>
          <div class="flex justify-around mt-2">
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
          <p
            class="text-red-600 text-sm"
            v-if="submitted && !$v.signupForm.user_type.required"
          >
            Account type is required
          </p>
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
            :class="{
              'border-2 border-red-600':
                (submitted && !$v.signupForm.password.required) ||
                (submitted && !$v.signupForm.password.minLength),
            }"
          />
          <!-- rendering errors -->
          <!-- frontend errors -->
          <p
            class="text-red-600 text-sm"
            v-if="submitted && !$v.signupForm.password.required"
          >
            Password is required
          </p>
          <p
            class="text-red-600 text-sm"
            v-if="submitted && !$v.signupForm.password.minLength"
          >
            Minimum length of password is
            {{ $v.signupForm.password.$params.minLength.min }}
          </p>
          <!-- server errors -->
          <div
            v-if="userErrorMessages['password']"
            class="flex flex-wrap w-full"
          >
            <div
              v-for="password_error in userErrorMessages['password']"
              :key="password_error"
            >
              <p class="text-sm text-red-600 my-1">{{ password_error }}</p>
            </div>
          </div>
        </div>

        <button class="form-btn-2" type="submit" @click="signup()">
          Signup
        </button>

        <div class="flex justify-around">
          <router-link class="text-blue-800 text-xl" :to="{ name: 'Login' }"
            >already having an account?</router-link
          >
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { required, email, minLength } from "vuelidate/lib/validators";
import { mapGetters } from "vuex";

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
  computed: {
    ...mapGetters(["userErrorMessages"]),
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

      this.submitted = true;
      this.$v.$touch();

      if (!this.$v.$error) {
        try {
          await this.$store.dispatch("signup", signupFormData);
        } catch (error) {
          console.log(error);
        }
      }
    },
    setDeveloperUserType() {
      this.signupForm.user_type = "developer"; // set user type

      // alter background colors of buttons
      // set background color on developer type button
      const developer_btn = document.getElementById("developer_type_btn");
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
  mounted() {
    this.signupForm.user_type = "student";
  },
};
</script>

<style scoped></style>
