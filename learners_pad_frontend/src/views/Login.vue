<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent>
      <label for="username1">Username</label> <br />
      <input type="text" name="usrname" id="username1" /> <br />

      <label for="password1">Password</label> <br />
      <input type="password" name="password" id="password1" /> <br />

      <button>Login</button>
      <div>
        <a href="#">Create account</a> | <a href="#">Forgot Password</a>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
};
</script>

<style scoped></style>
