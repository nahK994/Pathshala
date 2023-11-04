import './nav-bar.css'

function NavBar(props) {
  return (
    <div className='common'>
      <div className='top-bar'>haha</div>
      <div className='container'>{props.content}</div>
    </div>
  );
}

export default NavBar;
