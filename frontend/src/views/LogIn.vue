<template>
  <div class="logIn-wrapper">
    <form @submit.prevent="logIn">
      <div class="message">{{ state.message }}</div>
      <div class="error" v-if="state.error">We cannot find your login in our database</div>
      <div class="singleInput">
        <label for="username">Username</label>
        <input id="username" type="text" v-model="state.credentials.username" />
      </div>
      <div class="singleInput">
        <label for="password">Password</label>
        <input id="password" type="password" v-model="state.credentials.password" />
      </div>
      <button class="signUp-button">Log in</button>
    </form>
  </div>
</template>
<script>
import { reactive } from "vue";
import { useStore } from "vuex";
export default {
  name: "LogIn",
  props: {
    message: {
      type: String,
    },
  },
  setup(props) {
    const store = useStore();
    const state = reactive({
      message: props.message,
      error: false,
      credentials: {
        username: "me_pro",
        password: "barcelona10",
      },
    });
    async function logIn() {
      const feedback = await store.dispatch("auth_module/login", state.credentials);
      if (feedback.result === "negative") {
        state.error = true;
        state.message = "";
      } else {
        location.reload();
      }
    }
    return {
      logIn,
      state,
    };
  },
};
</script>
