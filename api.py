import signal
import sys
import logging
from run import shlok_ai_web
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder="build")
port = int(os.environ.get("PORT", 5001))
CORS(app)


@app.route("/api/shloka-prompt", methods=["POST"])
def shloka_sage_ai():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        print("Prompt: ", prompt)
        result = shlok_ai_web.shlokAI(prompt)

        # If the result is an error, return the error message
        if "Error" in result:
            print("Error:", result)
            return jsonify(Error=result)

        # If the result is not an error, return the result
        else:
            # result_json = json.dumps(result)
            print("Result:", result)
            return jsonify(Result=result)

    except Exception as e:
        print("Error:", e)
        error_message = "Shlok-AI is currently unable to process your request. Please try again later."
        return jsonify(Error=error_message)


def signal_handler(signal, frame):
    print("You have requested to exit the program using Ctrl+C. Exiting.")
    logging.info("You have requested to exit the program using Ctrl+C. Exiting.")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    app.run(debug=True, host="0.0.0.0", port=port)
