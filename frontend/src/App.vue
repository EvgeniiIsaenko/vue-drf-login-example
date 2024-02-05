<template>
  <nav>
    <router-link v-if="this.$cookies.get('token')" to="/profile">Профиль</router-link>
    <div v-else>
      <router-link to="/register">Зарегистрироваться</router-link>
      <router-link to="/login" style="margin-left: 15px;">Войти</router-link>
    </div>
  </nav>
  <router-view/>
</template>

<script>
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
