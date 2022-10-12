<template>
  <div class="container">
    
    <form action="create_single/" method="post" enctype="multipart/form-data">
      <input type="text" name="file_name" placeholder="Enter name" />
      <br />
      <input type="file" name="images" id="" placeholder="Choose DP" />
      <br />
      <br />
      <button type="submit" @click="submitData">Submit</button>
    </form>
    <div v-for="(image, key) in images" :key="key">
      <div>
        <img src="get/" style="width: 150px;
                                height: 100px;" />
        {{ image.images }}
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
export default {
  /*
      Defines the data used by the component
    */
  data() {
    return {
      images:[],
      file: "",
      post_data: {
        images: "",
        file_name: "",
      },
    };
  },

  methods: {
    submitData() {
      const form = document.querySelector("form");
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        axios
          .post("create_single/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((res) => {
            console.log(res);
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
  },
  beforeMount(){
    axios.get("get/").then((res)=>{
    this.images = res.data.data
    console.log(this.images)
  })
  .catch((err)=>{
    console.log(err)
  })

  }
};
</script>