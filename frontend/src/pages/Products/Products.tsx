import { useEffect, useState } from "react";
import api from "../../services/api";
import Loader from "../../components/common/Loader";
import ErrorMessage from "../../components/common/ErrorMessage";

interface Product {
  id: number;
  name: string;
  price: number;
}

export default function Products() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res = await api.get<Product[]>("/products");
        setProducts(res.data);
      } catch (err) {
        console.error(err);
        setError("Failed to load products");
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) return <Loader />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Products</h2>

      <div className="bg-white rounded shadow overflow-hidden">
        {products.length === 0 ? (
          <div className="p-4 text-gray-500">No products found.</div>
        ) : (
          products.map((product) => (
            <div
              key={product.id}
              className="p-4 border-b last:border-none flex justify-between"
            >
              <span>{product.name}</span>
              <span className="font-semibold">${product.price}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
