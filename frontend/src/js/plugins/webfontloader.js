/**
 * Load fonts for our website via api.
 * 
 * webfontloader documentation: https://github.com/typekit/webfontloader
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/plugins/webfontloader.js
 * @exports function Asynchronous function to load all fonts.
 */

export async function loadFonts () {
    const webFontLoader = await import(/* webpackChunkName: "webfontloader" */'webfontloader')

    webFontLoader.load({
        google: {
            families: ['Roboto:100,300,400,500,700,900&display=swap'],
        },
    })
}
