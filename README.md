# HeistTeam
# Telegram Music Bot 🎧

A powerful Telegram music bot for streaming audio and video in voice chats, deployed with FastAPI and Pyrogram on Render using a Blueprint (`render.yaml`).

## ✨ Features

- **High-Performance:** Uses a webhook-based approach with FastAPI for efficient, real-time updates.
- **Render Deployment:** Easily deployable to Render using a Blueprint configuration (`render.yaml`).
- **YouTube Streaming:** Stream music from YouTube and other sources in Telegram group voice chats.
- **Admin Controls:** Restrict sensitive commands (`/play`, `/stop`, etc.) to group administrators.
- **Fast and Asynchronous:** Built with Pyrogram and `py-tgcalls` for fast, non-blocking performance.

## 🚀 Deployment

This project uses a Render Blueprint to automate the deployment process.

1.  **Fork the repository:** Click the "Fork" button in the top right corner of this repository to create a copy in your own GitHub account.
2.  **Create a new Blueprint:** Log in to your Render dashboard and click **`New > Blueprint Instance`**.
3.  **Connect your repository:** Select your forked repository. Render will automatically detect the `render.yaml` file.
4.  **Configure environment variables:** Go to your new service and add the following environment variables under the **`Environment`** tab.

