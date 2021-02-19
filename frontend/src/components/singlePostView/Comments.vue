<template>
  <section class="postComments">
    <div class="commentsTitle">Comments ({{ comments.length }})</div>
    <form
      @submit.prevent="addComment"
      class="newCommentForm"
      v-if="Object.keys(state.user).length !== 0"
    >
      <textarea class="newCommentContent" v-model="state.textAreaContent"></textarea>
      <button class="addCommentButton">Add Comment</button>
    </form>
    <div class="singleComment" v-for="comment in comments" :key="comment.pk">
      <div class="commentDetails">
        <div class="commentAuthor">{{ comment.username }}</div>
        <div class="commentDate">{{ formatAgoDate(comment.created) }} ago</div>
      </div>
      <div class="commentContent">
        {{ comment.content }}
      </div>
      <div class="commentLikes" v-if="Object.keys(state.user).length !== 0">
        <button class="likeComment">Like</button>{{ comment.liked_by.length }} likes
      </div>
    </div>
  </section>
</template>
<script>
import { reactive, onBeforeMount } from "vue";
import { useStore } from "vuex";
export default {
  name: "Comments",
  emits: ["refreshPost"],
  props: {
    comments: Object,
    pk: Number,
  },
  setup(props, { emit }) {
    const store = useStore();
    const state = reactive({
      user: JSON.parse(localStorage.getItem("user")),
      textAreaContent: "",
    });
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
    async function userAuth() {
      const result = await store.dispatch("auth_module/localStorageAuthentication");
      return result;
    }
    async function addComment() {
      const data = {
        content: state.textAreaContent,
        pk: props.pk,
      };
      await store.dispatch("content_edit_module/addComment", data);
      emit("refreshPost");
      state.textAreaContent = "";
    }
    onBeforeMount(() => {
      const ifUserValidate = userAuth();
      if (!ifUserValidate) {
        state.user = {};
      }
    });
    return {
      formatAgoDate,
      addComment,
      state,
    };
  },
};
</script>
