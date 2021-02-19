import { API_ADDRESS } from "../index";
import axios from "axios";
import { refreshToken, localStorageAuthentication } from "../../router/_guards";

export const auth_module = {
  namespaced: true,
  mutations: {},
  actions: {
    async createUser(_, credentials) {
      try {
        const { username, email, first_name, last_name, password, password2 } = credentials;
        const url = `${API_ADDRESS}/auth/register/`;
        const data = {
          username,
          email,
          first_name,
          last_name,
          password,
          password2,
        };
        await axios.post(url, data);
        return true;
      } catch {
        return false;
      }
    },
    async login(_, credentials) {
      const { username, password } = credentials;
      try {
        const { data: feedback } = await axios.post(`${API_ADDRESS}/auth/login/`, {
          username,
          password,
        });
        const { data: userDetail } = await axios.get(`${API_ADDRESS}/api/user-detail/${username}/`);
        const pk = userDetail[0].pk;
        const user = { username, pk, ...feedback };
        localStorage.setItem("user", JSON.stringify(user));
        return { result: "positive" };
      } catch {
        return { result: "negative" };
      }
    },
    async logout() {
      const user = JSON.parse(localStorage.getItem("user"));
      const url = `${API_ADDRESS}/auth/logout/`;
      const data = { refreshToken: user.refresh };
      const options = {
        headers: {
          Authorization: `Bearer ${user.access}`,
        },
      };
      await axios.post(url, data, options);

      localStorage.setItem("user", JSON.stringify({}));
      location.reload();
    },
    async refreshToken() {
      return await refreshToken();
    },
    async localStorageAuthentication() {
      return localStorageAuthentication();
    },
    async deepAuthentication() {
      return localStorageAuthentication() && (await refreshToken()) === "AUTHORIZED";
    },
  },
};
