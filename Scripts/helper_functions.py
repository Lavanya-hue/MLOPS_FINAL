import logging
import os
from dotenv import load_dotenv

#changes made by me:

from pathlib import Path

# Load .env manually here
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get logs directory from env, raise error if not set
LOGS_DIR = os.getenv('LOGS_DIR')
if LOGS_DIR is None:
    raise ValueError("LOGS_DIR environment variable not set. Please check your .env file.")

# Join with BASE_DIR to get absolute path
LOGS_DIR = os.path.join(BASE_DIR, LOGS_DIR)

#till here

# Load environment variables
# load_dotenv()

# Define base paths dynamically
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# LOGS_DIR = os.path.join(BASE_DIR, os.getenv('LOGS_DIR'))

# Ensure Logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Define log file path
LOG_FILE = os.path.join(LOGS_DIR, "mlops_training.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_logger():
    """
    Returns the configured logger.
    """
    return logging.getLogger()

def log_info(message):
    """
    Logs an info-level message.
    """
    logger = get_logger()
    logger.info(message)
    print(f"INFO: {message}")  # Optional console output

def log_error(message):
    """
    Logs an error-level message.
    """
    logger = get_logger()
    logger.error(message)
    print(f"ERROR: {message}")  # Optional console output

def log_warning(message):
    """
    Logs a warning-level message.
    """
    logger = get_logger()
    logger.warning(message)
    print(f"WARNING: {message}")  # Optional console output
