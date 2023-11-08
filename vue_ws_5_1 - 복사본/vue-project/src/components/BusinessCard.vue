<template>
    <div>
        <p v-if="businessCard.length === 0">명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
        <p v-else>현재 보유중인 명함 수 : {{ businessCard.length }}</p>
        <BusinessCardDetail 
            v-for="(card, index) in businessCard"
            :key="card.name"
            :card-name="card.name"
            :card-title="card.title"
            :card-index="index"
            @delete-card-func="deleteCard"
        />
    </div>
</template>

<script setup>

    import {ref} from 'vue'
    import BusinessCardDetail from '@/components/BusinessCardDetail.vue'

    const businessCard = ref([
        {name:'일론 머스크', title:'테슬라 테크노킹'},
        {name:'래리 엘리슨', title:'오라클 창업주'},
        {name:'빌 게이츠', title:'마이크로소프트 공동 창업주'},
        {name:'레리 페이지', title:'구글 공동창업주'},
        {name:'세르게이 브린', title:'구글 공동창업주'},
    ])

    const deleteCard = (idx) => {
        businessCard.value.splice(idx, 1)
    }

</script>

<style scoped>

</style>