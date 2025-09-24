import logging

# Create logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler("app.log")
fh.setLevel(logging.WARNING)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers
logger.addHandler(ch)
logger.addHandler(fh)

# Example logs
logger.debug("Debugging details")
logger.info("General info")
logger.warning("This goes to file and console")
logger.error("This goes to file and console")

#highest -> lowest
#critical,error,warning,info,debug