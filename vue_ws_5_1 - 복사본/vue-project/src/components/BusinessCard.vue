<template>
    <div>
      <p v-if="businessCard.length === 0">명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
      <p v-else>현재 보유중인 명함 수: {{ businessCard.length }}</p>
  
      <div class="chat-container">
        <BusinessCardDetail
          v-for="(card, index) in businessCard"
          :key="card.name"
          :card-name="card.name"
          :card-title="card.title"
          :card-index="index"
          @delete-card-func="deleteCard"
          :is-user-message="true"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import BusinessCardDetail from '@/components/BusinessCardDetail.vue';
  
  const businessCard = ref([
    { name: '일론 머스크', title: '테슬라 테크노킹' },
    { name: '래리 엘리슨', title: '오라클 창업주' },
    { name: '빌 게이츠', title: '마이크로소프트 공동 창업주' },
    { name: '레리 페이지', title: '구글 공동창업주' },
    { name: '세르게이 브린', title: '구글 공동창업주' },
  ]);
  
  const deleteCard = (idx) => {
    businessCard.value.splice(idx, 1);
  };
  </script>
  
  <style scoped>
  div {
    text-align: center;
  }
  
  .chat-container {
    display: flex;
    flex-direction: column;
    align-items: flex-end; /* Align items to the right side */
  }
  
  .business-card-bubble {
    background-color: #e0e0e0;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    max-width: 70%;
    text-align: left;
  }
  
  </style>
  