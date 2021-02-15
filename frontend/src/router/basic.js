import Gallery from "../views/Gallery.vue";
import Authors from "../views/Authors.vue";
import SinglePost from "../views/SinglePost.vue";
export default [
  {
    path: "/Gallery",
    name: "Gallery",
    component: Gallery,
    meta: {
      title: "Gallery",
    },
  },
  {
    path: "/Authors",
    name: "Authors",
    component: Authors,
    meta: {
      title: "Authors",
    },
  },
  {
    path: "/singlePost/:postPk",
    name: "SinglePost",
    component: SinglePost,
    meta: {
      title: "SinglePost",
    },
  },
];
