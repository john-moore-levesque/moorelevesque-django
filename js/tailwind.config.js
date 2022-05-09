const { fontFamily } = require('tailwindcss/defaultTheme')

module.exports = {
  content: ["./css/*.css"],
  theme: {
    extend: {
      fontSize: {
        'body': '0.95rem',
      },
      fontFamily: {
         'sans': ['Noto Sans'],
         'serif': ['Noto Serif']
      }
    },
  },
  plugins: [],
}


