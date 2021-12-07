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
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
