<template>
  <section class="postContent">
    <div class="goBack" v-on:click="goBack">
      <div class="arrow">&#8920;</div>
    </div>
    <div class="author">
      {{ post.author.username }}
      <span class="date">{{ formatDate(post.created) }}</span>
    </div>
    <div class="singlePostTitle">
      {{ post.title }}
    </div>
    <div class="singlePostContent">
      {{ post.content }}
    </div>
  </section>
</template>
<script>
import router from "../../router/index";
export default {
  name: "PostContent",
  props: {
    post: Object,
  },
  setup() {
    function formatDate(date) {
      const result = date.slice(0, 10);
      return result.slice(8, 10) + "-" + result.slice(5, 7) + "-" + result.slice(0, 4);
    }
    function goBack() {
      router.push("/");
    }
    return {
      goBack,
      formatDate,
    };
  },
};
</script>
