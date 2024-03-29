const suggestedUrl = `https://${process.env.NEXT_PUBLIC_CODESPACE_NAME}-8000.app.github.dev/`;

if (process.env.NEXT_PUBLIC_CODESPACES === 'true' && process.env.NEXT_PUBLIC_CODESPACE_NAME) {
    if (!process.env.NEXT_PUBLIC_BACKEND_URL.startsWith(suggestedUrl)) {
        console.warn(`It looks like you're running on a Github codespace. You may want to set the NEXT_PUBLIC_BACKEND_URL environment variable to ${suggestedUrl}`);
    }
}

export const backendUrl = "https://rad-backend.onrender.com";

