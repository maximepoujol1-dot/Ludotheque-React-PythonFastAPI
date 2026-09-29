import React from 'react'

interface ButtonProps {
  title: string
  style: string
  action: ()=> void

}

const Button = ({title,style,action}:ButtonProps) => {
  return (
    <button className={style} onClick={action}>{title}</button>
  )
}

export default Button