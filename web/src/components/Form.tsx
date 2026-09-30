import Card from './Card'
import Button from './Button'
import useToggle from '../hooks/toggle'

const tabBase = "px-6 py-2 font-semibold transition-colors cursor-pointer border-b-2"
const tabActive = "text-orange-500 border-orange-500"
const tabInactive = "text-gray-500 border-transparent hover:text-orange-400"

const Form = () => {
  const [register, toggle] = useToggle(false);
	return (
    <div className="flex min-h-screen flex-col md:flex-row items-center justify-center">
      
      <div className="flex flex-1 flex-col items-center justify-center px-4 py-12">
        <div className="flex flex-col md:flex-row justify-center items-stretch gap-6 w-full max-w-3xl min-h-[500px]">
        {register ? 
        <Card title={"Register"} style={"flex flex-col w-full max-w-sm p-8 card bg-white shadow-xl border border-gray-200 border-t-4 border-t-orange-500 rounded-2xl"}>
          <div className="flex flex-col gap-2 mt-4">
					  <h2 className="text-sm font-semibold text-gray-600 mt-2">Email</h2>
            <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="email" required placeholder="mail@site.com" />
					  <h2 className="text-sm font-semibold text-gray-600 mt-2">password</h2>
            <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="password" required placeholder="your password" />
            <button className="mt-6 w-full py-2 rounded-lg bg-orange-500 text-white font-semibold shadow-md transition hover:bg-orange-600 active:scale-95 cursor-pointer">submit</button>
            <div className="flex justify-center items-center gap-2 mt-8">
            <Button title={register && 'login'} style={`${tabBase} ${register ? tabActive : tabInactive}`} action={toggle}/>
            
        </div>
          </div>
        </Card>
         : 
        <Card title={"Login"} style={"flex flex-col w-full max-w-sm p-8 card bg-white shadow-xl border border-gray-200 border-t-4 border-t-orange-500 rounded-2xl"}>
          <div className="flex flex-col gap-2 mt-4">
					  <h2 className="text-sm font-semibold text-gray-600 mt-2">Email</h2>
              <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="email" required placeholder="mail@site.com" />
					    <h2 className="text-sm font-semibold text-gray-600 mt-2">password</h2>
              <input className="input validator w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200" type="password" required placeholder="your password" />
              <button className="mt-6 w-full py-2 rounded-lg bg-orange-500 text-white font-semibold shadow-md transition hover:bg-orange-600 active:scale-95 cursor-pointer">submit</button>
              <div className="flex justify-center items-center gap-2 mt-8">
            <Button title={!register && 'register'} style={`${tabBase} ${register ? tabActive : tabInactive}`} action={toggle}/>
            </div>
          </div>
        </Card>}
      </div>
        
      </div>
      
      <div className="flex flex-1 items-center justify-center p-8">
        <img src="src/assets/font.png" alt="Illustration de connexion" className="h-full w-full object-cover rounded-2xl"/>
      </div> 
    </div>
	)
}

export default Form
