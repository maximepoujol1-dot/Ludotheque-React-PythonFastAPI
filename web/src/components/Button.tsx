import React from 'react'

interface ButtonProps {
  title: React.ReactNode | string
  style: string
  action: () => void
}

const Button = ({ title, style, action }: ButtonProps) => {
  return (
    <button type="button" className={style} onClick={action}>
      {title}
    </button>
  )
}

export default Button