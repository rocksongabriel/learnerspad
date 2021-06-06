<template>
  <div>
    <h1 class="text-center text-red-600 font-bold text-2xl">Notes</h1>

    <div class="my-3 space-x-3 flex justify-end">
      <transition
        enter-active-class="animate__animated animate__fadeInRightBig"
        leave-active-class="animate__animated animate__fadeOutRightBig"
      >
        <button
          class="
            py-2
            px-4
            bg-red-600
            hover:bg-red-700
            text-black
            font-bold
            rounded-lg
            focus:outline-none
          "
          v-if="show_editor"
          @click="show_editor = !show_editor"
        >
          Cancel
        </button>
      </transition>
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
      >
        Create New Note
      </button>
    </div>

    <transition
      enter-active-class="animate__animated animate__fadeInRightBig"
      leave-active-class="animate__animated animate__fadeOutRightBig"
    >
      <Editor v-if="show_editor" />
    </transition>
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

<style scoped></style>
