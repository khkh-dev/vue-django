import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import ProfileView from '@/views/ProfileView.vue';
import ProfileUpdateView from '@/views/ProfileUpdateView.vue';
import NotesView from '@/views/NotesView.vue';
import NoteCreateView from '@/views/NoteCreateView.vue';
import NoteUpdateView from '@/views/NoteUpdateView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';

const routes: Array<RouteRecordRaw> = [
  {path: '/', component: HomeView},
  {path: '/profile', component: ProfileView},
  {path: '/profile/update/:id', component: ProfileUpdateView, name: "profile-update"},
  {path: '/notes', component: NotesView},
  {path: '/notes/create', component: NoteCreateView, name: "note-create"},
  {path: '/notes/update/:id', component: NoteUpdateView, name: "note-update"},
  {path: '/login', component: LoginView},
  {path: '/register', component: RegisterView}
]



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
