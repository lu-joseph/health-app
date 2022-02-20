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
      'bluedark':"#093199",
      'peach':'#FF8C38',
      'blueish':"#25B0B9",
      'gray':'rgb(156 163 175)'
    },
    boxShadow:{
      "md": '0 0 15px -3px rgb(0 0 0 / 0.2), 0 4px 6px -4px rgb(0 0 0 / 0.1)'
    },
    extend: {
      spacing: {
        '2screen':'200vh',
        '100%':'100%',
        '5%':'5%',
        '90%':'90%'
      },
      gridTemplateRows:{
        'dash': "1fr 2em 3fr 3fr 3fr"
      },
      fontFamily:{
        'montserrat':["Montserrat",'sans-serif']
      }
    },
  },
  plugins: [],
}
