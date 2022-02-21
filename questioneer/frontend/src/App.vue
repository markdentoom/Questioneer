<template>
  <nav>
    <NavbarComponent />
  </nav>
  <router-view />
</template>

<script>
import { axios } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue";

export default {
  name: "app",
  components: {
    NavbarComponent,
  },
  methods: {
    async setUserInfo() {
      try {
        const response = await axios.get("/auth/users/me/");
        const requestUser = response.data["username"];
        window.localStorage.setItem("username", requestUser);
      } catch (e) {
        console.log(e);
      }
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>


<style>
body {
  font-family: "Noto Sans JP", sans-serif;
  font-weight: 300;
}
</style>
