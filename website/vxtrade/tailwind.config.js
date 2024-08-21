// tailwind.config.js
module.exports = {
	content: [
		"./app/**/*.{js,jsx,ts,tsx}", // Adjust according to your project structure
	],
	theme: {
		extend: {
			fontFamily: {
				DM: ["Plus Jakarta Sans", "sans-serif"],
				mona: ["Work Sans", "sans-serif"],
			},
		},
		fontWeight: {
			thin: "100",
			hairline: "100",
			extralight: "200",
			light: "300",
			normal: "200",
			medium: "400",
			semibold: "500",
			bold: "600",
			extrabold: "800",
			"extra-bold": "800",
			black: "900",
		},
	},
	plugins: ["daisyui"],
};
