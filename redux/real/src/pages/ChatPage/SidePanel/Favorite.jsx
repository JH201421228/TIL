import { DataSnapshot, child, off, onChildAdded, onChildRemoved, ref } from 'firebase/database'
import React, { useEffect, useState } from 'react'
import { FaRegSmileBeam } from 'react-icons/fa'
import { db } from '../../../firebase'
import { useSelector } from 'react-redux'

const Favorite = () => {
  
  const {currentUser} = useSelector(state => state.user)
  const [favoriteChatRooms, setFavoriteChatRooms] = useState([])

  useEffect(() => {
    if (currentUser?.uid) {
      addListener(currentUser.uid)
    }
    return () => {
      removeListener(currentUser.uid)
    }
  }, [currentUser?.uid])

  const removeListener = (userId) => {
    off(child(usersRef, `${userId}/favorite`))
  }

  const usersRef = ref(db, 'users')
  const addListener = (userId) => {
    let favoriteArray = []
    onChildAdded(child(usersRef, `${userId}/favorite`), DataSnapshot => {
      favoriteArray.push({id: DataSnapshot.key, ...DataSnapshot.val()})
      const newFavoriteChatRooms = [...favoriteArray]
      setFavoriteChatRooms(newFavoriteChatRooms)
      console.log(favoriteArray)
    })
    onChildRemoved(child(usersRef, `${userId}/favorite`), DataSnapshot => {
      const filteredChatRooms = favoriteArray.filter(chatRoom => {
        return chatRoom.id !== DataSnapshot.key
      })
      favoriteArray = filteredChatRooms
      setFavoriteChatRooms(favoriteArray)
    })
  }

  const renderFavoriteChatRooms = (favoriteChatRooms) => {
    return(
      favoriteChatRooms.length > 0 &&
      favoriteChatRooms.map(chatRoom =>
        <li
          key={chatRoom.id}
        >
          # {chatRoom.name}
        </li>
        )
    )
  }

  return (
    <div>
      <span style={{display: 'flex', alignItems: 'center'}}>
        <FaRegSmileBeam style={{marginRight: 3}} />
        FAVORITE
      </span>
      <ul style={{listStyleType: 'none', padding: 0}}>
        {renderFavoriteChatRooms(favoriteChatRooms)}
      </ul>
    </div>
  )
}

export default Favorite