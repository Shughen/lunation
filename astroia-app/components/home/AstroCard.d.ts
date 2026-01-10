// Déclaration de type pour AstroCard (composant JS)
declare module '@/components/home/AstroCard' {
  import { ComponentType } from 'react';

  interface AstroCardProps {
    moonSign: string;
    energyText: string;
    onPress: () => void;
  }

  const AstroCard: ComponentType<AstroCardProps>;
  export default AstroCard;
}

