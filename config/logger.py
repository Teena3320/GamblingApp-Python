import logging
from config.settings import LOG_LEVEL

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("gambling_app")