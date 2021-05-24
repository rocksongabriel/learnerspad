/* eslint-disable */

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "@/store/index";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "/login",
        name: "Login",
        component: () => {
          return import(/* webpackChunkName: "login" */ "../views/Login.vue");
        },
      },
      {
        path: "/signup",
        name: "Signup",
        component: () => {
          return import(/* webpackChunkName: "signup" */ "../views/Signup.vue");
        },
      },
    ]
  },
  
  {
    path: "/user/dashboard",
    name: "Dashboard",
    component: () => {
      return import(/* webpackChunkName: "dashboard" */ "../views/Dashboard");
    },
    meta: {
      requiresAuth: true,
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((x) => x.meta.requiresAuth);

  if (requiresAuth && !store.getters.isAuthenticated) {
    // if requires auth and current user data is not filled in the store
    next({ name: "Login" });
  } else {
    next();
  }
});

export default router;
