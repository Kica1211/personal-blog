import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import basic from "./basic";
import user from './user'
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      title: "Home",
    },
  },
  ...basic,
  ...user,
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const DEFAULT_PAGE_NAME = "Home";
document.title = DEFAULT_PAGE_NAME;
router.beforeEach((to, from, next) => {
  let title = (to.matched[0].meta && to.matched[0].meta.title) || DEFAULT_PAGE_NAME;
  document.title = title;
  next();
});
export default router;
