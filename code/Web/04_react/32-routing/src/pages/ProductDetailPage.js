import React from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { productInfos } from '../components/ProductList';

export default function ProductDetailPage({ products }) {
  const { productId } = useParams();
  console.log('useParams', useParams());
  console.log('productId', productId); // '2'

  // const targetProduct = productInfos[Number(productId) - 1];
  const product = products[Number(id) - 1];

  const navigate = useNavigate();
  return (
    <div>
      <h1>ProductDetailPage</h1>
      <button onClick={() => navigate(-1)}>뒤로가기</button>
      <button onClick={() => navigate('/')}>홈으로 이동하기</button>
      {/* products가 아직 불러와지지 않았을 경우 대비(직접 경로 치고 들어왔을 경우) */}
      {products.length !== 0 ? (
        <ul>
          <li>상품 번호 : {id}</li>
          <li>상품명 : {product.name}</li>
          <li>판매자 : {product.email}</li>
          <li>상세 설명 : {product.body}</li>
        </ul>
      ) : (
        <div>Loading...</div>
      )}
    </div>
  );
}
