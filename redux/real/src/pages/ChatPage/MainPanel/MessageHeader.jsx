import React, { useEffect, useState } from 'react'
import { Accordion, Col, FormControl, FormGroup, Image, InputGroup, Row } from 'react-bootstrap'
import { useSelector } from 'react-redux'
import {AiOutlineSearch} from 'react-icons/ai'
import { FaLock, FaLockOpen } from 'react-icons/fa'
import {MdFavorite, MdFavoriteBorder} from 'react-icons/md'
import { child, ref, update, remove, onValue } from 'firebase/database'
import { db } from '../../../firebase'

const MessageHeader = ({handleSearchChange}) => {

  const {userPosts} = useSelector(state => state.chatRoom)

  const {currentChatRoom} = useSelector(state => state.chatRoom)
  const {isPrivateChatRoom} = useSelector(state => state.chatRoom)
  const [isFavorite, setIsFavorite] = useState(false)
  const usersRef = ref(db, 'users')

  const {currentUser} = useSelector(state => state.user) 

  useEffect(() => {
    if (currentChatRoom?.id && currentUser?.uid) {
      addFavoriteListener(currentChatRoom.id, currentUser.uid)
    }
  
  }, [currentChatRoom?.id, currentUser?.uid])

  const addFavoriteListener = (chatRoomId, userId) => {
    onValue(child(usersRef, `${userId}/favorite`), data => {
      if (data.val() !== null) {
        const chatRoomIds = Object.keys(data.val())
        const isAlreadyFavorite = chatRoomIds.includes(chatRoomId)
        setIsFavorite(isAlreadyFavorite)
      }
    })
  }

  const handleFavorite = () => {
    if (isFavorite) {
      setIsFavorite(false)
      remove(child(usersRef, `${currentUser.uid}/favorite/${currentChatRoom.id}`))
    }
    else {
      setIsFavorite(true)
      update(child(usersRef, `${currentUser.uid}/favorite`), {
        [currentChatRoom.id] : {
          name: currentChatRoom.name,
          description: currentChatRoom.description,
          createdBy: {
            name: currentChatRoom.createdBy.name,
            image: currentChatRoom.createdBy.image
          }
        }
      })
    }
  }

  const renderUserPosts = (userPosts) => {
    return(
      Object.entries(userPosts).sort((a, b) => b[1].count - a[1].count).map(([key, val], i) => (
        <div key={i} style={{display: 'flex'}}>
          <Image
            style={{width: 45, height: 45, marginRight: 10}}
            roundedCircle
            src={val.image}
            alt={key}
          />
          <div>
            <h6>{key}</h6>
            <p>
              {val.count} 개
            </p>
          </div>
        </div>
      ))
    )
  }

  return (
    <div
      style={{
        width: '100%',
        border: '0.2rem solid #ececec',
        borderRadius: '4px',
        height: '190px',
        padding: '1rem',
        marginBottom: '1rem'
      }}
    >
      <Row>
        <Col>
        <h2>
          {isPrivateChatRoom
          ? <FaLock style={{marginBottom: 10}} />
          : <FaLockOpen style={{marginBottom: 10}} />
          }
          {' '}
          <span>{currentChatRoom?.name}</span>
          {' '}
          {!isPrivateChatRoom &&
          <span style={{cursor: 'pointer'}} onClick={handleFavorite}>
            {isFavorite
            ? <MdFavorite style={{marginBottom: 10}} />
            : <MdFavoriteBorder style={{marginBottom: 10}} />
            }
          </span>
          }
        </h2>
        </Col>
        <Col>
          <InputGroup>
            <InputGroup.Text>
              <AiOutlineSearch />
            </InputGroup.Text>
            <FormControl
              onChange={handleSearchChange}
              placeholder='Search Messages'
            />
          </InputGroup>
        </Col>
      </Row>
      {!isPrivateChatRoom &&      
      <div style={{display: 'flex', justifyContent: 'flex-end'}}>
        <Image
          roundedCircle
          src={currentChatRoom?.createdBy.image}
          style={{width: 30, height: 30, marginRight: 7}}
        />
        {" "}
        <p>{currentChatRoom?.createdBy.name}</p>
      </div>
      }

      <Row>
        <Col>
        <Accordion>
          <Accordion.Item eventKey='0'>
          <Accordion.Header>Description</Accordion.Header>
          <Accordion.Collapse eventKey='0'>
          <Accordion.Body>
            {currentChatRoom?.description}
          </Accordion.Body>
          </Accordion.Collapse>
          </Accordion.Item>
        </Accordion>
        </Col>
        <Col>
        <Accordion>
          <Accordion.Item eventKey='1'>
          <Accordion.Header>Posts Count</Accordion.Header>
          <Accordion.Collapse eventKey='1'>
          <Accordion.Body>
            {userPosts && renderUserPosts(userPosts)}
          </Accordion.Body>
          </Accordion.Collapse>
          </Accordion.Item>
        </Accordion>
        </Col>
      </Row>

    </div>
  )
}

export default MessageHeader