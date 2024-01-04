<template>
    <div>
        <h3>{{ cardName }}</h3>
        <p>{{ cardTitle }}</p>
        <button @click="deleteCardFunc">명함 삭제</button>
    </div>
</template>

<script setup>
    
    const props = defineProps({
        cardName:String,
        cardTitle:String,
        cardIndex:Number,
    })

    const emit = defineEmits(['deleteCardFunc',])

    const deleteCardFunc = () => {
        emit('deleteCardFunc', props.cardIndex)
    }

</script>


<style scoped>
    div{
        display: inline-block;
        width: 40%;
        background-color: whitesmoke;
        border: 1px solid gray;
        margin: 5px;
        border-radius: 5%;
        padding: 5px;
    }
</style>