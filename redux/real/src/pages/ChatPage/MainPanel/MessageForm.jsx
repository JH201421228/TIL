import { child, push, set, ref as dbRef, serverTimestamp } from 'firebase/database'
import React, { useState } from 'react'
import { useSelector } from 'react-redux'

const MessageForm = () => {

  const [content, setContent] = useState('')
  const [loading, setLoading] = useState(false)
  const [errors, setErrors] = useState([])
  const messagesRef = dbRef(db, 'messages')

  const {currentChatRoom} = useSelector(state => state.chatRoom)
  const {currentUser} = useSelector(state => state.user)
  const {isPrivateChatRoom} = useSelector(state => chatRoom)

  const handleSubmit = async(e) => {
    e.preventDefault()
    if (!content) {
      setErrors(pre => pre.content('Type Contents First'))
      return
    }
    setLoading(true)
    try {
      await set(push(child(messagesRef, currentChatRoom.id)), )
    }
    catch () {

    }
  }

  const createMessage = (fileUrl = null) => {
    const message = {
      timestamp: serverTimestamp(),
      user: {
        id: currentUser.uid,
        name: currentUser.displayName,
        image: currentUser.photoURL
      }
    }

    if (fileUrl !== null) {
      message('image') = fileUrl
    }
    else {
      
    }

    return message
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          style={{width: '100%', height: 90, border: '0.2rem solid rgb(235, 236, 236), borderRadius: 4'}}
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <div>
          {errors.map((errorMsg, i) => <p style={{color: 'red'}} key={i}>{errorMsg}</p>)}
        </div>
        <div style={{display: 'flex', gap: 16}}>
          <div style={{flexGrow: 1}}>
            <button className='message-form-button' type='submit' style={{width: '100%', fontSize: 20, fontWeight: 'bold' }} disabled={loading}>
              보내기
            </button>
          </div>
          <div style={{flexGrow: 1}}>
            <button className='message-form-button' type='submit' style={{width: '100%', fontSize: 20, fontWeight: 'bold' }} disabled={loading}>
              이미지
            </button>
          </div>
        </div>
      </form>
      <input
        type= 'file'
        accept= 'image/jpeg, image/png'
        style={{display: 'none'}}
      />
    </div>
  )
}

export default MessageForm