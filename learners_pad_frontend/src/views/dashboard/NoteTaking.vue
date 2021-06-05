<template>
  <div>
    <h1 class="text-center text-red-600 font-bold text-2xl">Notes</h1>

    <div class="my-3 space-x-3 flex justify-end">
      <button
        class="
          py-2
          px-4
          bg-red-600
          hover:bg-red-700
          text-black
          font-bold
          rounded-lg
          animate__animated animate__zoomIn
        "
        v-if="show_editor"
      >
        Cancel</button
      ><button
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
      >
        Create New Note
      </button>
    </div>

    <Editor v-if="show_editor" />
  </div>
</template>

<script>
import Editor from "../../components/dashboard/note-taking/Editor";

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
};
</script>
