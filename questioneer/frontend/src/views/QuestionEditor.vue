<template>
  <div class="container my-2">
    <h1 class="mb-3">Ask a question</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="questionBody"
        class="form-control"
        rows="4"
        placeholder="What would you like to ask?"
      />
      <button type="submit" class="btn btn-success mt-3">Submit</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>


<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "QuestionEditor",
  props: {
    slug: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      questionBody: null,
      error: null,
    };
  },
  methods: {
    async performNetworkRequest() {
      let endpoint = "/api/v1/questions/";
      let method = "POST";
      if (this.slug !== undefined && this.slug !== "") {
        endpoint += `${this.slug}/`;
        method = "PUT";
      }
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: { content: this.questionBody },
        });
        this.$router.push({
          name: "question",
          params: { slug: response.data.slug },
        });
      } catch (e) {
        this.error = e.response.statusText;
      }
    },
    onSubmit() {
      if (!this.questionBody) {
        this.error = "Please fill out an answer";
        return;
      } else if (this.questionBody.length > 240) {
        this.error = "Ensure this field has no more than 240 characters";
      } else {
        console.log("YEEEEEEE");
        this.performNetworkRequest();
      }
    },
  },
  created() {
    document.title = "Editor - QuestionTime";
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined && to.params.slug !== "") {
      const endpoint = `/api/v1/questions/${to.params.slug}/`;
      try {
        const response = await axios.get(endpoint);
        return next((vm) => (vm.questionBody = response.data.content));
      } catch (e) {
        console.log(e);
      }
    } else {
      return next();
    }
  },
};
</script>
