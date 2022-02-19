<template>
  <div class="Home mt-3">
    <div class="container">
      <div v-for="question in this.questions" :key="question.pk">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Posted by
              <span class="question-author">{{ question.author }}</span>
            </p>
            <h2>{{ question.content }}</h2>
            <p class="mb-0">{{ question.answers_count }} answers</p>
          </div>
        </div>
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
    // Function to populate questions array
    async getQuestions() {
      let endpoint = "/api/v1/questions/";
      try {
        const response = await axios.get(endpoint);
        this.questions = response.data;
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  created() {
    // Call getQuestions before the page is visible
    this.getQuestions();
  },
};
</script>

<style>
.question-author {
  font-weight: bold;
  color: #dc3545;
}
</style>