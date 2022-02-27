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
  created: function(){
      axios.get('http://localhost:5000/',
      {
        params:{
          fruit:'apple',
          animal:'giraffe'
        }
      })
      .then(response => (this.msg= response["data"]))
      .catch(error => console.log(error))
      console.log(this.msg)

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
