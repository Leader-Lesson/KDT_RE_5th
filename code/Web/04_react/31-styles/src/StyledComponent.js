import React from 'react';
import styled from 'styled-components';

// CSS in JS: js 안에 css를 작성함
// styled-components, emotion, styled-jsx, ...
// 각 컴포넌트마다 격리된 스타일 적용가능
const StyledContainer = styled.div`
  display: flex;
`;

const StyledBox = styled.div`
  width: 100px;
  height: 100px;
  /* 
    styled-components 에 props 보낼 때 나오는 dom 관련 warning!
    props 변수 앞에 $ 붙여서 실제 HTML 요소에는 전달되지 않도록 하기!
    https://velog.io/@hyerin0930/React-styled-component%EC%97%90-props-%EB%B3%B4%EB%82%BC-%EB%95%8C-%EB%82%98%EC%98%A4%EB%8A%94-warning-%ED%95%B4%EA%B2%B0 
  */
  background-color: ${(props) => props.$bgColor || 'blue'};

  &:hover {
    transform: translateY(-20px);
  }
`;

export default function StyledComponent() {
  return (
    <StyledContainer>
      <StyledBox $bgColor="red"></StyledBox>
      <StyledBox $bgColor="orange"></StyledBox>
      <StyledBox $bgColor="yellow"></StyledBox>
      <StyledBox></StyledBox>
    </StyledContainer>
  );
}
