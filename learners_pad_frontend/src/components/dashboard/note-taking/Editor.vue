<template>
  <div class="">
    <div class="">
      <input
        type="text"
        name=""
        id=""
        class="
          border-2 border-gray-300
          p-3
          mb-2
          focus:outline-none
          text-black
          font-bold
          w-full
        "
        placeholder="Title of Note ..."
      />
      <vue-editor
        v-model="content"
        :editor-toolbar="customToolbar"
        class="shadow-2xl border-none"
      />

      <!-- button to save note -->
      <button
        class="
          py-2
          px-4
          bg-gray-800
          hover:bg-gray-900
          my-2
          font-bold
          text-white
          rounded-lg
          focus:outline-none
        "
      >
        Add Note
      </button>
    </div>
  </div>
</template>

<script>
import { VueEditor } from "vue2-editor";

export default {
  name: "Editor",

  components: {
    VueEditor,
  },

  data() {
    return {
      title: "",
      content: "This is the content",
      customToolbar: [
        [{ header: [false, 1, 2, 3, 4, 5, 6] }],
        [{ color: [] }, { background: [] }],
        ["bold", "italic", "underline"],
        ["code"],
        [
          { align: "" },
          { align: "center" },
          { align: "right" },
          { align: "justify" },
        ],
        [{ list: "ordered" }, { list: "bullet" }, { list: "check" }],
        [{ script: "sub" }, { script: "super" }],
      ],
    };
  },
};
</script>

<style></style>
