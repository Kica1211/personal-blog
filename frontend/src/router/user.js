import Profile from "../views/Profile.vue";
import LogIn from "../views/LogIn.vue";
import Logout from "../views/Logout.vue";
import SignUp from "../views/SignUp.vue";
import { unauthorized, deepUserAuthorization } from "./_guards";
export default [
  {
    path: "/signUp",
    name: "SignUp",
    component: SignUp,
    meta: {
      title: "SignUp",
    },
    beforeEnter: unauthorized,
  },
  {
    path: "/logIn",
    name: "LogIn",
    component: LogIn,
    props: true,
    meta: {
      title: "LogIn",
    },
    beforeEnter: unauthorized,
  },
  {
    path: "/Profile",
    name: "Profile",
    component: Profile,
    meta: {
      title: "Profile",
    },
    beforeEnter: deepUserAuthorization,
  },
  {
    path: "/Logout",
    name: "Logout",
    component: Logout,
    meta: {
      title: "Logout",
    },
    beforeEnter: deepUserAuthorization,
  },
];
