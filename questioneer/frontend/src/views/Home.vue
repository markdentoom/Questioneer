<template>
  <div class="Home">
    <h1>Homepage</h1>
    <button @click="getQuestions">Load questions</button>
    <div v-for="question in this.questions" v-bind:key="question.id">
      <div class="card-item">
        <p>{{ question.author }}</p>
        <p>{{ question.created_at }}</p>
        <p>{{ question.content }}</p>
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Home",
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    async getQuestions() {
      let endpoint = "/api/v1/questions/";
      try {
        const response = await axios.get(endpoint);
        this.questions = response.data;
        console.log(this.questions);
      } catch (error) {
        console.log(error.response);
        // alert(error.response.statusText);
      }
    },
  },
};
</script>
