import { useAuth } from "./AuthContext";

export default function Topbar() {
  const { logout } = useAuth();

  return (
    <header className="h-16 bg-white shadow flex items-center justify-between px-6">
      <h1 className="text-lg font-semibold">ERP Dashboard</h1>

      <button
        onClick={logout}
        className="bg-red-500 text-white px-4 py-2 rounded hover:opacity-90"
      >
        Logout
      </button>
    </header>
  );
}
