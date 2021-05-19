<template>
  <div id="app" class="">
    <div id="nav">
      <router-link
        :to="{ name: 'Home' }"
        class="text-blue-700 text-lg font-sans underline"
        >Home</router-link
      >
      |
      <router-link
        :to="{ name: 'Signup' }"
        class="text-blue-700 text-lg font-sans underline"
        >Signup</router-link
      >
      |
      <router-link
        :to="{ name: 'Login' }"
        class="text-blue-700 text-lg font-sans underline"
        >Login</router-link
      >
      |
      <router-link
        :to="{ name: 'Dashboard' }"
        class="text-blue-700 text-lg font-sans underline"
        >Dashboard</router-link
      >
    </div>

    <router-view />
  </div>
</template>

<style></style>
