/**
 * MarkdownText Component
 * Parse markdown simple pour React Native
 *
 * Supporte:
 * - **gras** → fontWeight: 'bold'
 * - Retours à la ligne
 */

import React from 'react';
import { Text, TextStyle } from 'react-native';

interface MarkdownTextProps {
  children: string;
  style?: TextStyle;
}

interface TextSegment {
  text: string;
  bold: boolean;
}

/**
 * Parse une string markdown simple et retourne des segments
 * Ex: "Hello **world** test" → [
 *   { text: "Hello ", bold: false },
 *   { text: "world", bold: true },
 *   { text: " test", bold: false }
 * ]
 */
function parseMarkdown(text: string): TextSegment[] {
  const segments: TextSegment[] = [];
  const regex = /\*\*(.+?)\*\*/g;

  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = regex.exec(text)) !== null) {
    // Texte avant le gras
    if (match.index > lastIndex) {
      segments.push({
        text: text.substring(lastIndex, match.index),
        bold: false,
      });
    }

    // Texte en gras (groupe capturé)
    segments.push({
      text: match[1],
      bold: true,
    });

    lastIndex = regex.lastIndex;
  }

  // Texte restant après le dernier match
  if (lastIndex < text.length) {
    segments.push({
      text: text.substring(lastIndex),
      bold: false,
    });
  }

  // Si aucun match, retourner tout le texte
  if (segments.length === 0) {
    segments.push({ text, bold: false });
  }

  return segments;
}

export function MarkdownText({ children, style }: MarkdownTextProps) {
  const segments = parseMarkdown(children);

  return (
    <Text style={style}>
      {segments.map((segment, index) => (
        <Text
          key={index}
          style={segment.bold ? { fontWeight: 'bold' } : undefined}
        >
          {segment.text}
        </Text>
      ))}
    </Text>
  );
}
