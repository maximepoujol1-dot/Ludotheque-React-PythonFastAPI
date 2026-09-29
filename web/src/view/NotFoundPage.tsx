import React from 'react'
import Card from '../components/Card'

const NotFoundPage = () => {
  return (
    <Card title={"Not Found : 404"} style={'max-w-md mx-auto my-20 p-10 text-center bg-white rounded-2xl shadow-lg border border-gray-200 border-t-4 border-t-orange-500'}>
      <>
        <p className='text-lg text-gray-500 mt-4'>nous sommes perdu</p>
        
      </>
    </Card>
  )
}

export default NotFoundPage