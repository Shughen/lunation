// Déclaration de type pour CycleCard (composant JS)
declare module '@/components/home/CycleCard' {
  import { ComponentType } from 'react';

  interface CycleCardProps {
    dayLabel: string;
    phase: string;
    energy: string;
    fertile: boolean;
    onPress: () => void | Promise<void>;
  }

  const CycleCard: ComponentType<CycleCardProps>;
  export default CycleCard;
}

