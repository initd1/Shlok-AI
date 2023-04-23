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

class CostCalculator:
    def __init__(self):
        self.token_count = token_count
        self.cost_per_token = cost_per_token

    def calculateCost(self, token_count, cost_per_token):
        return token_count * cost_per_token 