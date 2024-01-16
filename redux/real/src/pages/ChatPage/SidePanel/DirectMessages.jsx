import React, { useEffect, useState } from 'react'
import {FaRegSmile} from 'react-icons/fa'
import {ref, onChildAdded, DataSnapshot} from 'firebase/database'
import {db} from '../../../firebase'
import { useDispatch, useSelector } from 'react-redux'
import { setCurrentChatRoom, setPrivateChatRoom } from '../../../store/chatRoomSlice'

const DirectMessages = () => {

  const usersRef = ref(db, "users")

  const dispatch = useDispatch()

  const [activeChatRoom, setActiveChatRoom] = useState('')

  const [users, setUsers] = useState([])

  const {currentUser} = useSelector(state => state.user)

  useEffect(() => {
    if (currentUser?.uid) {
      addUsersListener(currentUser.uid)
    }
    return () => {

    }
  }, [currentUser?.uid])

  const addUsersListener = (currentUserId) => {
    let usersArray = []
    onChildAdded(usersRef, DataSnapshot => {
      if (currentUserId !== DataSnapshot.key) {
        let user = DataSnapshot.val()
        user['uid'] = DataSnapshot.key
        usersArray.push(user)

        const newUsersArray = [...usersArray]
        setUsers(newUsersArray)
      }
    })
  }

  const getChatRoomId = (userId) => {
    const currentUserId = currentUser.uid

    return (
      userId > currentUserId
      ? `${userId}/${currentUserId}`
      : `${currentUserId}/${userId}`
    )
  }

  const changeChatRoom = (user) => {
    const chatRoomId = getChatRoomId(user.uid)
    const chatRoomData = {
      id: chatRoomId,
      name: user.name
    }
    dispatch(setCurrentChatRoom(chatRoomData))
    dispatch(setPrivateChatRoom(true))
    setActiveChatRoom(user.uid)
  }

  const renderDirectMessages = (users) => {
    return (
      users.length > 0 &&
      users.map(user => (
        <li key={user.uid}
          style={{
            backgroundColor: user.uid === activeChatRoom ? '#ffffff45':''
          }}
          onClick={() => {changeChatRoom(user)}}
        >
          # {user.name}
        </li>
      ))
    )
  }

  return (
    <div>
      <span style={{display: 'flex', alignItems: 'center'}}>
        <FaRegSmile
          style={{marginRight: 3}}
        />
        DIRECT MESSAGES
      </span>
      <ul style={{listStyleType: 'none', padding: 0}}>
        {renderDirectMessages(users)}
      </ul>
    </div>
  )
}

export default DirectMessages