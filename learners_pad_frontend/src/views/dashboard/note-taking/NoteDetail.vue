<template>
  <div>
    <div>
      <!-- small menu to go to all the notes -->
      <div class="my-4 text-lg font-medium py-4 px-3">
        <router-link
          :to="{ name: 'NoteTaking' }"
          class="align-middle text-blue-400 font-medium hover:text-blue-500"
          ><font-awesome-icon :icon="['fas', 'angle-double-left']" /> all
          lists</router-link
        >
      </div>

      <!-- current note detail -->
      <div class="flex justify-around">
        <div class="md:4/5 lg:w-3/5 bg-gray-200 p-5 lg:p-10 rounded-md">
          <!-- TODO - Add a menu to delete, update this note -->
          <!-- the notes content -->
          <h2
            class="font-extrabold text-2xl text-center text-gray-800 mt-3 mb-2"
          >
            This will have the title of the note
          </h2>
          <p class="font-medium text-sm text-gray-700 text-right">7/6/2021</p>
          <p class="my-3 tracking-wider">
            There are many variations of passages of Lorem Ipsum available, but
            the majority have suffered alteration in some form, by injected
            humour, or randomised words which don't look even slightly
            believable. If you are going to use a passage of Lorem Ipsum, you
            need to be sure there isn't anything embarrassing hidden in the
            middle of text. All the Lorem Ipsum generators on the Internet tend
            to repeat predefined chunks as necessary, making this the first true
            generator on the Internet. It uses a dictionary of over 200 Latin
            words, combined with a handful of model sentence structures, to
            generate Lorem Ipsum which looks reasonable. The generated Lorem
            Ipsum is therefore always free from repetition, injected humour, or
            non-characteristic words etc.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NoteDetail",

  data() {
    return {};
  },

  computed: {
    ...mapGetters(["notes"]),
  },
};
</script>
