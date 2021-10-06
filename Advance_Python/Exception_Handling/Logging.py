# Logging

from logging import *

log_format = "{lineno} -- {name} -- {asctime} -- {message}"
basicConfig(filename="log", filemode="w", level=DEBUG, format=log_format, style="{")

logger = getLogger()

logger.debug("This is Debug")
logger.info("This is Info")
logger.warning("This is Warning")
logger.error("This is Error")
logger.critical("This is critical")