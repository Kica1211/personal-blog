<template>
  <div class="home-items-wrapper">
    <div class="homeSinglePost" v-for="post in state.posts" :key="post.pk">
      <HomeSinglePost :post="post" :user="state.user" @refreshPosts="getPosts" />
    </div>
  </div>
</template>
<script>
import { reactive, onBeforeMount } from "vue";
import axios from "axios";
import { API_ADDRESS } from "../../store/index";
import HomeSinglePost from "./HomeSinglePost";
import { useStore } from "vuex";
export default {
  name: "HomeContent",
  components: { HomeSinglePost },
  setup() {
    const store = useStore();
    const state = reactive({
      posts: [],
      user: JSON.parse(localStorage.getItem("user")),
    });
    function getPosts() {
      axios
        .get(`${API_ADDRESS}/api/posts-list/?expand=category,comments,likedBy,author`)
        .then((res) => (state.posts = res.data))
        .catch((err) => console.log(err));
    }
    async function userAuth() {
      const result = await store.dispatch("auth_module/localStorageAuthentication");
      return result;
    }
    onBeforeMount(() => {
      getPosts();
      const ifUserValidate = userAuth();
      if (!ifUserValidate) {
        state.user = {};
      }
    });
    return {
      state,
      getPosts,
    };
  },
};
</script>
