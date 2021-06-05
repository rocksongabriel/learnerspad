<template>
  <div>
    <h1 class="text-center text-red-600 font-bold text-2xl">Notes</h1>

    <Editor />
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
    return {};
  },
};
</script>
