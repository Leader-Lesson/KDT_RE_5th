import { useSelector, useDispatch } from 'react-redux';
import { Box1, Box2, Box3 } from '../App4';
import { plus, minus } from '../store/counterReducer';

export const Box1Container = () => {
  return <Box1 />;
};

export const Box2Container = () => {
  return <Box2 />;
};

export const Box3Container = () => {
  const number = useSelector((state) => state.counter.number);
  const dispatch = useDispatch();

  return (
    <Box3
      number={number}
      onIncrease={() => dispatch(plus())}
      onDecrease={() => dispatch(minus())}
    />
  );
};
