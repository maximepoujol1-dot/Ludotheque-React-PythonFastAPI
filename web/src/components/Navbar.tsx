import { Link } from 'react-router-dom'
import Button from './Button'

const Navbar = () => {

  function swipTheme(){
    return
  }
    
  function swipLangage(){
    return
  }

  return (
  <div className="flex gap-4">
        <Link to="/">Home</Link>
        <Link to="/collection">Collection</Link>
        <Link to="/account">Account</Link>
        <Button title={'Langage'} action={()=>swipLangage()}></Button>
        <Button title={'Theme'} action={()=>swipTheme()}></Button>
    </div>
  )
}

export default Navbar