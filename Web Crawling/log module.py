import sys
sys.stdout = open("output.txt","w")

import logging

#logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG)

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
logging.debug("This is debug log")
logging.info("This is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")