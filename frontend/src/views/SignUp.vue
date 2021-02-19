<template>
  <div class="signUp-wrapper" @submit.prevent="signUp">
    <form>
      <div class="error" v-if="state.error">Please enter the valid data</div>
      <div class="singleInput">
        <label for="username">Username</label>
        <input id="username" type="text" v-model="state.credentials.username" />
      </div>
      <div class="singleInput">
        <label for="email">Email</label>
        <input id="email" type="email" v-model="state.credentials.email" />
      </div>
      <div class="singleInput">
        <label for="first_name">First Name</label>
        <input id="first_name" type="text" v-model="state.credentials.first_name" />
      </div>
      <div class="singleInput">
        <label for="last_name">Last Name</label>
        <input id="last_name" type="text" v-model="state.credentials.last_name" />
      </div>
      <div class="singleInput">
        <label for="password">Password</label>
        <input id="password" type="password" v-model="state.credentials.password" />
      </div>
      <div class="singleInput">
        <label for="confirm-password">Confirm password</label>
        <input id="confirm-password" type="password" v-model="state.credentials.password2" />
      </div>
      <button class="signUp-button">Join to us!</button>
    </form>
  </div>
</template>
<script>
import { reactive } from "vue";
import { useStore } from "vuex";
import router from "../router/index";
export default {
  name: "SignUp",
  setup() {
    const store = useStore();
    const state = reactive({
      error: false,
      credentials: {
        username: "",
        email: "",
        first_name: "",
        last_name: "",
        password: "",
        password2: "",
      },
    });
    async function signUp() {
      const feedback = await store.dispatch("auth_module/createUser", state.credentials);
      if (feedback) {
        router.push({ name: "LogIn", params: { message: "Now you can log in" } });
      } else {
        state.error = true;
      }
    }
    return {
      signUp,
      state,
    };
  },
};
</script>
