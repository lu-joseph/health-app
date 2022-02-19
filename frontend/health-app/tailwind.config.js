const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    colors:{
      'customblue':'#6E7DE8',
      'white':colors.white,
      'black':colors.black
    },
    extend: {
      spacing: {
        '2screen':'200vh'
      }
    },
  },
  plugins: [],
}
