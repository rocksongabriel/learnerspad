import axios from "axios";
import store from "./src/store/index";

// export const AUTH_HTTP_1 = axios.create({
//   baseURL: "http://localhost:8000/",
// });

let jwtInterceptor = axios.create({
  baseURL: "http://localhost:8000/",
});

jwtInterceptor.interceptors.request.use((config) => {
  console.log(config);
  config.params = {name: "Gabriel"};
  console.log(config);
  console.log(store);
  return config;
});

export default jwtInterceptor;
