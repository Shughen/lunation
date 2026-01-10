// Déclaration de type pour MoodCard (composant JS)
declare module '@/components/home/MoodCard' {
  import { ComponentType } from 'react';

  interface MoodCardProps {
    onOpenJournal: () => void;
  }

  const MoodCard: ComponentType<MoodCardProps>;
  export default MoodCard;
}

