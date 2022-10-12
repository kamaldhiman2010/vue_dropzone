<template>
  <div id="app">
    <FileUpload />
  </div>
</template>

<script>

// import FileUpload from './components/image_upload.vue';
import FileUpload from './components/vueDropzone.vue'
// import FileUpload from './components/upload_image.vue'


export default {
  name: 'App',
  components: {
  
    FileUpload
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
