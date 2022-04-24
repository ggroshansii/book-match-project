/* eslint-disable */

import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/auth/Login'
import Register from '../components/auth/Register'
import Splash from '../components/Splash'
import Movies from '../components/Movies.vue'
import Genres from '../components/Genres.vue'
import Movie from '../components/Movie.vue'
import UserMovies from '../components/UserMovies.vue'
import Profile from '../components/Profile.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Splash',
      component: Splash,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/movies/',
      name: 'Movies',
      component: Movies
    },
        {
      path: '/genres',
      name: 'Genres',
      component: Genres,
    },
    {
      path: '/movie/:title',
      name: 'Movie',
      component: Movie
    },
    // {
    //   path: '/user/profile/movies',
    //   name: 'UserMovies',
    //   component: UserMovies,
    // },
    {
      path: '/user/profile',
      name: 'Profile',
      component: Profile,
    }

  ]
})