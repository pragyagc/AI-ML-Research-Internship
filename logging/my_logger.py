# my_logger.py
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",                # log file name
    level=logging.DEBUG,               # log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Example log messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("Logging complete! Check app.log file.")
