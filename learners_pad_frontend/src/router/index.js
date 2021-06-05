/* eslint-disable */

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "@/store/index";


Vue.use(VueRouter);

const routes = [{
    path: "/",
    name: "Home",
    component: Home,
    children: [{
        path: "/login",
        name: "Login",
        component: () => {
          return import( /* webpackChunkName: "login" */ "../views/Login.vue");
        },
      },
      {
        path: "/signup",
        name: "Signup",
        component: () => {
          return import( /* webpackChunkName: "signup" */ "../views/Signup.vue");
        },
      },
    ]
  },

  {
    path: "/user/dashboard",
    name: "Dashboard",
    component: () => {
      return import( /* webpackChunkName: "dashboard" */ "../views/Dashboard");
    },
    meta: {
      requiresAuth: true,
    },
    children: [{
        path: "profile",
        name: "UserProfile",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/Profile");
        }
      },
      {
        path: "note-taking",
        name: "NoteTaking",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/NoteTaking");
        }
      },
      {
        path: "flashcards",
        name: "FlashCards",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/FlashCards");
        }
      },
      {
        path: "reminders",
        name: "Reminders",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/Reminders");
        }
      },
      {
        path: "timetables",
        name: "Timetables",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/TimeTables");
        }
      },
      {
        path: "time-tracking",
        name: "TimeTracking",
        component: () => {
          return import( /* webpackChunkName: "dashboard" */ "../views/dashboard/TimeTracking");
        }
      }
    ]
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
    next({
      name: "Login"
    });
  } else {
    next();
  }
});

export default router;