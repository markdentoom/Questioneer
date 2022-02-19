<template>
  <div class="Home mt-3">
    <div class="container">
      <div v-for="question in this.questions" :key="question.uuid">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-1">
              Posted by
              <span class="question-author">{{ question.author }}</span>
            </p>
            <h2>
              <router-link
                :to="{ name: 'question', params: { slug: question.slug } }"
                class="question-link"
              >
                {{ question.content }}
              </router-link>
            </h2>
            <p class="mb-0">{{ question.answers_count }} answers</p>
          </div>
        </div>
      </div>

      <div class="my-4">
        <p v-show="loadingQuestions">Loading...</p>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn-sm btn-outline-success"
        >
          More questions
        </button>
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
      next: null,
      loadingQuestions: false,
    };
  },
  methods: {
    // Function to populate questions array
    async getQuestions() {
      let endpoint = "/api/v1/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      try {
        const response = await axios.get(endpoint);
        const data = response.data;
        this.questions.push(...data.results);
        this.loadingQuestions = false;
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
    document.title = "Questioneer";
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
.question-link {
  font-weight: 400;
  color: black;
  text-decoration: none;
}
.question-link:hover {
  color: #343a40;
}
</style>