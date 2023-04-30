import signal, sys
import argparse
import logging
from run import shlok_ai_terminal
from run import shlok_ai_web


def signal_handler(signal, frame):
    print("You have requested to exit the program using Ctrl+C. Exiting.")
    logging.info("You have requested to exit the program using Ctrl+C. Exiting.")
    sys.exit(0)


def accept_user_input():
    try:
        parser = argparse.ArgumentParser(description="Choose the mode to run ShlokAI")
        parser.add_argument("-t", "--terminal", help="Run ShlokAI in Terminal mode")
        parser.add_argument("-w", "--web", help="Run ShlokAI in Web mode")
        args = parser.parse_args()
    except Exception as er:
        print(er)
        logging.critical(er)
        return
    if args.terminal:
        shlok_ai_terminal.shlokAI()
    elif args.web:
        shlok_ai_web.shlokAI()
    else:
        print("Please choose a mode to run ShlokAI")
        logging.critical("Please choose a mode to run ShlokAI")
        return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    accept_user_input()
