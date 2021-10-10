<template>
  <div id="nav">
    <navbarComponent />
  </div>
  <router-view />
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
  },
};
</script>

<style>
body {
  font-family: "Noto Sans JP", sans-serif;
  font-weight: 300;
}
</style>
