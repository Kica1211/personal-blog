<template>
  <router-link :to="{ path: `/singlePost/${post.pk}` }">
    <div class="author-date">
      <div class="author">{{ post.author.first_name }} {{ post.author.last_name }}</div>
      <div class="date">{{ formatDate(post.created) }}</div>
    </div>
    <div class="post-title">{{ post.title }}</div>
    <div class="post-content">
      {{ addDots(post.content) }}
      <span class="read-more" v-if="post.content.length > 500">Read more</span>
    </div>
  </router-link>
  <div class="rating-section">
    <div class="rating-item">
      <div class="info">
        {{ post.likedBy.length || 0 }} {{ post.likedBy.length == 1 ? "like" : "likes" }}
      </div>
      <button v-on:click="likePost">
        {{ post.likedBy.includes(user.pk) ? "Like" : "Unlike" }}
      </button>
    </div>
    <div class="rating-item">
      <div class="info">
        {{ post.comments.length || 0 }} {{ post.comments.length == 1 ? "comment" : "comments" }}
      </div>
      <button>Comment</button>
    </div>
  </div>
</template>
<script>
import { useStore } from "vuex";
export default {
  name: "HomeSinglePost",
  props: {
    post: Object,
  },
  setup(props) {
    const user = localStorage.getItem("user");
    const store = useStore();
    function formatDate(date) {
      const result = date.slice(0, 10);
      return result.slice(8, 10) + "-" + result.slice(5, 7) + "-" + result.slice(0, 4);
    }
    function addDots(word) {
      if (word.length > 500) {
        return word.slice(0, 500) + "...";
      } else {
        return word;
      }
    }
    function likePost() {
      const flag = !props.post.likedBy.includes(user.pk);
      store.dispatch("content_edit_module/likePost", props.post, flag);
    }
    return {
      addDots,
      formatDate,
      likePost,
      user,
    };
  },
};
</script>
