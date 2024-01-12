import React from 'react'
import MessageHeader from './MessageHeader'
import MessageForm from './MessageForm'


const MainPanel = () => {
  return (
    <div style={{padding: '2rem 2rem 0 2rem'}}>
      <MessageHeader />
      <div style={{
        width: '100%',
        height: 450,
        border: '0.2rem solid #ececec',
        borderRadius: '4px',
        padding: '1rem',
        marginBottom: '1rem',
        overflow: 'auto'
      }}>

      </div>
      <MessageForm />
    </div>
  )
}

export default MainPanel