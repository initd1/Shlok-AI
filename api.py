import signal, sys
import logging
from run import shlok_ai_web
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='build')
port = int(os.environ.get('PORT', 5001))
CORS(app)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve(path):
#     if path != "" and os.path.exists("build/" + path):
#         return send_from_directory('build', path)
#     else:
#         return send_from_directory('build', 'index.html')

@app.route("/api/shloka-prompt", methods=["POST"])
def shloka_sage_ai():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        print("Prompt: ", prompt)
        result = shlok_ai_web.shlokAI(prompt)
        print("Result:", result)
        return jsonify(result=result)
    except Exception as e:
        print("Error", e)
        print(jsonify(result="Shlok-AI is currently unable to process your request. Please try again later."))
        return jsonify(result="Shlok-AI is currently unable to process your request. Please try again later.")

def signal_handler(signal, frame):
    print("You have requested to exit the program using Ctrl+C. Exiting.")
    logging.info("You have requested to exit the program using Ctrl+C. Exiting.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    app.run(debug=True,host='0.0.0.0', port=port)
