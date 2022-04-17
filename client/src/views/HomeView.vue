


<template>
  <div class="" id="app">
    <ul>
      <li v-for="item in data" :key="item.name">名称：{{item.name}} 电话号码：{{item.phone}}</li>
    </ul>
  </div>
</template>




<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data() {
    return {
      data: []
    }
  },
  created() {
    axios.post('/api/register?dd=222&33=67666').then(data=>{
      this.data = data.data.data;
    })
  }
}
</script>
