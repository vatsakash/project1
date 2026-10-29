"""from src.logger import logging 

logging.debug("This is a debug Message")
logging.info("This is an info message ")
logging.error("This is error message")
logging.warning("This is error message")
logging.critical("This is for critical message")"""

#for checking the exception file 

# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 2 + 'z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()
