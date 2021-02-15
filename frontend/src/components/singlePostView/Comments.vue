<template>
  <section class="postComments">
    <div class="commentsTitle">Comments ({{ comments.length }})</div>
    <div class="singleComment" v-for="comment in comments" :key="comment.pk">
      <div class="commentDetails">
        <div class="commentAuthor">{{ comment.username }}</div>
        <div class="commentDate">{{ formatAgoDate(comment.created) }} ago</div>
      </div>
      <div class="commentContent">
        {{ comment.content }}
      </div>
      <div class="commentLikes">
        <button class="likeComment">Like</button>{{ comment.liked_by.length }} likes
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "Comments",
  props: {
    comments: Object,
  },
  setup() {
    function formatAgoDate(date) {
      const dateSeconds = new Date(date).getTime();
      const seconds = Math.floor((new Date() - dateSeconds) / 1000);
      let interval = seconds / 31536000;
      if (interval > 1) {
        return Math.floor(interval) + " years";
      }
      interval = seconds / 2592000;
      if (interval > 1) {
        return Math.floor(interval) + " months";
      }
      interval = seconds / 86400;
      if (interval > 1) {
        return Math.floor(interval) + " days";
      }
      interval = seconds / 3600;
      if (interval > 1) {
        return Math.floor(interval) + " hours";
      }
      interval = seconds / 60;
      if (interval > 1) {
        return Math.floor(interval) + " minutes";
      }
      return Math.floor(seconds) + " seconds";
    }
    return {
      formatAgoDate,
    };
  },
};
</script>
