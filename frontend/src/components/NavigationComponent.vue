<template>
  <header class="p-3 text-bg-dark text-end d-flex">
    <div>
      <router-link to="/" class="nav-link text-white"><img class="icon" src="https://www.svgrepo.com/show/452130/vue.svg" alt="/"></router-link>
    </div>
    <div class="container" style="display: flex; flex-direction: row; justify-content: flex-end;">
      <div class="text-end d-flex align-items-center justify-content-center" v-if="!auth">
        <router-link to="/login" class="btn btn-outline-light me-2">Login</router-link>
        <router-link to="/register" class="btn btn-warning">Register</router-link>
      </div>
    </div>
  </header>
</template>

<script>
import {computed} from "vue";
import axios from "axios";
import {useStore} from "vuex";
import router from "@/router";


export default {
  name: "NavigationComponent",
  setup() {
    const store = useStore();
    const auth = computed(() => store.state.auth);

    return {
      auth
    }
  }
}
</script>

<style scoped>
.icon {
  height: 50px;
}
</style>