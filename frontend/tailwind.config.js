/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Custom brand colors for My Dolla $ign
        'dolla': {
          'green': '#22c55e',
          'dark': '#15803d',
          'light': '#86efac',
        }
      }
    },
  },
  plugins: [],
}
