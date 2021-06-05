<template>
  <div>
    <nav class="navbar">
      <!-- menu items -->
      <ul class="navbar-nav">
        <li class="nav-item logo">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['fas', 'home']" /><span
              class="link-text"
            >
              Dashboard</span
            ></a
          >
        </li>
        <hr class="hidden sm:block border-2 border-gray-500 w-full" />
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'NoteTaking' }"
            ><font-awesome-icon :icon="['far', 'list-alt']" />
            <span class="link-text">Note Taking</span></router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'FlashCards' }" class="nav-link"
            ><font-awesome-icon :icon="['far', 'sticky-note']" />
            <span class="link-text">Flashcards</span></router-link
          >
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Timetables' }"
            ><font-awesome-icon :icon="['far', 'calendar-check']" />
            <span class="link-text">Timetables</span></router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'TimeTracking' }" class="nav-link"
            ><font-awesome-icon :icon="['far', 'clock']" />
            <span class="link-text">Time Tracking</span></router-link
          >
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Reminders' }"
            ><font-awesome-icon :icon="['fas', 'bell']" />
            <span class="link-text">Reminders</span></router-link
          >
        </li>
        <li class="nav-item cursor-pointer">
          <router-link :to="{ name: 'UserProfile' }" class="nav-link"
            ><font-awesome-icon :icon="['far', 'user']" />
            <span class="link-text">Profile</span></router-link
          >
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "SideNavBar",
  data() {
    return {};
  },
};
</script>

<style scoped>
:root {
  --transition-speed: 600ms;
  --primary-background: rgba(17, 24, 39);
  --secondary-background: rgba(15, 22, 37);
}

/* logo */
.logo {
  text-transform: uppercase;
  font-weight: 800;
}

.logo svg {
  color: white;
}

.navbar {
  width: 5rem;
  height: 100vh;
  position: fixed;
  background: rgba(15, 22, 37);
  color: white;
  transition: width 200ms ease;
  z-index: 99999;
}

.navbar-nav {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
}

.nav-item {
  width: 100%;
}

.nav-item:last-child {
  margin-top: auto;
}

.nav-link {
  display: flex;
  align-items: center;
  height: 4rem;
  color: #949494;
  text-decoration: none;
  filter: grayscale(100%) opacity(0.7);
  transition: 600ms;
}

.nav-link:hover {
  background: rgb(8, 11, 19);
  filter: grayscale(0%) opacity(1);
}

.nav-link svg {
  min-width: 2rem;
  margin: 0 1.5rem;
  font-size: 1.6rem;
}

.link-text {
  display: none;
  margin-left: 0.8rem;
}

.navbar:hover .link-text {
  display: block;
}

svg {
  color: #df49a6;
}

svg {
  transition: 600ms;
}

/* Large Screens */
@media only screen and (min-width: 640px) {
  .navbar {
    width: 5rem;
    height: 100vh;
    top: 0;
  }

  .navbar:hover {
    width: 16rem;
  }

  .navbar:hover .link-text {
    display: inline;
    transition: opacity 600ms;
  }
}

/* Small screens */
@media only screen and (max-width: 640px) {
  .navbar {
    bottom: 0;
    width: 100vw;
    height: 4rem;
  }

  .navbar-nav {
    flex-direction: row;
    justify-content: center;
  }

  .nav-link {
    justify-content: center;
  }

  .nav-link svg {
    min-width: 2rem;
    margin: 0 1.2rem;
    font-size: 1.3rem;
  }

  .navbar:hover .link-text {
    display: none;
  }
}

/* hide some of the icons on smaller screens */
@media only screen and (max-width: 499px) {
  .nav-item:last-child,
  .nav-item:nth-last-child(2) {
    display: none;
  }
}
@media only screen and (max-width: 379px) {
  .nav-item:nth-last-child(3) {
    display: none;
  }
}
</style>
