<template>
  <div class="container mt-3">
    <div v-if="question">
      <h1>{{ question.content }}</h1>
      <!-- TODO Refactor "Posted by" -->
      <p class="mb-0">
        Posted by <span class="question-author">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr />
    </div>

    <div v-else>
      <h1 class="error text-center">404 - Question not found</h1>
    </div>

    <div v-if="question">
      <AnswerComponent
        v-for="answer in answers"
        :answer="answer"
        :key="answer.uuid"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">Loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
          class="btn btn-sm btn-outline-success"
        >
          Load more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
import AnswerComponent from "../components/Answer";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    AnswerComponent,
  },
  data() {
    return {
      question: null,
      answers: [],
      next: null,
      loadingAnswers: false,
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
    async getQuestionAnswers() {
      let endpoint = `/api/v1/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      try {
        const response = await axios.get(endpoint);
        const data = response.data;
        this.answers.push(...data.results);
        this.loadingAnswers = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      } catch (e) {
        console.log(e.response);
      }
    },
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
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