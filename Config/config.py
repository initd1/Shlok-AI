import logging
import logging.config
import configparser
import os
import sys


def get_config(config_file_path):
    """_Parse configuration from file and environment variables._

    Args:
        config_file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    """Read configuration from file and environment variables.  

    :param str config_file_path: path to the configuration file
    :return: configuration values as a dictionary
    :rtype: dict
    """
    config = configparser.ConfigParser()
    # read from file
    config.read(config_file_path, encoding="utf-8")
    config.__dict__

    # read from environment variables
    for key in config["ENVIRONMENT"]:
        env_var = os.environ.get(key)
        if env_var is not None:
            config["ENVIRONMENT"][key] = env_var

    return config


def get_logging_config(file_location="Config/logger.ini"):
    """_Get logging configuration from configuration file._
    Args:
        file_location (str, optional): _description_. Defaults to "Config/logger.ini".

    Returns:
        _dict_: _logging configuration as a dictionary_
    """
    try:
        open(file_location, "r")
    except FileNotFoundError:
        logging.critical(f"File location invalid: {file_location}")
        sys.exit(1)

    config = get_config("Config/logger.ini")
    return config


def configure_logging():
    """_Configure logging for the application._

    Returns:
        _file_: _traceback.log created and populated with relevant logs from the execution of the code_
    """
    logging_config = get_logging_config()
    path = os.path.join("Config/logger.ini")

    if not os.path.isdir("Logs"):
        os.makedirs("Logs")
    if not os.path.exists(os.path.join("Logs", "shlokai.log")):
        with open(os.path.join("Logs", "shlokai.log"), "w") as fp:
            fp.write("Created shlokai.log as part of tests.")
            fp.close()
    if not os.path.exists(os.path.join("Logs", "shlokai_debug.log")):
        with open(os.path.join("Logs", "shlokai_debug.log"), "w") as fp:
            fp.write("Created shlokai_debug.log as part of tests.")
            fp.close()

    # Define log format
    log_format = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_format)

    # Set up file handler
    file_handler = logging.FileHandler(
        logging_config["handler_file"]["args"],
        mode=logging_config["handler_file"]["mode"],
        encoding=logging_config["handler_file"]["encoding"],
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)

    # Add handlers to root logger
    logging.root.addHandler(console_handler)
    logging.root.addHandler(file_handler)

    # Set root logger level
    logging.root.setLevel(logging.DEBUG)
    return logging_config
