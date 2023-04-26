import signal, sys
import logging
from run import shlok_ai_web
from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='build')
port = int(os.environ.get('PORT', 3000))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("build/" + path):
        return send_from_directory('build', path)
    else:
        return send_from_directory('build', 'index.html')

@app.route("/api/shloka-prompt", methods=["POST"])
def shloka_sage_ai(prompt):
    prompt = request.form["prompt"]
    result = shlok_ai_web.shlokAI(prompt)
    return jsonify(result=result)

def signal_handler(signal, frame):
    print("You have requested to exit the program using Ctrl+C. Exiting.")
    logging.info("You have requested to exit the program using Ctrl+C. Exiting.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    app.run()
