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
    # try:
    #     parser = argparse.ArgumentParser(description="Choose the mode to run ShlokAI")
    #     parser.add_argument("-t", "--terminal", help="Run ShlokAI in Terminal mode")
    #     parser.add_argument("-w", "--web", help="Run ShlokAI in Web mode")
    #     # args = parser.parse_args()
    # except Exception as er:
    #     print(er)
    #     logging.critical(er)
    #     return   
    help_message = """
    usage: main.py [-h] [-t] [-w]

    Choose the mode to run ShlokAI

    options:
    -h, --help            show this help message and exit
    -t, --terminal        Run ShlokAI in Terminal mode
    -w, --web             Run ShlokAI in Web mode
    """
    if len(sys.argv) == 1:
        print("Please choose a mode to run ShlokAI. View Help menu for modes: python main.py -h")
        logging.critical("Please choose a mode to run ShlokAI. View Help menu for modes: python main.py -h")
        return
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(help_message)
        logging.info(help_message)
        return
    elif sys.argv[1] == "-t" or sys.argv[1] == "--terminal":
        shlok_ai_terminal.shlokAI()
    elif sys.argv[1] == "-w" or sys.argv[1] == "--web":
        shlok_ai_web.shlokAI()
    # if args.terminal:
    #     shlok_ai_terminal.shlokAI()
    # elif args.web:
    #     shlok_ai_web.shlokAI()
    else:
        print("Please choose a mode to run ShlokAI")
        logging.critical("Please choose a mode to run ShlokAI. View Help menu for modes: python main.py -h")
        return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    accept_user_input()
