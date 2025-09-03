import logging
from .main import app, pyrogram_client # Import core components
from .music_player import play_music, stop_music # Import music functions

# Optional: Configure logging for the package
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
