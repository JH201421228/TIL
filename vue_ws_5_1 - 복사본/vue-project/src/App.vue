<template>
  <div>
    <header>
      <h1>명함 관리 페이지</h1>
    </header>

    <main>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>

    <article>
      <h2>보유 명함 목록</h2>
      <BusinessCard />
    </article>

    <footer>
      <p>(c) 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>

  import BusinessCard from './components/BusinessCard.vue';

</script>

<style scoped>
  div{
    text-align: center;
  }
  header{
    background-color: cornflowerblue;
    color: white;
    width: 40%;
    margin: auto;
    padding: 1px;
  }
  footer{
    position: relative;
    bottom: 0;
    background-color: aliceblue;
  }
</style>