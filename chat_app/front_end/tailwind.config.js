module.exports = {
  purge: {
    enabled: true,
    content: [
      "./src/**/*.{js,jsx,ts,tsx}",
      "./src/components/App.js",
      "./templates/front_end/index.html",
      "./src/**/*.html",
      "./src/**/*.vue",
      "./src/**/*.js",
      "./src/**/*.jsx",
    ],
    options: {
      keyframes: true,
    },
  },

  darkMode: false, // or 'media' or 'class'
  theme: {
    fill: theme => ({
       'red': theme('colors.red.450'),
       'green': theme('colors.green.450'),
     }),

    extend: {
      colors: {
        red: {
          450: "#FF0000",
        },
        green: {
          450: "#39FF14",
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
