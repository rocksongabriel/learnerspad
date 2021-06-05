import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";
import "./assets/tailwind.css";
import axios from "axios";
import {
  library
} from "@fortawesome/fontawesome-svg-core";
import {
  faGithub,
  faLinkedin,
  faTwitter,
  faDev,
} from "@fortawesome/free-brands-svg-icons";
import {
  faBell,
  faHome,
  faSpinner,
  faArrowRight,
  faGraduationCap,
} from "@fortawesome/free-solid-svg-icons";
import {
  faStickyNote,
  faCalendarCheck,
  faUser,
  faClock,
  faListAlt,
} from "@fortawesome/free-regular-svg-icons";
import {
  FontAwesomeIcon
} from "@fortawesome/vue-fontawesome";

library.add(faGithub, faLinkedin, faTwitter, faDev);
library.add(
  faBell,
  faStickyNote,
  faCalendarCheck,
  faUser,
  faClock,
  faListAlt,
  faHome,
  faSpinner,
  faArrowRight,
  faGraduationCap
);

Vue.component("font-awesome-icon", FontAwesomeIcon);

// register vuelidate
Vue.use(Vuelidate);

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.config.productionTip = false;

new Vue({
  router,
  store: store,
  render: (h) => h(App),
}).$mount("#app");