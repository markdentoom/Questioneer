<template>
  <div class="container mt-3">
    <div v-if="question">
      <h1>{{ question.content }}</h1>
      <!-- TODO Refactor "Posted by" -->
      <p class="mb-0">
        Posted by <span class="question-author">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
    </div>
    <div v-else>
      <h1 class="error text-center">404 - Question not found</h1>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      question: null,
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    async getQuestionData() {
      const endpoint = `/api/v1/questions/${this.slug}/`;
      try {
        const response = await axios.get(endpoint);
        const data = response.data;
        this.question = data;
        this.setPageTitle(data.content);
      } catch (e) {
        console.log(e.response);
        this.setPageTitle("404 - Not found");
      }
    },
  },
  created() {
    this.getQuestionData();
  },
};
</script>

<style>
.question-author {
  font-weight: bold;
  color: #dc3545;
}
.error {
  font-weight: bold;
  color: #dc3545;
}
</style>