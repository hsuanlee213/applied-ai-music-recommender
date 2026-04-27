import logging
import os


def setup_logger() -> logging.Logger:
    """
    Set up a logger for the application.
    Logs are written to logs/app.log.
    """
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("music_recommender")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/app.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger