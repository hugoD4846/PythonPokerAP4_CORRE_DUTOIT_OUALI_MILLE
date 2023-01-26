import logging


def setUpLogging(level=logging.INFO):
    logging.basicConfig(filename="poker.log", level=level)
    logging.info("Starting up")
    logging.info("Logging is working")
