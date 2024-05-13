<template>
  <div class="container mt-5" v-if="auth">
    <div class="row d-flex justify-content-center">
      <div class="card col-md-8" v-if="notes && notes.length">
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(note) in notes" :key="note.id">
                    <td>{{note.title}}</td>
                    <td>{{note.text}}</td>
                    <td class="td-actions">
                      <div class="td-actions_items">
                        <router-link :to="{name: 'note-update', params: { id: note.id }}" class="btn btn-success">Update</router-link>
                        <button class="btn btn-danger" v-on:click="deleteNote(note)">Delete</button>
                      </div>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="buttons">
          <router-link :to="{name: 'note-create'}" class="btn btn-outline-dark">
            Create a note
          </router-link>
          <router-link to="/" class="btn btn-outline-dark" aria-current="page">
            Back to home
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="!notes.length">
        <div class="message">
          <p>No notes. Would you like to create a new one?</p>
        </div>
        <div class="buttons">
          <router-link :to="{name: 'note-create'}" class="btn btn-outline-dark">
            Create a note
          </router-link>
          <router-link to="/" class="btn btn-outline-dark" aria-current="page">
            Back to home
          </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {useStore} from "vuex";
import {computed, onMounted, ref} from "vue";
import axios from "axios";

export default {
  name: "NotesView",
  data() {
      return {
          notes: [],
          // message: ""
      }
  },
  mounted() {
      this.all();
  },
  methods: {
      all: function () {
        axios.get('https://hola2you.eu/api/notes/')
            .then( response => {

              if (response.data.length !== 0) {
                this.notes = response.data
              } else {
                this.notes = []
              }
            })
      },
      deleteNote: function (note) {
        axios.delete(`https://hola2you.eu/api/notes/${note.id}/`)
          .then((response) => {
            if (response) {
              this.all();
            }
          })
      },
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
  padding: 20px;
  position:relative;
  overflow:hidden;
  border-radius:8px;
  cursor:pointer;
}

.buttons, .message {
  display: flex;
  flex-direction: row;
  width: 75%;
  margin: 0 auto;
  justify-content: space-around;
}

.buttons > .btn {
  width: 45%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.btn-success {
  color: #fff;
  background-color: #28a745;
  border-color: #28a745;
}

.btn-success:hover {
  color: #fff;
  background-color: #22893a;
  border-color: #22893a;
}

td.td-actions {
  border: 0;
}

.td-actions {
  width: 200px;
}

.td-actions_items {
  display: flex;
  flex-direction: row;
  width: 200px;
  margin: 0 auto;
  justify-content: space-around;
}

td {
  vertical-align: baseline;
}
</style>