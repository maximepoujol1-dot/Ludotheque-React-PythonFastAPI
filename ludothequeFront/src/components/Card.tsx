import React from 'react'

interface CardProps {
  title: string
  children: React.ReactNode

}

const Card = ({title,children}:CardProps) => {
  return (
    <div>
      <h1>{title}</h1>
      {children}
    </div>
  )
}

export default Card