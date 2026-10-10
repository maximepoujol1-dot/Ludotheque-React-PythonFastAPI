import Card from '../components/Card'
import Button from '../components/Button'
import { Link } from 'react-router-dom';

const tabBase = "px-6 py-2 font-semibold transition-colors cursor-pointer border-b-2"
const cardStyle = "flex flex-col w-full max-w-sm p-8 card bg-white dark:bg-dark-surface shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl"
const titleStyle = "text-sm font-semibold text-gray-600 dark:text-gray-300 mt-2"
const inputStyle = "input validator w-full bg-gray-50 dark:bg-white/5 text-gray-900 dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500 border border-gray-300 dark:border-white/10 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white dark:focus:bg-white/10 focus:border-green-500 focus:ring-2 focus:ring-green-200 dark:focus:ring-green-500/30"
const buttonStyle = "mt-6 w-full py-2 rounded-lg bg-green-500 text-white font-semibold shadow-md transition hover:bg-green-600 active:scale-95 cursor-pointer"

const LoginPage = () => {
  return (
    <div className="flex min-h-screen flex-col md:flex-row items-center justify-center">
      
      <div className="flex flex-1 flex-col items-center justify-center px-4 py-12">
        <div className="flex flex-col md:flex-row justify-center items-stretch gap-6 w-full max-w-3xl min-h-[500px]">
               
        <Card title={"Login"} style={cardStyle}>
          <div className="flex flex-col gap-2 mt-4">
					  <h2 className={titleStyle}>Email</h2>
            <input className={inputStyle} type="email" required placeholder="mail@site.com" />
					  <h2 className={titleStyle}>password</h2>
            <input className={inputStyle} type="password" required placeholder="your password" />
            <button className={buttonStyle}>submit</button>
            <div className="flex justify-center items-center gap-2 mt-8">
            <Link to="/register"><li className={tabBase}>Register</li></Link>
            </div>
          </div>
        </Card>
      </div>
        
      </div>
      
      <div className="flex flex-1 items-center justify-center p-8">
        <img src="src/assets/font.png" alt="Illustration de connexion" className="h-full w-full object-cover rounded-2xl"/>
      </div> 
    </div>
	)
}

export default LoginPage