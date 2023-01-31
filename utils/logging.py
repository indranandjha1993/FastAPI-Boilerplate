import logging
from logging.handlers import RotatingFileHandler


def configure_logging():
    logger = logging.getLogger("app")
    handler = RotatingFileHandler("app.log")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
