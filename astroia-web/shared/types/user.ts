/**
 * Types liés aux utilisateurs
 */

export interface User {
  id: number;
  email: string;
  fullName?: string;
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface UserProfile {
  userId: number;
  birthDate?: Date;
  birthTime?: string; // Format: "HH:MM"
  birthPlace?: string;
  sunSign?: string;
  moonSign?: string;
  ascendant?: string;
}

export interface UserWithProfile extends User {
  profile?: UserProfile;
}

