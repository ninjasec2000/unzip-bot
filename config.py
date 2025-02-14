# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("API_ID", "21268963"))
    API_HASH = os.environ.get("API_HASH", "60239424717807c61aa7e446d443984f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7874751517:AAGk5u7lGbdq9SfEE_HF0FOwc83MZS-N8xQ")
    LOGS_CHANNEL = (
        int(os.environ.get("LOGS_CHANNEL", None))
        if os.environ.get("LOGS_CHANNEL").strip("-").isdigit()
        else os.environ.get("LOGS_CHANNEL")
    )
    MONGODB_URL = os.environ.get("MONGODB_URL", None)
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "Unzipper_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5955963998"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours (in seconds)
    MAX_TASK_DURATION_MERGE = 240 * 60  # 4 hours (in seconds)
