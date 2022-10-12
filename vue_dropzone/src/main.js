import Vue from 'vue'
import App from './App.vue'
import VueAxios from "vue-axios";
import axios from "axios";
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

Vue.use(VueAxios, axios);
// var cors = require('cors')
Vue.config.productionTip = false;
// Vue.use(cors()) 
import AxiosPlugin from 'vue-axios-cors';
 
Vue.use(AxiosPlugin)

new Vue({

  render: (h) => h(App),
}).$mount('#app');