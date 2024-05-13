<template>
  <main class="d-flex flex-nowrap" style="height: 840px;" v-if="auth">
    <div class="d-flex flex-column flex-shrink-0 p-3 bg-body-tertiary" style="width: 300px;">
      <div class="menu-title fs-3">
        Home
      </div>
      <hr>
      <div class="menu-bar nav nav-pills flex-column mb-auto">
          <router-link to="/profile" class="btn btn-outline-dark" aria-current="page">
            Profile
          </router-link>
          <router-link to="/notes" class="btn btn-outline-dark" aria-current="page">
            Notes
          </router-link>
          <router-link to="/" class="btn btn-danger me-2" @click="logout">
            Logout
          </router-link>
      </div>
      <hr>
    </div>
  </main>
</template>

<script>
import {computed} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import router from "@/router";

export default {
  name: "MenuComponent",
  setup() {
    const store = useStore();
    const auth = computed(() => store.state.auth);

    const logout = async () => {
      await axios.post("https://hola2you.eu/api/logout", {withCredentials: true});

      localStorage.removeItem("authorized");
      axios.defaults.headers.common["Authorization"] = ``;

      await store.dispatch("setAuthentication", false);
      await router.push('/');
    }
    return {
      auth,
      logout
    }
  }
}
</script>

<style scoped>
.nav-pills .nav-link, .nav-pills .show>.nav-link {
    color: var(--bs-nav-pills-link-active-color);
    background-color: #babcc3;
}

.menu-title {
  margin: 0 auto;
}

.btn {
  margin: 2%;
}

.scrollspy-example {
    position: relative;
    height: 820px;
    width: 840px;
    margin-top: 0.5rem;
    overflow: auto;
}

::-webkit-scrollbar {
    visibility: hidden;
}
</style>