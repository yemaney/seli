"""Collection of functions related to logging data.
"""

import logging


def get_logger(name : str) -> logging.Logger:
    """
    Creates and returns a logger that logs data into a `logs.log` file
    with a specific format.

    Parameters
    ----------
    name : str
        name of the logger, should be `__name__` for good module level
        logging format

    Returns
    -------
    logging.Logger
        logger to send execution details to a file
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs.log")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s, %(msecs)d %(levelname)-8s [%(name)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
