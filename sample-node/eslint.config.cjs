const js = require('@eslint/js');
const prettier = require('eslint-config-prettier');

module.exports = [
  {
    ...js.configs.recommended,
  },
  ...prettier(),
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {},
    },
    linterOptions: {
      ignorePatterns: ['dist/**', 'node_modules/**'],
    },
    rules: {
      semi: ['error', 'always'],
      'no-unused-vars': 'error',
    },
  },
];
