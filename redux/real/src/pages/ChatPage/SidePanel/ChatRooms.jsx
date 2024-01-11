import React, { useEffect, useState } from 'react'
import { Button, Modal, Form } from 'react-bootstrap'
import {FaPlus, FaRegSmileWink} from 'react-icons/fa'
import {DataSnapshot, child, ref as dbRef, onChildAdded, push, update} from 'firebase/database'
import {db} from '../../../firebase'
import { useDispatch, useSelector } from 'react-redux'

const ChatRooms = () => {
  const [show, setShow] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')

  const chatRoomsRef = dbRef(db, "chatRooms")

  const [chatRooms, setChatRooms] = useState([])
  const [firstLoad, setFirstLoad] = useState(true)
  const [activeChatRoomId, setActiveChatRoomId] = useState('')

  const {currentUser} = useSelector((state) => state.user)
  const dispatch = useDispatch()

  useEffect(() => {
    addChatRoomsListners()
  }, [])

  const handleSubmit = async () => {

    if (isFormValid(name, description)) {

      const key = push(chatRoomsRef).key

      const newChatRoom = {
        id: key,
        name: name,
        description: description,
        createdBy: {
          name: currentUser.displayName,
          image: currentUser.photoURL
        }
      }

      try {
        await update(child(chatRoomsRef, key), newChatRoom)
        setName('')
        setDescription('')
        setShow(false)
      }
      catch (error) {
        alert(error)
      }

    }
  }

  const addChatRoomsListners = () => {
    let chatRoomsArray = []

    onChildAdded(chatRoomsRef, DataSnapshot => {
      chatRoomsArray.push(DataSnapshot.val())
      const newChatRooms = [...chatRoomsArray]
      setChatRooms(newChatRooms)
    })
  }

  const isFormValid = (name, description) => {
    return name && description
  }

  const renderChatRooms = () => {
    return (
      chatRooms.length > 0 &&
        chatRooms.map(room => {
          return (
            <li
              key={room.id}
            >
              # {room.name}
            </li>
          )
        })
      )
    }

  return (
    <div>
      <div style={{
        position: 'relative',
        width: '100%',
        display: 'flex',
        alignItems: 'center'
      }}>
        <FaRegSmileWink style={{marginRight: 3}} />
        CHAT ROOMS {" "}
        <FaPlus style={{position: 'absolute', right:0, cursor: 'pointer'}} onClick={() => setShow(!show)} />
      </div>

      <ul style={{listStyleType: 'none', padding: 0}}>
        {renderChatRooms()}
      </ul>

      <Modal show={show} onHide={() => setShow(false)}>
        <Modal.Header closeButton>
          <Modal.Title>채팅 방 생성하기</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group>
              <Form.Label>방 이름</Form.Label>
              <Form.Control
                onChange={(e) => setName(e.target.value)}
                type='text'
                placeholder='채팅 방 이름을 입력하세요.'
              />
            </Form.Group>
            <Form.Group>
              <Form.Label>방 설명</Form.Label>
              <Form.Control
                onChange={(e) => setDescription(e.target.value)}
                type='text'
                placeholder='채팅 방 설명을 입력하세요.'
              />
            </Form.Group>
          </Form>
          </Modal.Body>
        <Modal.Footer>
          <Button variant='secondary' onClick={() => setShow(false)}>
            취소
          </Button>
          <Button variant='primary' onClick={handleSubmit} >
            생성
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  )
}

export default ChatRooms
