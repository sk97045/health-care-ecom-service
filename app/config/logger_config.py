import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level to INFO
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

# Set the logging level for the console handler
console_handler.setLevel(logging.INFO)

# Create a formatter to specify the log message format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set the formatter for the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)
