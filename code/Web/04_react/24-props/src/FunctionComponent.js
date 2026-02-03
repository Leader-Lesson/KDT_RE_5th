import PropTypes from 'prop-types';

export default function FunctionComponent({ name = '기본 이름' }) {
  const student = '홍길동';
  const { name } = props;
  return (
    <div>
      <h1>Hi {student}!</h1>
      <p>여기는 FunctionComponent</p>
      {/* <p>
        새로운 컴포넌트의 이름은 <b>{props.name}</b>
      </p> */}
      <p>
        새로운 컴포넌트의 이름은 <b>{name}</b>
      </p>
    </div>
  );
}

// 18.3 부터 deprecated warning 표시됨 (아마 19버전부터 안될 것 같음)
// FunctionComponent.defaultProps = {
//   name: '기본 이름',
// };

FunctionComponent.propTypes = {
  name: PropTypes.string,
};
