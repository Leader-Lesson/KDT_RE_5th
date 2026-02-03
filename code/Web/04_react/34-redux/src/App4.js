import { useSelector } from 'react-redux';
import {
  Box1Container,
  Box2Container,
  Box3Container,
} from './containers/BoxesContainer';
// import Bank from './components/Bank';
// import { BankContainer } from './containers/BankContainers';

import './styles/Box.css';

// redux 적용
function App4() {
  const number = useSelector((state) => state.counter.number);

  return (
    <div className="App4">
      <h1>React Redux 실습</h1>
      {/* <h2>number: {number}</h2> */}
      <Box1Container />
      <hr />
      {/* <BankContainer /> */}
    </div>
  );
}

export const Box1 = () => {
  return (
    <div className="Box">
      <h2>Box1</h2>
      <Box2Container />
    </div>
  );
};

export const Box2 = () => {
  return (
    <div className="Box">
      <h2>Box2</h2>
      <Box3Container />
    </div>
  );
};

export const Box3 = ({ number, onIncrease, onDecrease }) => {
  console.log('number', number);
  return (
    <div className="Box">
      <h2>Box3: {number}</h2>

      <button onClick={onIncrease}>PLUS</button>
      <button onClick={onDecrease}>MINUS</button>
    </div>
  );
};

export default App4;
