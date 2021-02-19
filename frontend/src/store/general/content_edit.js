import { API_ADDRESS } from "../index";
import axios from "axios";
import { refreshToken, localStorageAuthentication } from "../../router/_guards";
export const content_edit_module = {
  namespaced: true,
  actions: {
    async likePost(_, data) {
      const isAuthorizated = (await refreshToken()) && localStorageAuthentication();
      if (isAuthorizated) {
        try {
          const user = JSON.parse(localStorage.getItem("user"));
          const options = {
            headers: {
              Authorization: `Bearer ${user.access}`,
            },
          };
          if (data.flag) {
            axios.patch(`${API_ADDRESS}/api/post-like/${data.pk}/`, {}, options);
          } else {
            axios.patch(`${API_ADDRESS}/api/post-unlike/${data.pk}/`, {}, options);
          }
        } catch {
          console.log("error");
        }
      } else {
        localStorage.setItem("user", {});
        location.reload();
      }
    },
    async addComment(_, data) {
      const isAuthorizated = (await refreshToken()) && localStorageAuthentication();
      if (isAuthorizated) {
        try {
          const user = JSON.parse(localStorage.getItem("user"));
          const options = {
            headers: {
              Authorization: `Bearer ${user.access}`,
            },
          };
          const postData = {
            content: data.content,
            post: data.pk,
          };
          await axios.post(`${API_ADDRESS}/api/comment-create/`, postData, options);
        } catch {
          console.log("error");
        }
      } else {
        localStorage.setItem("user", {});
        location.reload();
      }
    },
  },
};
