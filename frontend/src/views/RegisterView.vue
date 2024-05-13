<template>
  <main class="form-register w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please register</h1>

      <div class="form-floating">
        <input v-model="data.first_name" required class="form-control" placeholder="First Name">
        <label>First Name</label>
      </div>

      <div class="form-floating">
        <input v-model="data.last_name" required class="form-control" placeholder="Last Name">
        <label>Last Name</label>
      </div>

      <div class="form-floating">
        <input v-model="data.email" type="email" required class="form-control" placeholder="email@example.com">
        <label>Email address</label>
      </div>

      <div class="form-floating">
        <input v-model="data.password" type="password" required class="form-control" placeholder="Password">
        <label>Password</label>
      </div>

      <div class="form-floating">
        <input v-model="data.password_confirm" type="password" required class="form-control" placeholder="Password Confirm">
        <label>Password</label>
      </div>

      <button class="btn btn-primary w-100 py-2" type="submit">Submit</button>
    </form>
  </main>
</template>

<script lang="ts">
import axios from 'axios';
import { reactive } from "vue";
import { useRouter } from "vue-router";
import store from "@/store";

export default {
  name: "RegisterView",
  setup() {
    const data = reactive({
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      password_confirm: "",
    });

    const router = useRouter();

    const submit = async () => {
      try {
        await axios.post("https://hola2you.eu/api/register", data)
        await router.push("/login");
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