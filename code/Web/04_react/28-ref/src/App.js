import './App.css';
import Ex1 from './Ex1';
import RefClass1 from './RefClass1';
import RefClass2 from './RefClass2';
import RefFunction1 from './RefFunction1';
import RefFunction2 from './RefFunction2';

function App() {
  return (
    <div className='App'>
      {/* 클래스형 컴포넌트; ref 사용방법 1. 콜백함수  */}
      <RefClass1 />
      <hr />

      {/* 클래스형 컴포넌트; ref 사용방법 2. createRef()  */}
      <RefClass2 />
      <hr />

      {/* 함수형 컴포넌트; useRef()로 DOM 요소에 직접 접근 */}
      <RefFunction1 />
      <hr />

      {/* 함수형 컴포넌트; useRef()로 로컬변수 사용 */}
      <RefFunction2 />
      <hr />

      {/* 실습 */}
      <Ex1 />
      <hr />
    </div>
  );
}

export default App;
