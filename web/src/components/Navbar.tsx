import { Link } from 'react-router-dom'
import Button from './Button'
import useToggle from '../hooks/toggle';
import { useEffect } from 'react';
import Avatar from './Avatar';

const linkStyle ="text-gray-700 dark:text-white hover:text-green-500 dark:hover:text-green-500 text-2xl transition-colors border-b-2 border-transparent hover:border-green-500 pb-1 cursor-pointer "

const sun = <img src="\src\assets\soleil.png" className="h-10 w-10 rounded-full object-cover" alt="Sun" />
const moon = <img src="\src\assets\moon.png" className="h-10 w-10 rounded-full object-cover" alt="Moon" />
const Navbar = () => {
  const [isDark, toggle] = useToggle(
    localStorage.getItem('theme') === 'dark'
  );

  useEffect(() => {
    document.documentElement.classList.toggle('dark', isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  }, [isDark]);

  return (
    <nav className='sticky top-0 z-50'>
      <div className='h-[14vh] min-h-[80px] w-full flex items-center justify-between px-6 md:px-20 border-b border-b border-gray-200 bg-white/90 shadow-sm backdrop-blur dark:border-white/10 dark:bg-dark-surface/90'>
        <div className='flex items-center'>
            <Link to="/"><h2 className='text-5xl font-bold text-green-500 tracking-tight transition-transform hover:scale-110'>Micromaniac</h2></Link>
        </div>

        <div>
          <ul className='flex items-center gap-8 text-[17px] font-medium'>
            <Link to="/collection"><li className={linkStyle}>My collection</li></Link>
            <Link to="/stat"><li className={linkStyle}>stat</li></Link>
            <Link to="/account"><Avatar/></Link>
            <Button style='flex h-10 w-10 shrink-0 items-center justify-center rounded-full p-0 transition-transform hover:scale-110' title={isDark ? sun : moon} action={toggle}></Button>
          </ul>
        </div>
      </div>
    </nav>
    )
}

export default Navbar