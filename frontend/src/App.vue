<template>
  <NavigationComponent />
  <router-view />
</template>

<script>
import NavigationComponent from "@/components/NavigationComponent";
export default {
  components: {NavigationComponent}
}
</script>

<style>
.form-signin, .form-register {
  max-width: 330px;
  padding: 1rem;
}

.form-signin, .form-register .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
}

.form-register button[type="submit"] {
  margin-top: 10px;
}
</style>