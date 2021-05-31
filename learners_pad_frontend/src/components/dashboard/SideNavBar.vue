<template>
  <div>
    <nav class="navbar">
      <!-- menu items -->
      <ul class="nabar-nav">
        <li class="nav-item">
          <a href="#"
            ><font-awesome-icon :icon="['far', 'list-alt']" /><span
              class="link-text"
            >
              Note Taking</span
            ></a
          >
        </li>
        <li class="nav-item">
          <a href="#"
            ><font-awesome-icon :icon="['far', 'sticky-note']" />
            <span class="link-text">Flashcards</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#"
            ><font-awesome-icon :icon="['far', 'calendar-check']" />
            <span class="link-text">Timetables</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#"
            ><font-awesome-icon :icon="['far', 'clock']" />
            <span class="link-text">Time Tracking</span></a
          >
        </li>
        <li class="nav-item">
          <a href="#"
            ><font-awesome-icon :icon="['fas', 'bell']" />
            <span class="link-text">Repeatitive Reminders</span></a
          >
        </li>
        <li class="nav-item mt-auto">
          <a href="#"
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

</style>
 