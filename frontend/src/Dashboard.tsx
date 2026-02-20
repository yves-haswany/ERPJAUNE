export default function Dashboard() {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>

      <div className="grid grid-cols-3 gap-4">
        <div className="bg-white p-6 rounded shadow">
          <p className="text-gray-500">Total Sales</p>
          <h3 className="text-xl font-bold">$12,340</h3>
        </div>

        <div className="bg-white p-6 rounded shadow">
          <p className="text-gray-500">Products</p>
          <h3 className="text-xl font-bold">128</h3>
        </div>

        <div className="bg-white p-6 rounded shadow">
          <p className="text-gray-500">Users</p>
          <h3 className="text-xl font-bold">54</h3>
        </div>
      </div>
    </div>
  );
}
