import logging
import os
import sys
import logging.config
from matrx_utils.conf import settings
from matrx_utils import vcprint

def get_log_directory():
    """Return the appropriate log directory based on environment"""
    if settings.ENVIRONMENT == "remote":
        return settings.REMOTE_LOG_DIRECTORY
    else:
        path = settings.LOCAL_LOG_DIRECTORY
        os.makedirs(path, exist_ok=True)
        return path


log_file_dir = get_log_directory()
if log_file_dir is None:
    raise ValueError("LOCAL_LOG_DIR must be set in settings.py")

os.makedirs(log_file_dir, exist_ok=True)
LOG_FILENAME = settings.LOG_FILENAME

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {  # Formatter for files (more detail)
            "format": "%(asctime)s [%(levelname)-8s] [%(name)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {  # Formatter for console (less detail)
            "format": "%(levelname)-8s [%(name)s] %(message)s",
        }
    },
    "handlers": {
        "console": {
            # Show INFO+ if DEBUG=True, WARNING+ if DEBUG=False
            "level": "INFO" if settings.DEBUG else "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "simple",  # Use simple console format
            "stream": "ext://sys.stdout",
        },
        "file": {
            "level": "DEBUG",  # Always log DEBUG+ to file
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{log_file_dir}/{LOG_FILENAME}",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "standard",  # Use detailed file format
            "encoding": "utf-8",
        },
    },
    "loggers": {
        # --- Rule for matrx_utils.vcprint ---
        "matrx_utils.vcprint": {
            "handlers": ["file"],
            "level": "DEBUG" if settings.LOG_VCPRINT else "CRITICAL",
            "propagate": False,
        },
        # --- Rule for the main application logger ---
        "app": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        # --- Rule for Uvicorn (sensible defaults) ---
        "uvicorn.error": {
            "handlers": ["console", "file"],
            "level": "INFO",  # Log server errors
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console", "file"],  # Access logs usually just go to console
            "level": "INFO",  # Log requests
            "propagate": False,
        },
    },
    "root": {  # Catch-all
        "handlers": ["console", "file"],
        "level": "WARNING",  # Default level for other libraries
    },
}

try:
    log_dir = os.path.dirname(LOGGING['handlers']['file']['filename'])
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logging.config.dictConfig(LOGGING)

except Exception as e:
    print(f"CRITICAL ERROR: Failed to configure logging: {e}", file=sys.stderr)


vcprint("[system_logger.py] Started System Logger")