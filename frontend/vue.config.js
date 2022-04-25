const {defineConfig} = require('@vue/cli-service')

// const AutoImport = require('unplugin-auto-import/webpack')
// const Components = require('unplugin-vue-components/webpack')
// const {ElementPlusResolver} = require('unplugin-vue-components/resolvers')

module.exports = defineConfig({
    transpileDependencies: true,
    // 以下是按需导入配置内容
    // configureWebpack: {
    //     plugins: [
    //         AutoImport({
    //             resolvers: [ElementPlusResolver()],
    //         }),
    //         Components({
    //             resolvers: [ElementPlusResolver()],
    //         }),
    //     ],
    // }
})

