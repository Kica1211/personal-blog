<template>
  <div id="singlePostView-wrapper" v-if="Object.values(state.post).length">
    <PostContent :post="state.post" />
    <Comments :comments="state.post.comments" />
  </div>
</template>
<script>
import { reactive, onMounted } from "vue";
import { API_ADDRESS } from "../store/index";
import axios from "axios";
import { useRoute } from "vue-router";
import PostContent from "../components/singlePostView/PostContent";
import Comments from "../components/singlePostView/Comments";
export default {
  name: "SinglePostView",
  components: { PostContent, Comments },
  setup() {
    const route = useRoute();
    const state = reactive({
      post: {},
    });
    const postPk = route.params["postPk"];
    function getPost() {
      axios
        .get(`${API_ADDRESS}/api/post-detail/${postPk}/?expand=category,comments,likedBy,author`)
        .then((res) => (state.post = res.data[0]))
        .catch((err) => console.log(err));
    }
    onMounted(() => {
      getPost();
    });
    return {
      state,
    };
  },
};
</script>
