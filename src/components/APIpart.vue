<template>
  <div class="api-view">
    <h1>msg:{{ info }}</h1>

    <p>
    return msg : {{msg}}
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'APIpart',
  props: {
    info : String
  },
  data: function(){
      return{
          msg:null
      }
  },
  mounted: function(){
      axios.get('https://api.ipify.org/',
      {
        params:{
          format:'json'
        }
      })
      .then(response => (this.msg= response))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
