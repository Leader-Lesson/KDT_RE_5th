import React from 'react';
import ProductList from '../components/ProductList';

export default function ProductPage({ products }) {
  return (
    <div>
      <h1>ProductPage</h1>
      <ProductList products={products} />
    </div>
  );
}
