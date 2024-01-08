// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCWLDcyVXnnsX73czz0D7inUusW-vYXElU",
  authDomain: "react-chat-app-57803.firebaseapp.com",
  projectId: "react-chat-app-57803",
  storageBucket: "react-chat-app-57803.appspot.com",
  messagingSenderId: "216229125089",
  appId: "1:216229125089:web:7ef908fadcc0526e3590a0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default app