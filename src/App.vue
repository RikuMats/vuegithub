<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <APIpart info="sss"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import APIpart from './components/APIpart.vue'
export default {
  name: 'App',
  components: {
    HelloWorld,
    APIpart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
