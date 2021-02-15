<template>
  <div class="home-items-wrapper" v-if="state.posts.length > 0">
    <div class="homeSinglePost" v-for="post in state.posts" :key="post.pk">
      <HomeSinglePost :post="post" />
    </div>
  </div>
  <div class="no-posts" v-else>
    No posted posts. Come back later!
  </div>
</template>
<script>
import { reactive, onBeforeMount } from "vue";
import axios from "axios";
import { API_ADDRESS } from "../../store/index";
import HomeSinglePost from "./HomeSinglePost";
export default {
  name: "HomeContent",
  components: { HomeSinglePost },
  setup() {
    const state = reactive({
      posts: [],
    });
    function getPosts() {
      axios
        .get(`${API_ADDRESS}/api/posts-list/?expand=category,comments,likedBy,author`)
        .then((res) => (state.posts = res.data))
        .catch((err) => console.log(err));
    }
    onBeforeMount(() => {
      getPosts();
    });
    return {
      state,
    };
  },
};
</script>
