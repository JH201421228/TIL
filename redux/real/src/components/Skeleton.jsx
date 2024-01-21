import React from 'react'
import './Skeleton.css'

const Skeleton = () => {
  return (
    <div className='skeleton'>
      <div className='skeleton-avatar'></div>
      <div className='skeleton-author'></div>
      <div className='skeleton-description'></div>
    </div>
  )
}

export default Skeleton