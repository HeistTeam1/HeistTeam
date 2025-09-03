# app/youtube.py
import os
import yt_dlp

def get_youtube_stream_info(query: str):
    """Searches YouTube and returns info for the best audio stream."""
    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'quiet': True}) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            return info['url'], info['title'], info['webpage_url']
    except Exception as e:
        print(f"Error fetching YouTube stream info: {e}")
        return None, None, None

def download_youtube_audio(url: str, filename: str):
    """Downloads audio from a YouTube URL to a file."""
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": filename,
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
