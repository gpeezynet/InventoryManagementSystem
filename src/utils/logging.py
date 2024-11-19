import logging

# Configure logging settings
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    """Create and return a logger instance."""
    logger = logging.getLogger(name)
    return logger

# Example usage
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("This is an info message")
    logger.error("This is an error message")
