<template>
  <div>
    <nav class="navbar">
      <!-- menu items -->
      <ul class="navbar-nav">
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['fas', 'home']" /><span
              class="link-text"
            >
              Dashboard</span
            ></a
          >
        </li>
        <hr class="hidden md:block border-2 border-gray-500 w-full">
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['far', 'list-alt']" />
            <span class="link-text">Note Taking</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['far', 'sticky-note']" />
            <span class="link-text">Flashcards</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['far', 'calendar-check']" />
            <span class="link-text">Timetables</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['far', 'clock']" />
            <span class="link-text">Time Tracking</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['fas', 'bell']" />
            <span class="link-text">Repeatitive Reminders</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link"
            ><font-awesome-icon :icon="['far', 'user']" />
            <span class="link-text">Profile</span></a
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

.navbar {
  height: 100vh;
  width: 5rem;
  position: fixed;
  background: rgba(15, 22, 37);
  color: white;
  transition: width 200ms ease;
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

.navbar:hover {
  width: 16rem;
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
</style>
