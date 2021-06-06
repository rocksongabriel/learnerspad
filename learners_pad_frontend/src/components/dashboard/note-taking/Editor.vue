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
        v-model="title"
      />
      <vue-editor
        v-model="content"
        :editor-toolbar="customToolbar"
        class="shadow-2xl border-none"
        placeholder="Enter the content of your note here ..."
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
        @click="add_note()"
      >
        Add Note
      </button>
    </div>
  </div>
</template>

<script>
import { VueEditor } from "vue2-editor";
import { mapActions } from "vuex";

export default {
  name: "Editor",

  components: {
    VueEditor,
  },

  data() {
    return {
      title: "",
      content: "",
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

  methods: {
    ...mapActions(["addNote"]),

    // this method will add a new note
    add_note() {
      let note = {
        title: this.title,
        created: `${new Date().toLocaleDateString()} - ${new Date().toLocaleTimeString()}`,
        content: this.content,
      };
      this.addNote(note);

      this.title = "";
      this.content = "";
    },
  },
};
</script>

<style></style>
