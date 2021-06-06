<template>
  <div>
    <!-- Display the notes lists and buttons -->
    <div v-if="$route.name == 'NoteTaking'">
      <!-- button to show or hide the editor -->
      <div class="my-3 space-x-3 flex justify-end">
        <button
          class="
            py-2
            px-4
            bg-blue-600
            hover:bg-blue-500
            text-black
            font-bold
            focus:outline-none
            rounded-lg
          "
          @click="show_editor = !show_editor"
          v-if="!show_editor"
        >
          Create New Note
        </button>
        <button
          class="
            py-2
            px-4
            bg-red-600
            hover:bg-red-500
            text-black
            font-bold
            focus:outline-none
            rounded-lg
          "
          @click="show_editor = !show_editor"
          v-else
        >
          Cancel
        </button>
      </div>

      <!-- The editor to add notes -->
      <transition
        enter-active-class="animate__animated animate__fadeIn"
        leave-active-class="animate__animated animate__fadeOut"
      >
        <div>
          <Editor v-if="show_editor" />
        </div>
      </transition>

      <!-- The notes that have been created -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 my-8 mb-32 md:mb-0">
        <div
          v-for="note in notes"
          :key="note.created"
          class="
            bg-gray-300
            p-4
            rounded-md
            shadow-xl
            transform
            hover:scale-105
            hover:bg-gray-800
            hover:text-gray-200
            cursor-pointer
          "
        >
          <router-link
            :to="{ name: 'NoteDetail', params: { title: note.title } }"
          >
            <div>
              <p class="font-bold text-xl">{{ note.title | truncate(40) }}</p>
              <p class="font-medium text-sm text-right">
                {{ note.created }}
              </p>
              <p
                class="pt-3"
                :inner-html.prop="note.content | truncate(200)"
              ></p>
            </div>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Route to show the note detail -->
    <div>
      <transition
        mode="out-in"
        enter-active-class="animate__animated animate__fadeIn"
        leave-active-class="animate__animated animate__fadeOut"
      >
        <router-view></router-view>
      </transition>
    </div>
  </div>
</template>

<script>
import Editor from "@/components/dashboard/note-taking/Editor.vue";
import { mapGetters } from "vuex";

export default {
  name: "NoteTaking",

  components: {
    Editor,
  },

  data() {
    return {
      show_editor: false,
    };
  },

  computed: {
    ...mapGetters(["notes"]),
  },

  filters: {
    truncate(value, limit) {
      if (value.length > limit) {
        value = value.substring(0, limit - 3) + " . . .";
      }
      return value;
    },
  },
};
</script>

<style scoped></style>
