/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
    webpack: (config) => {
        config.resolve.alias.canvas = false;
        return config;
    },
    env: {
        NEXT_PUBLIC_CODESPACE_NAME: process.env.CODESPACE_NAME,
        NEXT_PUBLIC_CODESPACES: process.env.CODESPACES,   
    }
};

export default nextConfig;
