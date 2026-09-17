import React from 'react'

interface ButtonProps {
  title: string
  action: ()=> void

}

const Button = ({title,action}:ButtonProps) => {
  return (
    <button onClick={()=>action}>{title}</button>
  )
}

export default Button