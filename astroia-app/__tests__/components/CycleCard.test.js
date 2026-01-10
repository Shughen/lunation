/**
 * Tests pour CycleCard
 */

import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react-native';
import CycleCard from '@/components/home/CycleCard';

describe('CycleCard', () => {
  it('affiche correctement les données du cycle', () => {
    const mockOnPress = jest.fn();
    const { getByText } = render(
      <CycleCard
        phase="Ovulation"
        dayLabel="Jour 15"
        energy="Haute"
        fertile={true}
        onPress={mockOnPress}
      />
    );

    expect(getByText("Mon cycle aujourd'hui")).toBeTruthy();
    expect(getByText(/Jour 15/)).toBeTruthy();
    expect(getByText(/Ovulation/)).toBeTruthy();
    expect(getByText(/Haute/)).toBeTruthy();
    expect(getByText(/Phase fertile/)).toBeTruthy();
  });

  it('affiche le CTA de configuration si cycle non configuré', () => {
    const mockOnPress = jest.fn();
    const { getByText } = render(
      <CycleCard
        phase="Configure ton cycle"
        dayLabel="Commence ici"
        energy="—"
        fertile={false}
        onPress={mockOnPress}
      />
    );

    expect(getByText(/Configure ton cycle/)).toBeTruthy();
  });

  it('appelle onPress au tap', () => {
    const mockOnPress = jest.fn();
    render(
      <CycleCard
        phase="Ovulation"
        dayLabel="Jour 15"
        energy="Haute"
        fertile={true}
        onPress={mockOnPress}
      />
    );

    const button = screen.getByRole('button');
    fireEvent.press(button);

    expect(mockOnPress).toHaveBeenCalledTimes(1);
  });

  it('a un label d\'accessibilité approprié', () => {
    const mockOnPress = jest.fn();
    render(
      <CycleCard
        phase="Ovulation"
        dayLabel="Jour 15"
        energy="Haute"
        fertile={true}
        onPress={mockOnPress}
      />
    );

    const button = screen.getByLabelText(/Mon cycle aujourd'hui/);
    expect(button).toBeTruthy();
  });
});

