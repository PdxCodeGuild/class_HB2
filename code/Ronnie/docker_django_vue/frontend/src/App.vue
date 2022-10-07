<template>
  <v-app>
  <NavBar></NavBar>
    <router-view></router-view>
  </v-app>
</template>
<script>
import NavBar from '@/components/NavBar.vue';

export default {
    name: "App",
    components: { NavBar }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
}

* {
  margin: 0;
}

html, body {
  height: 100%;
}
</style>
