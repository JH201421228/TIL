import React, { useState } from 'react'
import { Button, Modal } from 'react-bootstrap'
import {FaPlus, FaRegSmileWink} from 'react-icons/fa'
import { Form } from 'react-router-dom'

const ChatRooms = () => {
  const [show, setShow] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')

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
        <FaPlus onClick={() => setShow(!show)} />
      </div>
      <Modal>
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
          <Button variant='primary' >
            생성
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  )
}

export default ChatRooms