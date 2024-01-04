<template>
  <div id="app">
    <ChatBox />
  </div>
</template>

<script>
import ChatBox from './components/ChatBox.vue';

export default {
  name: 'App',
  components: {
    ChatBox
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
