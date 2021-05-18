import axios from "axios";

export const AUTH_HTTP = axios.create({
  baseURL: "http://localhost:8000/",
});
