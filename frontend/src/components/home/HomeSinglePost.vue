<template>
  <router-link :to="{ path: `/singlePost/${post.pk}` }">
    <div class="author-date">
      <div class="author">{{ post.author.first_name }} {{ post.author.last_name }}</div>
      <div class="date">{{ formatDate(post.created) }}</div>
    </div>
    <div class="post-title">{{ post.title }}</div>
    <div class="post-content">
      {{ post.content.length > 500 ? post.content.slice(0, 500) + "..." : post.content }}
      <span class="read-more" v-if="post.content.length > 500">Read more</span>
    </div>
  </router-link>
  <div class="rating-section">
    <div class="rating-item">
      <div class="info">
        {{ post.likedBy.length || 0 }} {{ post.likedBy.length == 1 ? "like" : "likes" }}
      </div>
      <button v-on:click="likePost" v-if="Object.keys(user).length !== 0 && user !== null">
        Like
      </button>
    </div>
    <div class="rating-item">
      <div class="info">
        {{ post.comments.length || 0 }} {{ post.comments.length == 1 ? "comment" : "comments" }}
      </div>
      <router-link
        :to="{ path: `/singlePost/${post.pk}` }"
        v-if="Object.keys(user).length !== 0 && user !== null"
      >
        <button>Comment</button>
      </router-link>
    </div>
  </div>
</template>
<script>
import { useStore } from "vuex";
export default {
  name: "HomeSinglePost",
  emits: ["refreshPosts"],
  props: {
    post: Object,
    user: Object,
  },
  setup(props, { emit }) {
    const store = useStore();
    function formatDate(date) {
      const result = date.slice(0, 10);
      return result.slice(8, 10) + "-" + result.slice(5, 7) + "-" + result.slice(0, 4);
    }

    async function likePost() {
      let flag = true;
      Object.values(props.post.likedBy).forEach((item) => {
        if (item.pk === props.user.pk) {
          flag = false;
        }
      });
      const data = {
        flag,
        pk: props.post.pk,
      };
      await store.dispatch("content_edit_module/likePost", data);
      emit("refreshPosts");
    }
    return {
      formatDate,
      likePost,
    };
  },
};
</script>
