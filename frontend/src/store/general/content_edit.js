import { API_ADDRESS } from "../index";
import axios from "axios";
export const content_edit_module = {
  namespaced: true,
  actions: {
    async likePost(_, post, flag) {
      try {
        const user = JSON.parse(localStorage.getItem("user"));
        const data = {
          title: post.title,
        };
        const options = {
          headers: {
            Authorization: `Bearer ${user.access}`,
          },
        };
        if (flag) {
          const feed = await axios.patch(`${API_ADDRESS}/api/post-like/${post.pk}/`, data, options);
          console.log(feed);
        } else {
          const feed2 = await axios.patch(
            `${API_ADDRESS}/api/post-unlike/${post.pk}/`,
            data,
            options
          );
          console.log(feed2);
        }
      } catch {
        console.log("cos sie zjebalo xd");
      }
    },
  },
};
