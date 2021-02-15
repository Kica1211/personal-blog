<template>
  <div class="logout-wrapper">
    LOGOUT VIEW ES
    <div>are you sure you wanna logout?</div>
    <button v-on:click="logout">yes</button>
    <button v-on:click="goBack">no</button>
  </div>
</template>
<script>
import router from "../router/index";
import { useStore } from "vuex";
export default {
  name: "Logout",
  setup() {
    const store = useStore();
    async function logout() {
      store.dispatch("auth_module/logout");
    }
    function goBack() {
      router.push("/");
    }
    return {
      logout,
      goBack,
    };
  },
};
</script>
