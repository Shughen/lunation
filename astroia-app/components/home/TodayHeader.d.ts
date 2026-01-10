// Déclaration de type pour TodayHeader (composant JS)
declare module '@/components/home/TodayHeader' {
  import { ComponentType } from 'react';

  interface TodayHeaderProps {
    cycleLabel: string;
    moonLabel: string;
    mantra?: string;
  }

  const TodayHeader: ComponentType<TodayHeaderProps>;
  export default TodayHeader;
}

