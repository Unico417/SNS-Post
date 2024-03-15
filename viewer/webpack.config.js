const MiniCssExtractPlugin = require(`mini-css-extract-plugin`);

module.exports = {
  mode: `development`,
  entry: `${__dirname}/src/index.ts`,
  output: {
    path: `${__dirname}/../public`,
    filename: `main.js`
  },
  resolve: {
    extensions: [`.ts`, `.tsx`, `.js`, `.json`]
  },
  target: [`web`, `es5`],
  devtool: `inline-source-map`,
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: `ts-loader`,
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: `css-loader`,
            options: {
              modules: {
                localIdentName: `[name]__[local]--[hash:base64:5]`,
              },
            },
          },
          `sass-loader`,
        ],
      },
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: `style.css`,
    }),
  ],
};
