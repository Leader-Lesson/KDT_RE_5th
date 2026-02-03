import React, { useState } from 'react';

export default function UseMemoPrac() {
  const [text, setText] = useState('');
  const [searchWord, setSearchWord] = useState('');

  // useMemo를 사용하여 단어 빈도수 계산 결과를 메모이제이션
  const countWord = useMemo(() => {
    // 입력받은 문자열와 찾고자 하는 단어가 빈 문자열이 아닌 경우에만 계산
    if (text.trim() && searchWord.trim()) {
      const words = text.split(' ');
      return words.filter((word) => word.includes(searchWord)).length;
    }
    // 빈 문자열인 경우 0 반환
    return 0;
  }, [text, searchWord]);
  return (
    <div>
      <h1>UseMemoPrac</h1>
      <input
        type='text'
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder='텍스트를 입력하세요'
      />
      <input
        type='text'
        value={searchWord}
        onChange={(e) => setSearchWord(e.target.value)}
        placeholder='찾을 단어를 입력하세요'
      />
      <p>
        "{searchWord}" 단어의 빈도수: {countWord}
      </p>
    </div>
  );
}
