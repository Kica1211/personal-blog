<template>
  <div class="Profile-wrapper" v-if="state.user.first_name">
    <div class="welcomeProfile">
      Welcome {{ state.user.first_name }} {{ state.user.last_name }} to your profile !
    </div>
    <div class="changeYourPersonalInfo">
      Change your personal info
    </div>
  </div>
</template>
<script>
import { onBeforeMount, reactive } from "vue";
import { API_ADDRESS } from "../store/index";
import axios from "axios";
export default {
  name: "Profile",
  setup() {
    const state = reactive({
      user: JSON.parse(localStorage.getItem("user")),
    });
    onBeforeMount(() => {
      axios.get(`${API_ADDRESS}/api/user-detail/${state.user.username}/`).then((res) => {
        state.user = res.data[0];
      });
    });
    return {
      state,
    };
  },
};
</script>
