import axios from "axios";
import store from "@/store";

axios.defaults.baseURL = 'https://hola2you.eu/api/';

const refreshToken = async () => {
    // gets new access token by request to refresh url
    // previously we've set refresh token in request cookie on the back-end side
    // during request we decode user's refresh token from his cookies to check db for this user's active refresh token
    // if it exists, we replace expired access token with the new one
    const response = await axios.post('https://hola2you.eu/refresh', {}, {withCredentials: true});
    return response.data.token
}

axios.interceptors.response.use(
    response => {
        return response;
    },
    async error => {
        const authorized = localStorage.getItem("authorized");

        if (authorized == "true" && (error.response.status == 401 || error.response.status == 403)) {
            const refresh_token = await refreshToken();
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + refresh_token;
            await store.dispatch("setAuthentication", true);
        }
    },
)