import React from 'react'
import { Col, FormControl, FormGroup, Image, InputGroup, Row } from 'react-bootstrap'
import { useSelector } from 'react-redux'
import {AiOutlineSearch} from 'react-icons/ai'

const MessageHeader = () => {

  const {currentChatRoom} = useSelector(state => state.chatRoom)

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
        </Col>
        <Col>
          <InputGroup>
            <InputGroup.Text>
              <AiOutlineSearch />
            </InputGroup.Text>
            <FormControl
              onChange
              placeholder='Search Messages'
            />
          </InputGroup>
        </Col>
      </Row>
      <div style={{display: 'flex', justifyContent: 'flex-end'}}>
        <Image
          roundedCircle
          src={currentChatRoom?.createdBy.image}
          style={{width: 30, height: 30, marginRight: 7}}
        />
        {" "}
        <p>{currentChatRoom?.createdBy.name}</p>
      </div>
    </div>
  )
}

export default MessageHeader