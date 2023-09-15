import logging as log

def create_logger(logger_name: str, filename: str):

    logger = log.getLogger(logger_name)
    logger.setLevel(log.DEBUG)

    file_handler = log.FileHandler(filename)
    file_handler.setLevel(log.DEBUG)

    formatter = log.Formatter('%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger