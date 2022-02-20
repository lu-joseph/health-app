const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    colors:{
      'customblue':'#6E7DE8',
      'custombluebutton':'#4F78E3',
      'white':colors.white,
      'black':colors.black,
      'red':'#C51616',
      'yellow':'#FDD137',
      'green':'#55AD53',
      'bluelight':"#748FD6",
      'bluemed':"#4F78E3",
      'bluedark':"#093199"
    },
    boxShadow:{
      "md": '0 0 15px -3px rgb(0 0 0 / 0.2), 0 4px 6px -4px rgb(0 0 0 / 0.1)'
    },
    extend: {
      spacing: {
        '2screen':'200vh'
      }
    },
  },
  plugins: [],
}
