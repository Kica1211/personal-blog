import axios from "axios";
import { API_ADDRESS } from "../store/index";
export const refreshToken = async () => {
  try {
    const user = JSON.parse(localStorage.getItem("user"));
    const { access, refresh } = user;
    const options = {
      headers: {
        Authorization: `Bearer ${access}`,
      },
    };
    const data = {
      refresh,
    };
    const { data: feedback } = await axios.post(
      `${API_ADDRESS}/auth/login/refresh/`,
      data,
      options
    );
    user.access = feedback.access;
    user.refresh = feedback.refresh;
    localStorage.setItem("user", JSON.stringify(user));
    return "AUTHORIZED";
  } catch (e) {
    localStorage.setItem("user", JSON.stringify({}));
    return "UNAUTHORIZED";
  }
};
//
export const deepUserAuthorization = async (to, from, next) => {
  if (localStorageAuthentication()) {
    const response = await refreshToken();
    if (response === "AUTHORIZED") next();
    else next("/logIn");
  } else {
    next("/logIn");
  }
};
export const localStorageAuthentication = () => {
  try {
    const user = JSON.parse(localStorage.getItem("user"));
    let result = true;
    [["username", 1], ["pk", 0][("access", 67)], ["refresh", 67]].forEach((property) => {
      if (user[property[0]].length < property[1]) {
        result = false;
      }
    });
    if (!result) return false;
    else return true;
  } catch (e) {
    return false;
  }
};
export const unauthorized = (to, from, next) => {
  const user = localStorage.getItem("user");
  if (["{}", null].includes(user)) next();
  else next("/");
};
