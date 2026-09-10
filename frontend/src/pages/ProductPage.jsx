import { useEffect, useState } from "react";
import API from "../services/api";
import ProductCard from "../components/ProductCard";

function ProductPage() {

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {

    const fetchProducts = async () => {

      try {

        const response = await API.get("/products");

        setProducts(response.data);

      } catch (error) {

        console.error(error);

        setError("Failed to load products.");

      } finally {

        setLoading(false);

      }

    };

    fetchProducts();

  }, []);

  return (
    <div className="product-page">

      {/* Navbar */}

      <nav className="navbar">

        <div className="logo">
          MyShop
        </div>

        <div className="nav-links">
          <a href="/">Home</a>
          <a href="/products">Products</a>
          <a href="/cart">Cart 🛒</a>
        </div>

      </nav>


      {/* Page Header */}

      <section className="page-header">

        <h1>Our Products</h1>

        <p>
          Discover our latest products
        </p>

      </section>


      {/* Loading */}

      {loading && (
        <div className="message">
          Loading products...
        </div>
      )}


      {/* Error */}

      {error && (
        <div className="error">
          {error}
        </div>
      )}


      {/* Products */}

      {!loading && !error && (

        <div className="product-grid">

          {products.map((product) => (

            <ProductCard
              key={product.id}
              product={product}
            />

          ))}

        </div>

      )}

    </div>
  );
}

export default ProductPage;