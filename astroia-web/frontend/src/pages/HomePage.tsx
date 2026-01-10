import { Sparkles } from 'lucide-react'

export function HomePage() {
  return (
    <div className="max-w-4xl mx-auto text-center py-16">
      <div className="inline-flex items-center justify-center w-20 h-20 bg-purple-100 rounded-full mb-8">
        <Sparkles className="w-10 h-10 text-purple-600" />
      </div>

      <h1 className="text-5xl font-bold text-gray-900 mb-4">
        Bienvenue sur Astro.IA
      </h1>

      <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
        L'astrologie moderne propulsée par l'intelligence artificielle.
        Découvrez votre thème natal, analysez vos relations, et explorez
        les mystères cosmiques avec la puissance du ML.
      </p>

      <div className="flex items-center justify-center gap-4">
        <button className="px-6 py-3 bg-purple-600 text-white rounded-lg font-semibold hover:bg-purple-700 transition-colors">
          Commencer
        </button>
        <button className="px-6 py-3 bg-white text-gray-700 rounded-lg font-semibold border border-gray-300 hover:bg-gray-50 transition-colors">
          En savoir plus
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16">
        <FeatureCard
          icon="🌙"
          title="Thème Natal"
          description="Calculez votre carte du ciel avec précision astronomique"
        />
        <FeatureCard
          icon="💫"
          title="IA Astrologique"
          description="Conseils personnalisés par intelligence artificielle"
        />
        <FeatureCard
          icon="🤝"
          title="Compatibilité"
          description="Analysez vos relations avec le Machine Learning"
        />
      </div>
    </div>
  )
}

interface FeatureCardProps {
  icon: string
  title: string
  description: string
}

function FeatureCard({ icon, title, description }: FeatureCardProps) {
  return (
    <div className="p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow">
      <div className="text-4xl mb-4">{icon}</div>
      <h3 className="text-lg font-semibold text-gray-900 mb-2">{title}</h3>
      <p className="text-gray-600 text-sm">{description}</p>
    </div>
  )
}

