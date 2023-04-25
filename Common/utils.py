import configparser
from termcolor import colored
import sys
from Config.config import configure_logging
import logging


configure_logging()

def error_message(errormsg):
    logging.error(colored("Error: " + errormsg, "red"))
    # TODO: Extend error module to log to error log file
    # print(errormsg)


def exit_message(exitmsg):
    logging.critical("\033[91m{}\033[0m".format("Fatal Error: " + exitmsg))
    exit()

def calculateCost(self, token_count, model_name):
    # Mapping of cost per token to model
    # gpt-3.5-turbo: 0.00000000000
    # Create a dictionary of model name and cost per token and add 3 more models

    model_cost = {
        "gpt-4": 0.03,
        "gpt-3.5-turbo": 0.002,
        "ada": 0.0004,
        "curie": 0.0020,
        "babbage": 0.0005,
        "davinci": 0.02,
        # Audio models charged per minute
        "whisper": 0.006
    }
    cost_per_token = model_cost[model_name]
    cost = (token_count/1000) * cost_per_token
    return cost

class KeyFetcher:
    def getOpenAIApiKey(self):
        config = configparser.ConfigParser()

        if config.read("Config/config.ini", encoding="utf-8"):
            pass
        else:
            exit_message("Config file not found")
        try:
            OPENAI_API_KEY = config["OPENAI"]["OPENAI_API_KEY"]
        except Exception as er:
            error_message(str(er))
            exit_message("OpenAI API Key not found in config file")
        if OPENAI_API_KEY == "":
            exit_message("OpenAI API Key could not be retrieved")
        else:
            return OPENAI_API_KEY