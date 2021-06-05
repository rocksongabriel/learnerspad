<template>
  <div>
    <vue-editor v-model="content" />
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
    };
  },
};
</script>
