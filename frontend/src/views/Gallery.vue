<template>
  <div class="gallery-wrapper">
    Its gonna be styled soon
    <div class="singleImage" v-for="image in state.images" :key="image.pk">
      <div class="s-title">{{ image.title }}</div>
      <div class="s-image" v-bind:style="{ backgroundImage: `url(${image.image})fdsafd` }">
        {{ image.image }}
      </div>
    </div>
  </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import { useStore } from "vuex";
import axios from "axios";
export default {
  name: "Gallery",
  setup() {
    const state = reactive({
      images: [],
    });
    const store = useStore();
    const API_ADDRESS = store.state.API_ADDRESS;
    function getImages() {
      axios
        .get(`${API_ADDRESS}/api/images/`)
        .then((res) => (state.images = res.data))
        .catch((err) => console.log(err));
    }
    onMounted(() => {
      getImages();
    });
    return {
      state,
    };
  },
};
</script>
