import logging

MESSAGE_STRING: str = "%(asctime)s [%(levelname)s] | %(message)s"
DATE_STRING: str = "%d/%m/%Y %H:%M"


class Logger():
    def __init__(self, loglevel: int = logging.WARNING):
        self.loglevel = loglevel

    def stream_log(self, loglevel: int, message: str) -> None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(self.loglevel)
        formatter = logging.Formatter(MESSAGE_STRING, datefmt=DATE_STRING)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        match loglevel:
            case logging.DEBUG:
                logger.debug(message)
            case logging.INFO:
                logger.info(message)
            case logging.WARNING:
                logger.warning(message)
            case logging.ERROR:
                logger.error(message)
            case logging.CRITICAL:
                logger.critical(message)
