module.exports = {
  root: true,
  extends: ['expo'],
  env: {
    jest: true,
  },
  settings: {
    'import/resolver': {
      node: { extensions: ['.js', '.jsx'] }
    }
  },
  rules: {
    'import/no-unresolved': 'off',
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
  },
  overrides: [
    {
      files: ['**/*.ts', '**/*.tsx'],
      rules: {
        'no-unused-vars': 'off',
        '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_', varsIgnorePattern: '^_' }],
      },
    },
  ],
};

