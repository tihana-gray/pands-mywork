# Demonstrate logging
# Author: Tihana Gray


# Attributes you can put in the basicConfig
#   level
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s -  %(asctime)s - %(lineno)d

import logging
logging.basicConfig(   # removed filename="./mainlog.log" so I can see the output in the console
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-%(lineno)d")

# prog does stuff
logging.debug("we are doing stuff")
logging.info("this is information")
logging.warning("oooohhh i am not certain about this")
logging.error("not good")
logging.critical("really bad")