import { useState, useRef } from 'react';

const RefFunction2 = () => {
  const idRef = useRef(1);
  const [id, setId] = useState(10);
  let test = 10; // 일반 변수 : 리렌더링 되면 해당 값 초기화 됨

  const plusIdRef = () => {
    idRef.current += 1;
    console.log(idRef.current);
    // ref 로컬 변수값은 바뀌지만 컴포넌트가 다시 렌더링 되진 않음 하지만 리렌더링 되어도 값 유지
    test += 1;
    console.log(test);
  };

  // state로 선언해둔 값은 업데이트 되면 컴포넌트가 다시 렌더링 됨
  const plusIdState = () => setId(id + 1);

  return (
    <div>
      <h1>Ref Sample</h1>
      <h2>{test}</h2>
      <h2>{idRef.current}</h2>
      <button onClick={plusIdRef}>PLUS Ref</button>

      <h2>{id}</h2>
      <button onClick={plusIdState}>PLUS State</button>
    </div>
  );
};

export default RefFunction2;
