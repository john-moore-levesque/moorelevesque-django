const { fontFamily } = require('tailwindcss/defaultTheme')

module.exports = {
  content: ["./css/*.css"],
  theme: {
    extend: {
      fontFamily: {
         'sans': ['Noto Sans'],
         'serif': ['Noto Serif']
      }
    },
  },
  plugins: [],
}


