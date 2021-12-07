const common = require("./webpack.common");
const { merge } = require("webpack-merge");
const webpack = require("webpack");

module.exports = merge(common, {
  mode: "development",
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          "style-loader", //3 injects styes to DOM
          {
            loader: "css-loader", //2 Turns css into JS
            options: { importLoaders: 1 },
          },
          "postcss-loader", //1 Optimizes css for all browsers and for tailwind
        ],
      },
    ],
  },
  
  plugins: [
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("development"),
    }),
  ],
});
// "postcss": "^7.0.39",