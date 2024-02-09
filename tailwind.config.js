/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["docs/index.html"],
    theme: {
	extend: {},
    },
    plugins: [
	require("@tailwindcss/typography"),
	require("daisyui"),
    ],
}

