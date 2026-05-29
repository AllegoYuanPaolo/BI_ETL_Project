import logging
import os

def get_logger(module_name: str):
    """
    Creates a standardized logger for the project.
    Pass __name__ as the module_name.
    """
    # Create logger
    logger = logging.getLogger(module_name)
    
    # Only add handlers if they don't exist (prevents duplicate logs)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Format: Time - Module - Function - Level - Message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')

        # 1. File Handler (saves to etl.log)
        file_handler = logging.FileHandler('app/logs/etl_process.log')
        file_handler.setFormatter(formatter)
        
        # 2. Console Handler (shows in terminal)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger
