import Counter from './counter/counter'
import Todos from './todos/todos'
import { Link } from 'react-router-dom'


function Main() {

  return (
    <>
      <Counter />
      <hr />
      <Todos />
      <Link to={'/test'}>move</Link>
    </>
  )
}

export default Main