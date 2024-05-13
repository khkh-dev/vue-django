<template>
    <main class="text-center" v-if="!auth">
      <h3>This is welcome page.
        <p>{{ auth ? message : "Please sign in" }}</p>
      </h3>
    </main>
    <main>
      <div class="d-flex flex-nowrap" v-if="auth">
        <MenuComponent />
      </div>
    </main>
</template>

<script>
import {ref, onMounted, computed, onBeforeMount} from "vue";
import axios from "axios";
import {useStore} from "vuex";
import MenuComponent from "@/components/MenuComponent";

export default {
  name: "HomeView",
  components: {MenuComponent},
  setup() {
    const message = ref("");
    const store = useStore();
    const auth = computed(() => store.state.auth);

    return {
      message,
      auth
    }
  }
}
</script>

<style>
h3 {
  margin-top: 20px;
}
</style>