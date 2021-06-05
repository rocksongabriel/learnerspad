<template>
  <div>
    <vue-editor
      v-model="content"
      :editor-toolbar="customToolbar"
      class="border-gray-300 shadow-xl"
    />

    <div>{{ content }}</div>
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
      content: "This is the content",
      customToolbar: [
        [{ header: [false, 1, 2, 3, 4, 5, 6] }],
        [{ color: [] }, { background: [] }],
        ["bold", "italic", "underline"],
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
