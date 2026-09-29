import React from 'react'

interface CardProps {
  title: string
    style: string
  children: React.ReactNode

}

const Card = ({title,style,children}:CardProps) => {
  return (
    <div className={style}>
      <h1>{title}</h1>
      {children}
    </div>
  )
}

export default Card