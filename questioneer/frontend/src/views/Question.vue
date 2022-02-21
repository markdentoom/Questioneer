<template>
  <div class="container mt-3">
    <div v-if="question">
      <h1>{{ question.content }}</h1>
      <!-- TODO Refactor "Posted by" -->
      <p class="mb-0">
        Posted by <span class="question-author">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>

      <div v-if="userHasAnswered">
        <p class="answer-added">You have already answered this question</p>
      </div>
      <div v-else-if="showForm">
        <form @submit.prevent="onSubmit">
          <p>Answer question</p>
          <textarea
            v-model="newAnswerBody"
            class="form-control"
            placeholder="Share your knowledge!"
            rows="10"
          />
          <button type="submit" class="btn btn-success my-3">Submit</button>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button class="btn btn-success" @click="showForm = true">
          Answer question
        </button>
      </div>

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
      userHasAnswered: false,
      showForm: false,
      newAnswerBody: null,
      error: null,
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
        this.userHasAnswered = data.user_has_answered;
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
    async onSubmit() {
      if (!this.newAnswerBody) {
        this.error = "Please fill out an answer";
        return;
      }
      const endpoint = `/api/v1/questions/${this.slug}/answer/`;
      try {
        const response = await axios.post(endpoint, {
          body: this.newAnswerBody,
        });
        this.answers.unshift(response.data);
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
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
.answer-added {
  font-weight: bold;
  color: green;
}
</style>