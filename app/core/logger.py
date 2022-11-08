import logging

from app.core.config import settings

formatter = "%(levelname)s: %(asctime)s - %(module)s - %(funcName)s - %(message)s"

logger = logging.getLogger(__name__)
logging.basicConfig(level=settings.LOGGING_LEVEL, format=formatter)
