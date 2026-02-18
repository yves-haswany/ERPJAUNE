import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>ERP Jaune Dashboard</h1>
      <nav>
        <Link to="/products">Products</Link>
      </nav>
    </div>
  );
}
