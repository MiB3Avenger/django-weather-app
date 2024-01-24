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
            families: ['Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap'],
        },
    })
}
