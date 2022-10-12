<template>
  <div id="app">
    
    <div>
      <p>File Name</p>
      <input
        type="file_name"
        id="recipient"
        v-model="data_fields.file_name"
        class="
          w-full
          bg-gray-100 bg-opacity-50
          rounded
          border border-gray-300
          focus:border-indigo-500
          focus:bg-white
          focus:ring-2
          focus:ring-indigo-200
          text-base
          outline-none
          text-gray-700
          py-1
          px-3
          leading-8
          transition-colors
          duration-200
          ease-in-out
        "
      />
    </div>
    <div>
      <p>Add Image</p>
      <vue-dropzone
        ref="vueDropzone"
        id="drop1"
        v-on:vdropzone-sending="sendImages"
        :options="dropOptions"
        @vdropzone-complete="afterComplete"
        @vdropzone-removed-file="removeThisFile"
        v-on:vdropzone-success="showSuccess"
      ></vue-dropzone>
      <button v-on:click="triggerSend()">Send images</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vueDropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
export default {
  data: () => ({
    thisFile: "",
    all_data:[],
    data_fields: {
      id: "",
      file_name: "",
      images: "",
    },
    dropOptions: {
      autoProcessQueue: false,
      url: "/create/",
      headers: { "My-Awesome-Header": "header - value " },
      thumbnailWidth: 150,
      uploadMultiple: true,
      maxFiles: 5,
      addRemoveLinks: true,
      destroyDropzone: false,
      parallelUploads: 5,
      dictDefaultMessage:
        "<div class = 'dropzone-custom-title'><i class='fas fa-cloud-upload-alt '></i><br/>Drop your files</div>",
      // acceptedFile: ".png,.jpg,.jpeg",
    },
  }),
  components: {
    vueDropzone,
  },
  methods: {
    dropzoneChangeUrl() {
      this.$refs.vueDropzone.setOption("url", `create/`);
    },
    triggerSend() {
      this.$refs.vueDropzone.processQueue();
      this.$refs.vueDropzone.getUploadingFiles();
    },
    sendImages(file, xhr, formData) {
      if (formData) {
        // xhr.setRequestHeader("Header", "multipart/form-data");
        formData.append("images", file);
        formData.append("file_name", this.data_fields.file_name);
        // formData.append("id",  this.$store.data_fields.id);
        this.data_fields.images = file;
        console.log(file.upload.uuid);
        this.data_fields.id = file.upload.uuid;
        formData.append("uuid", this.data_fields.id);
        console.log(this.data_fields.id);
        this.all_data.push(this.data_fields)
        console.log(this.all_data)
        return formData;
      } else {
        console.log("error ");
      }
    },
    afterComplete(response) {
      if (response.status == "success") {
        alert("upload successful");
        this.sendSuccess = true;
      } else {
        console.log("upload failed");
      }
    },
    removeThisFile: function () {

 
      // console.log(this.all_data.id)
     
      const data = {
        id: this.data_fields.id,
        file_name: this.data_fields.file_name,
        images: this.data_fields.images,
      };
      console.log(data);
      // if (!confirm("Are you sure, you want to delete")) {
      //   return false;
      // }
      axios
        .delete("delete/" + data.id + "/")
        .then(() => {
          console.log("deleted");
        })
        .catch((error) => {
          console.log(error);
        });
      // this.$refs.vueDropzone.removeFile(thisFile)
      // console.log("File removed!")
    },
    showSuccess: function (file) {
      console.log("A file was successfully uploaded", file);
    },
    removeAllFiles() {
      this.$refs.dropzone.removeAllFiles();
    },
  },
};
</script>
<style>
.dropzone-custom-title {
  margin-top: 0;
  color: #00b782;
}
</style>