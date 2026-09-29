import { Link } from 'react-router-dom'
import Button from './Button'

const linkStyle ='text-gray-700 hover:text-orange-500 transition-colors border-b-2 border-transparent hover:border-orange-500 pb-1 cursor-pointer'

const Navbar = () => {

  function swipTheme(){
    return
  }
    
  function swipLangage(){
    return
  }

  return (
    <nav className='sticky top-0 z-50'>
      <div className='h-[14vh] min-h-[80px] w-full flex items-center justify-between px-6 md:px-20 border-b border-gray-200 bg-white/90 backdrop-blur shadow-sm'>
        <div className='flex items-center'>
            <Link to="/"><h2 className='text-3xl font-bold text-orange-500 hover:text-orange-600 transition-colors tracking-tight'>Micromaniac</h2></Link>
        </div>

        <div>
          <input
            className="w-64 lg:w-80 px-4 py-2 rounded-full border border-gray-300 bg-gray-50 text-gray-700 placeholder-gray-400 transition focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200"
            type="search"
            required
            placeholder="search a game"
          />
        </div>

        <div>
          <ul className='flex items-center gap-8 text-[17px] font-medium'>
            <Link to="/collection"><li className={linkStyle}>My collection</li></Link>
            <Link to="/account"><li className={linkStyle}>account</li></Link>
            <Button style={linkStyle} title={'Langage'} action={()=>swipLangage()}></Button>
            <Button style={linkStyle} title={'Theme'} action={()=>swipTheme()}></Button>
          </ul>
        </div>
      </div>
    </nav>
    )
}

export default Navbar