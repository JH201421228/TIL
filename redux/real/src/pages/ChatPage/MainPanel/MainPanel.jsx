import React, { useEffect, useState } from 'react'
import MessageHeader from './MessageHeader'
import MessageForm from './MessageForm'
import { child, onChildAdded, ref as dbRef, off } from 'firebase/database'
import { db } from '../../../firebase'
import { useDispatch, useSelector } from 'react-redux'
import Message from './Message'


const MainPanel = () => {

  const messagesRef = dbRef(db, 'messages')

  const [messages, setMessages] = useState([])
  const [messagesLoading, setMessagesLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [searchResults, setSearchResults] = useState([])
  const [searchLoading, setSearchLoading] = useState(false)
  
  const {currentUser} = useSelector(state => state.user)
  const {currentChatRoom} = useSelector(state => state.chatRoom)
  const dispatch = useDispatch()

  useEffect(() => {
    if (currentChatRoom.id) {
      addMessagesListener(currentChatRoom.id)
    }
    return () => {
      off(messagesRef)
    }
  }, [currentChatRoom.id])

  const handleSearchMessage = (searchTerm) => {
    const chatRoomMessages = [...messages]
    const regex = new RegExp(searchTerm, "gi")
    const searchResults = chatRoomMessages.reduce((acc, message) => {
      if (
        (message.content && message.content.match(regex)) ||
        message.user.name.match(regex)
        )
       {
        acc.push(message)
        console.log(acc)
       }
       return acc
    }, [])
    setSearchResults(searchResults)
    setSearchLoading(false)
  }

  const handleSearchChange = (event) => {
    console.log('검색어 변경', event.target.value)
    setSearchTerm(event.target.value)
    setSearchLoading(true)
    handleSearchMessage(event.target.value)
  }

  const addMessagesListener = (chatRoomId) => {
    let messagesArray = []

    onChildAdded(child(messagesRef, chatRoomId), DataSnapshot => {
      messagesArray.push(DataSnapshot.val())
      const newMessageArray = [...messagesArray]

      setMessages(newMessageArray)
      setMessagesLoading(false)
    })
  }

  const renderMessages = (messages) => {
    return(
      messages.length > 0 && messages.map((message) => {
        return (
          <Message
            key={message.timestamp}
            message={message}
            user={currentUser}
          />
        )
      })
    )
  }

  return (
    <div style={{padding: '2rem 2rem 0 2rem'}}>
      <MessageHeader handleSearchChange = {handleSearchChange} />
      <div style={{
        width: '100%',
        height: 450,
        border: '0.2rem solid #ececec',
        borderRadius: '4px',
        padding: '1rem',
        marginBottom: '1rem',
        overflow: 'auto'
      }}>
        {searchLoading && <div>Searching...</div>}

        {searchTerm ?
            renderMessages(searchResults)
            :
            renderMessages(messages)
        }
      </div>
      <MessageForm />
    </div>
  )
}

export default MainPanel