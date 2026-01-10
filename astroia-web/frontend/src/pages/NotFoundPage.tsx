import { Link } from 'react-router-dom'
import { Home } from 'lucide-react'

export function NotFoundPage() {
  return (
    <div className="max-w-2xl mx-auto text-center py-16">
      <h1 className="text-9xl font-bold text-gray-200 mb-4">404</h1>
      <h2 className="text-3xl font-bold text-gray-900 mb-4">
        Page non trouvée
      </h2>
      <p className="text-gray-600 mb-8">
        La page que vous recherchez semble avoir disparu dans les étoiles...
      </p>
      <Link
        to="/"
        className="inline-flex items-center gap-2 px-6 py-3 bg-purple-600 text-white rounded-lg font-semibold hover:bg-purple-700 transition-colors"
      >
        <Home size={20} />
        Retour à l'accueil
      </Link>
    </div>
  )
}

