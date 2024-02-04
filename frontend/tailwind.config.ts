import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        lora: ["Lora", "serif"], // The second font is a fallback.
        nunito: ["Nunito Sans", "sans-serif"], // The second font is a fallback.
      },
      colors: {
        "gradient-start": "rgba(255, 255, 204, 0.2)", // Change this with your color.
        "gradient-end": "rgba(204, 153, 255, 0.2)", // Change this with your color.
        "gradient-start-light": "rgba(255, 255, 204, 0.1)", // Change this with your color.
        "gradient-end-light": "rgba(204, 153, 255, 0.1)", // Change this with your color.
        "gray-00": "#F9F9FA",
        "gray-15": "#E9E9ED",
        "gray-30": "#D2D2DC",
        "gray-60": "#9EA2B0",
        "gray-90": "#3F3F46",
        "gray-pdf": "#F7F7F7",
        "llama-purple-light": "#EDDDFC",
        "llama-purple": "#D09FF6",
        "llama-magenta-light": "#FBD7F9",
        "llama-magenta": "#F48FEF",
        "llama-red-light": "#FBDBD9",
        "llama-red": "#F49B95",
        "llama-orange-light": "#FAE9D3",
        "llama-orange": "#F1BA72",
        "llama-yellow-light": "#FDF6DD",
        "llama-yellow": "#F8EC78",
        "llama-lime-light": "#E5FAD2",
        "llama-lime": "#A1E66D",
        "llama-teal-light": "#D9FBEC",
        "llama-teal": "#66D8A7",
        "llama-cyan-light": "#DAFAFB",
        "llama-cyan": "#70E4EC",
        "llama-blue-light": "#EDF5FD",
        "llama-blue": "#87B6F3",
        "llama-indigo-light": "#EDECFD",
        "llama-indigo": "#817AF2",
      },
      // backgroundImage: {
      //   "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
      //   "gradient-conic":
      //     "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      // },
    },
  },
  plugins: [],
};
export default config;
