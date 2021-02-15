<template>
  <nav id="mainNav">
    <div class="logo">
      <router-link :to="{ path: `/` }">
        logo here
      </router-link>
    </div>
    <div class="nav-menu" v-on:click="changeActive">menu</div>
    <div class="nav-links-wrapper" :class="state.activeClass">
      <router-link :to="{ path: `/` }">
        <div class="nav-link">Home</div>
      </router-link>
      <router-link :to="{ path: `/Gallery` }">
        <div class="nav-link">Gallery</div>
      </router-link>
      <router-link :to="{ path: `/Authors` }">
        <div class="nav-link">Authors</div>
      </router-link>
      <router-link :to="{ path: `/logIn` }" v-if="!state.loggedIn">
        <div class="nav-link">
          Log in
        </div>
      </router-link>

      <router-link :to="{ path: `/Profile` }" v-else>
        <div class="nav-link">Profile</div>
      </router-link>
      <router-link :to="{ path: `/signUp` }" v-if="!state.loggedIn">
        <div class="nav-link">
          Sign up
        </div>
      </router-link>
      <router-link :to="{ path: `/Logout` }" v-else>
        <div class="nav-link">Logout</div>
      </router-link>
    </div>
  </nav>
</template>
<script>
import { reactive, onBeforeMount } from "vue";
import { useStore } from "vuex";
export default {
  name: "MainNav",
  setup() {
    const store = useStore();
    const state = reactive({
      activeClass: "",
      loggedIn: true,
    });
    async function checkLoggedIn() {
      state.loggedIn = await store.dispatch("auth_module/deepAuthentication");
    }
    function changeActive() {
      if (!state.activeClass) {
        state.activeClass = "active";
      } else {
        state.activeClass = "";
      }
    }
    onBeforeMount(() => {
      checkLoggedIn();
    });
    return {
      state,
      changeActive,
    };
  },
};
</script>
