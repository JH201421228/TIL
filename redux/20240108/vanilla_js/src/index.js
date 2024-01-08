import {createStore} from "redux"

const plus = document.getElementById("plus")
const minus = document.getElementById("minus")
const number = document.querySelector("span")

const countModifier = () => {
  return "Hello"
}

const countStore = createStore(countModifier)

console.log(countStore)

// let count = 0

// number.innerText = count

// const updateText = () => {
//   number.innerText = count
// }

// const handlePlus = () => {
//   count++
//   updateText()
// }

// const handleMinus = () => {
//   count--
//   updateText()
// }

// plus.addEventListener("click", handlePlus)
// minus.addEventListener("click", handleMinus)