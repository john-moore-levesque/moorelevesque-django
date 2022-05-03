const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})


module.exports = {
  devServer: {
    allowedHosts: [
      /*
       * cloud9 FQDN,
       * cloud9 internal IP,
       * cloud9 external IP 1,
       * cloud9 external IP 2,
       * cloud9 external IP 3
       */
      ]
  }
}