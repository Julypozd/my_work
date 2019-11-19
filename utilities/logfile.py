import inspect
import logging

def logfile(level_log=logging.DEBUG):
    # ADD the name of the class or def to the log
    logger_name = inspect.stack()[1][3]
    #create logger
    logger = logging.getLogger(logger_name)
    # TO LOG ALL messages
    logger.setLevel(logging.DEBUG)

    #name and the mode of the file
    file_handler = logging.FileHandler("automation.log", mode='a')

    #w- Over write on Existing
    #a- append

    file_handler.setLevel(level_log)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

###
# logging.warning("warning message")
#logging.info("info message")
#logging.error("error message")
#logging.basicConfig(format= '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              #datefmt='%m/%d/%Y %I:%M:%S %p', level= logging.DEBUG)