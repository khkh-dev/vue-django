<template>
  <div class="container mt-5" v-if="auth">
    <div class="row d-flex justify-content-center">
      <div class="card col-md-6" v-if="profile" v-bind:key="profile.id">
        <form method="post">
            <div class="form-group">
                <label for="first_name">First name</label>
                <input
                    type="text"
                    class="form-control"
                    id="first_name"
                    v-model="profile.first_name"
                    name="first_name"
                    placeholder="Enter first name"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="firstNameErrors && firstNameErrors.length">
                    {{ firstNameErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="last_name">Last name</label>
                <input
                    type="text"
                    class="form-control"
                    id="last_name"
                    v-model="profile.last_name"
                    name="last_name"
                    placeholder="Enter last name"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="lastNameErrors && lastNameErrors.length">
                    {{ lastNameErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input
                    type="email"
                    class="form-control"
                    id="email"
                    v-model="profile.email"
                    name="email"
                    placeholder="Enter email"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="emailErrors && emailErrors.length">
                    {{ emailErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="last_name">Username</label>
                <input
                    type="text"
                    class="form-control"
                    id="username"
                    v-model="profile.username"
                    name="username"
                    placeholder="Enter username"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="usernameErrors && usernameErrors.length">
                    {{ usernameErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="last_name">About you</label>
                <input
                    type="text"
                    class="form-control"
                    id="about"
                    v-model="profile.about"
                    name="about"
                    placeholder="Tell more about you"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="aboutErrors && aboutErrors.length">
                    {{ aboutErrors }}
                  </p>
                </div>
            </div>
        </form>

        <div class="buttons">
            <button class="btn btn-light " v-on:click="updateProfile(profile)">Update</button>
            <router-link to="/profile" class="btn btn-outline-dark active" aria-current="page">
              Back to profile
            </router-link>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {computed, onMounted} from "vue";
import router from "@/router";
import {useStore} from "vuex";

export default {
  name: "ProfileUpdateView",
  data() {
      return {
        profile: {
          'id': '',
          'first_name': '',
          'last_name': '',
          'email': '',
          'username': '',
          'image': '',
          'about': ''
        },
        firstNameErrors: null,
        lastNameErrors: null,
        emailErrors: null,
        usernameErrors: null,
        aboutErrors: null,
      }
  },
  mounted() {
      this.getProfile();
  },
  methods: {
      checkForm: function (e) {
        if (!this.profile.first_name) {
          this.firstNameErrors = 'First name is required.';
        } else {
          this.firstNameErrors = '';
        }
        if (!this.profile.last_name) {
          this.lastNameErrors = 'Last name is required.';
        } else {
          this.lastNameErrors = '';
        }
        if (!this.profile.email) {
          this.emailErrors = 'Email name is required.';
        } else {
          this.emailErrors = '';
        }
        if (!this.profile.username) {
          this.usernameErrors = 'Username is required.';
        } else {
          this.usernameErrors = '';
        }
        if (!this.profile.about) {
          this.aboutErrors = 'Information about you is required.';
        } else {
          this.aboutErrors = '';
        }
      },
      getProfile: function () {
        axios.get('https://hola2you.eu/api/users/' + this.$route.params.id + '/')
          .then( response => {
              this.profile = response.data;
        });
      },
      updateProfile: function () {
        this.checkForm()
        if (!this.firstNameErrors && !this.lastNameErrors && !this.emailErrors && !this.usernameErrors && !this.aboutErrors) {
          axios.patch(`https://hola2you.eu/api/users/${this.profile.id}/`,
              this.profile
          )
          .then(async () => {
            await router.push('/profile');
          })
        }
      }
  },
  setup() {
    const store = useStore();
    const auth = computed(() => store.state.auth);

    return {
      auth,
    }
  }
}
</script>


<style scoped>
.card {
  padding: 30px;
  position:relative;
  overflow:hidden;
  border-radius: 8px;
}

.buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin-top: 10px;
}

.buttons > .btn {
  width: 45%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.form-group {
  margin-bottom: 10px;
}

.form-errors, .errors-block {
  color: #dc0c0c;
}
</style>
