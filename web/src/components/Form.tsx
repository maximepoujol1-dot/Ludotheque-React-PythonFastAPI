import React, { useState } from 'react'
import Card from './Card'
import LoginForm from './LoginForm'
import RegisterForm from './registerForm'
import Button from './Button'

const tabBase = "px-6 py-2 font-semibold transition-colors cursor-pointer border-b-2"
const tabActive = "text-orange-500 border-orange-500"
const tabInactive = "text-gray-500 border-transparent hover:text-orange-400"

const Form = () => {
  const [register, setRegister] = useState(true)
	return (
		<div className="px-4 py-12">
      <div className="flex flex-col md:flex-row justify-center items-stretch gap-6">
        
				
				{register ? <RegisterForm></RegisterForm> : <LoginForm></LoginForm>}
				
        </div>
        <div className="flex justify-center items-center gap-2 mt-8">
          <Button title={'register'} style={`${tabBase} ${register ? tabActive : tabInactive}`} action={() =>setRegister(true)}/>
          <div className="w-px h-6 bg-gray-300"></div>
          <Button title={'login'} style={`${tabBase} ${!register ? tabActive : tabInactive}`} action={()=>setRegister(false)}/>
        </div>
		</div>
	)
}

export default Form
