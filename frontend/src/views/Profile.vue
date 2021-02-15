<template>
  <div class="Profile-wrapper">
    <div class="welcomeProfile">Welcome @{{ state.username }} to your profile !</div>
  </div>
  <div class="changeYourPersonalInfo">
    Change your personal info
  </div>
</template>
<script>
import { reactive } from "vue";
export default {
  name: "Profile",
  setup() {
    const state = reactive({
      username: JSON.parse(localStorage.getItem("user")).username,
    });
    return {
      state,
    };
  },
};
</script>
