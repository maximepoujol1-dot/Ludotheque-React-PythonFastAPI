import React from 'react'
import Card from './Card'

const RegisterForm = () => {
	return (
		<Card title={"Register"} style={"flex flex-col w-full max-w-sm p-8 card bg-white shadow-xl border border-gray-200 border-t-4 border-t-orange-500 rounded-2xl"}>
                  <div className="flex flex-col gap-2 mt-4">
					          <h2 className="text-sm font-semibold text-gray-600 mt-2">Email</h2>
                      <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="email" required placeholder="mail@site.com" />
					            <h2 className="text-sm font-semibold text-gray-600 mt-2">password</h2>
                      <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="password" required placeholder="your password" />
                      <button className="mt-6 w-full py-2 rounded-lg bg-orange-500 text-white font-semibold shadow-md transition hover:bg-orange-600 active:scale-95 cursor-pointer">submit</button>
                  </div>
                </Card>
	)
}

export default RegisterForm

