from . import shlok_ai_web
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/shloka-prompt", methods=["POST"])
def shloka_sage_ai():
    prompt = request.form["prompt"]
    result = shlok_ai_web.shlokAI(prompt)
    return jsonify(result=result)


if __name__ == "__main__":
    app.run()
