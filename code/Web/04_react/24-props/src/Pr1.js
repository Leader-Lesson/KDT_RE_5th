export default function Pr1({ food = "피자" }) {
  return (
    <h1>
      제가 좋아하는 음식은
      <span style={{ color: "red" }}> {food}</span>
      입니다.
    </h1>
  );
}
