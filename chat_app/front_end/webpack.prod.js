const common = require("./webpack.common")
const { merge } = require("webpack-merge");
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const webpack = require("webpack");

module.exports = merge(common, {
  mode: "production",
  plugins: [
    new MiniCssExtractPlugin({
      filename: "../css/[name].css",
    }),
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("production"),
    }),
  ],

  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader, //Extract css from js to main.css
          {
            loader: "css-loader", //2 Turns css into JS
            options: { importLoaders: 1 },
          },
          "postcss-loader", //1 Optimizes css for all browsers and for tailwind
        ],
      },
    ],
  },
  optimization: {
    minimizer: [new OptimizeCssAssetsPlugin()],
  },
});
