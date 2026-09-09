function ProductCard({ product }) {
  return (
    <div className="product-card">

      <div className="product-image">
        🛍️
      </div>

      <div className="product-info">

        <h2>{product.name}</h2>

        <p className="description">
          {product.description}
        </p>

        <h3>
          ₹{Number(product.price).toLocaleString("en-IN")}
        </h3>

        <p className="stock">
          Stock: {product.stock}
        </p>

        <button className="cart-button">
          Add to Cart
        </button>

      </div>

    </div>
  );
}

export default ProductCard;