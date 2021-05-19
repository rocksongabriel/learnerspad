import axios from "axios";
// import store from "@/store/index";

export const AUTH_HTTP_1 = axios.create({
  baseURL: "http://localhost:8000/",
});

// export const AUTH_HTTP_2 = axios.create({
//   baseURL: "http://localhost:8000/",
//   headers: {
//     Authorization: "Bearer " + store.getters.userAccessToken,
//   },
// });
