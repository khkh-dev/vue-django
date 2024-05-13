<template>
  <div class="container mt-5">
    <div class="row d-flex justify-content-center">
      <div class="card col-md-6">
        <form method="post">
            <div class="form-group">
                <label for="name">Title</label>
                <input
                    type="text"
                    class="form-control"
                    id="title"
                    v-model="note.title"
                    name="title"
                    placeholder="Enter title"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="descriptionErrors && descriptionErrors.length">
                    {{ titleErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="description">Description</label>
                <input
                    type="text"
                    class="form-control"
                    id="text"
                    v-model="note.text"
                    name="text"
                    placeholder="Enter description"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="descriptionErrors && descriptionErrors.length">
                    {{ descriptionErrors }}
                  </p>
                </div>
            </div>
        </form>

        <div class="buttons">
            <button class="btn btn-outline-dark" v-on:click="createNote(note)">Create</button>
            <router-link to="/notes" class="btn btn-outline-dark" aria-current="page">
              Back to notes
            </router-link>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import {useStore} from "vuex";
import {computed} from "vue";
import axios from "axios";
import router from "@/router";

export default {
  name: "NoteCreateView",
  data() {
      return {
          note: {
              title: '',
              text: '',
          },
          titleErrors: null,
          descriptionErrors: null,
      }
  },
  methods: {
      checkForm: function (e) {
        if (!this.note.title) {
          this.titleErrors = 'Title is required.';
        } else {
          this.titleErrors = ''
        }
        if (!this.note.text) {
          this.descriptionErrors = 'Description is required.';
        } else {
          this.descriptionErrors = '';
        }
      },
      createNote: function () {
        this.checkForm()
        if (!this.titleErrors && !this.descriptionErrors) {
          axios.post(`https://hola2you.eu/api/notes/`,
            this.note
          )
          .then(async () => {
              await router.push('/notes');
          })
        }
      }
  },
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
.card {
  padding: 20px;
  position:relative;
  overflow:hidden;
  border-radius:8px;
  cursor:pointer;
}

.buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 75%;
  margin: 0 auto;
  padding-top: 10px;
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