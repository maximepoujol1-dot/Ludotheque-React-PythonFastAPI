import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <div>
        <Link to="/">Home</Link>
        <Link to="/collection">Collection</Link>
        <Link to="/account">Account</Link>
    </div>
  )
}

export default Navbar