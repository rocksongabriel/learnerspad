import axios from "axios";

axios.defaults.baseURL = "http://192.168.43.29:8000/";

const jwtInterceptor = axios.create({});

jwtInterceptor.interceptors.request.use(
  (req) => {
    return req;
  },
  (error) => {
    return Response.reject(error);
  }
);

export default jwtInterceptor;

/*
  ! - Interceptor not working
  TODO - implement the token refresh logic
  TODO - add the request token header to some requests in the interceptor
*/