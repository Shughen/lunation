import { apiClient } from '@/lib/api'

export interface DashboardData {
  stats: {
    analyses: number
    predictions: number
    ml_accuracy: number
  }
}

export const dashboardService = {
  async getDashboardData(): Promise<DashboardData> {
    const { data } = await apiClient.get('/api/dashboard')
    return data
  },
}

