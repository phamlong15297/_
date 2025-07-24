import js from '@eslint/js';
import prettier from 'eslint-config-prettier';
import pluginPrettierRecommended from 'eslint-plugin-prettier/configs/recommended';

export default [
  js.configs.recommended,
  prettier,
  pluginPrettierRecommended,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
      },
    },
    linterOptions: {
      // ignore patterns can be added here
      ignorePatterns: ['dist/**', 'node_modules/**'],
    },
    rules: {
      semi: ["error", "always"],
      "no-unused-vars": "error",
    },
  },
];

