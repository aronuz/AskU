<template>
  <div class="home">
    <h1>Home Page</h1>
    <div class="questions" v-if="questions.length > 0">
      <div v-for="question in questions" :key="question.uuid">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Asked by:
              <span class="question-author">{{ question.author }}</span>
            </p>
            <h2>
              <!-- <router-link
                :to="{ name: 'question', params: { slug: question.slug } }"
                class="question-link"
              > -->
              {{ question.content }}
              <!-- </router-link> -->
            </h2>
            <p class="mb-0">{{ question.answers_count }} answers</p>
          </div>
        </div>
      </div>
    </div>
    <div class="my-4">
      <p v-show="loadingQuestionsFlag">loading...</p>
      <button
        v-show="next"
        @click="getQuestions"
        class="btn btn-sm btn-outline-success"
      >
        Load More
      </button>
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
      loadingQuestionsFlag: false,
    };
  },
  methods: {
    async getQuestions() {
      let endPoint = !this.next ? "/api/v1/questions/" : this.next;
      try {
        this.loadingQuestionsFlag = true;
        const r = await axios.get(endPoint);
        this.questions.push(...r.data.results);
        this.next = r.data.next || null;
      } catch (e) {
        alert(e.response.statusText);
      } finally {
        this.loadingQuestionsFlag = false;
      }
    },
  },
  created() {
    this.getQuestions();
  },
};
</script>


<style scoped>
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