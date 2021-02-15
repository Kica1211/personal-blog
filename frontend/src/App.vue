<template>
  <div class="app-wrapper">
    <MainNav />
    <main class="router-wrapper">
      <router-view />
    </main>
    <MainFooter />
  </div>
</template>
<script>
import MainNav from "./components/MainNav";
import MainFooter from "./components/MainFooter";
export default {
  name: "App",
  components: { MainNav, MainFooter },
};
</script>
