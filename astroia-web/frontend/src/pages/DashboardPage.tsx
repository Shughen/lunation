import { useQuery } from '@tanstack/react-query'
import { Loader2 } from 'lucide-react'
import { dashboardService } from '@/services/dashboard'

export function DashboardPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['dashboard'],
    queryFn: dashboardService.getDashboardData,
  })

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-16">
        <Loader2 className="w-8 h-8 animate-spin text-purple-600" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center py-16">
        <p className="text-red-600">Erreur de chargement</p>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <StatCard
          title="Analyses"
          value={data?.stats.analyses || 0}
          trend="+12%"
        />
        <StatCard
          title="Prédictions"
          value={data?.stats.predictions || 0}
          trend="+5%"
        />
        <StatCard
          title="Précision ML"
          value={`${data?.stats.ml_accuracy || 0}%`}
          trend="+2%"
        />
      </div>

      <div className="mt-8 bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Activité récente</h2>
        <p className="text-gray-600">Aucune activité pour le moment</p>
      </div>
    </div>
  )
}

interface StatCardProps {
  title: string
  value: number | string
  trend: string
}

function StatCard({ title, value, trend }: StatCardProps) {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-sm font-medium text-gray-600 mb-2">{title}</h3>
      <div className="flex items-end justify-between">
        <p className="text-3xl font-bold text-gray-900">{value}</p>
        <span className="text-sm text-green-600 font-medium">{trend}</span>
      </div>
    </div>
  )
}

