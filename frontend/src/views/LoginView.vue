<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <div class="form-floating">
        <input v-model="data.email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
      </div>

      <div class="form-floating">
        <input v-model="data.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Password</label>
      </div>

      <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
    </form>
  </main>
</template>

<script>
import axios from "axios";
import { reactive } from "vue";
import { useRouter } from "vue-router";
import store from "@/store";

export default {
  name: "LoginView",
  setup() {
    const data = reactive({
      email: "",
      password: ""
    });

    const router = useRouter();

    const submit = async () => {
      try {
        const response = await axios.post("https://hola2you.eu/api/login", data, {
          withCredentials: true
        });
        await store.dispatch("setAuthentication", true);
        axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.token}`;
        await router.push('/');
        localStorage.setItem("authorized", JSON.stringify(true));
      } catch (error) {
        await store.dispatch("setAuthentication", false);
        localStorage.setItem("authorized", JSON.stringify(false));
      }
    }

    return {
      data,
      submit
    };
  }
}
</script>

<style scoped>

</style>