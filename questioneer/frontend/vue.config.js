/*
Used the following django-vue connection approach as a foundation:
https://github.com/django-webpack/django-webpack-loader/issues/209#issue-512863855
https://github.com/EugeneDae/django-vue-cli-webpack-demo

But simplified it by avoiding template inheritance on Django's side, as this is not needed here.

Note: configure your Django backend properly for this setup to work as expected.

Settings Options:
https://cli.vuejs.org/config/
https://v4.webpack.js.org/configuration/dev-server/
*/

module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/static/dist/"
      : "http://127.0.0.1:8080",
  outputDir: "../static/dist",
  indexPath: "../../templates/index.html",
  pages: {
    index: {
      entry: "src/main.js",
      title: "Questioneer",
    },
  },
  chainWebpack: (config) => {
    config.devServer
      .public("http://127.0.0.1:8080")
      .hotOnly(true)
      .headers({ "Access-Control-Allow-Origin": "*" })
      .writeToDisk((filePath) => filePath.endsWith("index.html"))
  },
}

// TODO convert main frontend files to es6 if possible
