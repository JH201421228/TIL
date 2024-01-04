<template>
    <div>
      <div v-for="message in messages" :key="message.id" :class="{ 'user-message': message.sender === '제사준비10년차', 'partner-message': message.sender === '야채장수' }">
        <div class="message-container">
          <img v-if="message.sender === '야채장수'" src="@/image/1.jpg" alt="" class="user-avatar right-avatar">
          <div class="message-box">
            <strong>{{ message.sender }}:</strong> {{ message.text }}
          </div>
          <img v-if="message.sender === '제사준비10년차'" src="@/image/2.jpg" alt="" class="user-avatar left-avatar">
        </div>
      </div>
      <div class="input-container">
        <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="메시지를 입력하세요" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        messages: [],
        newMessage: '',
        partnerResponses: [
          '안녕하세요!',
          '반가워요!',
          '뭐라고요?',
          '어떤 이야기를 해볼까요?',
          '오늘 날씨가 좋네요.'
        ],
        partnerResponseIndex: 0
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim() !== '') {
          this.messages.push({
            id: Date.now(),
            sender: '야채장수',
            text: this.newMessage
          });
  
          // 배열에 있는 순서대로 대답
          this.messages.push({
            id: Date.now(),
            sender: '제사준비10년차',
            text: this.partnerResponses[this.partnerResponseIndex]
          });
  
          // 다음 대답을 위해 인덱스 증가
          this.partnerResponseIndex = (this.partnerResponseIndex + 1) % this.partnerResponses.length;
  
          this.newMessage = '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .user-message {
    text-align: left;
    margin-bottom: 8px;
    color: #3498db;
  }
  
  .partner-message {
    text-align: right;
    margin-bottom: 8px;
    color: #e74c3c;
  }
  
  .input-container {
    position: fixed;
    bottom: 20px;
    width: 100%;
    background-color: #f1f1f1;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
  }
  
  .input-container input {
    flex: 1;
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
  }
  
  .message-box {
    display: inline-block;
    padding: 8px;
    border-radius: 5px;
    background-color: #ddd;
  }
  
  .user-avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .left-avatar {
    margin-right: 10px;
  }
  
  .right-avatar {
    margin-left: 10px;
  }
  </style>
  