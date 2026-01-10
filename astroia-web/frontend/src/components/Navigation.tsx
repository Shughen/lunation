import { Link } from 'react-router-dom'
import { Home, LayoutDashboard, User } from 'lucide-react'

export function Navigation() {
  return (
    <nav className="bg-white shadow-sm">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center space-x-2">
            <span className="text-2xl">✨</span>
            <span className="font-bold text-xl text-gray-900">Astro.IA</span>
          </Link>

          <div className="flex items-center space-x-4">
            <NavLink to="/" icon={<Home size={20} />} label="Accueil" />
            <NavLink to="/dashboard" icon={<LayoutDashboard size={20} />} label="Dashboard" />
            <NavLink to="/profile" icon={<User size={20} />} label="Profil" />
          </div>
        </div>
      </div>
    </nav>
  )
}

interface NavLinkProps {
  to: string
  icon: React.ReactNode
  label: string
}

function NavLink({ to, icon, label }: NavLinkProps) {
  return (
    <Link
      to={to}
      className="flex items-center space-x-2 px-3 py-2 rounded-md text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
    >
      {icon}
      <span className="text-sm font-medium">{label}</span>
    </Link>
  )
}

