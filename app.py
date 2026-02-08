from flask import Flask, render_template, request, jsonify
from chatbot import chatwai
import os
import json
from uuid import uuid4
app = Flask(__name__)
chatfile = "chats.json"

def load_chats():
    if not os.path.exists(chatfile):
        return {}
    with open(chatfile, "r") as f:
        return json.load(f)


def save_chats(data):
    with open(chatfile, "w") as f:
        json.dump(data, f, indent=4)
#routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    chat_id = data.get("chat_id")

    chats = load_chats()

    if chat_id not in chats:
        chats[chat_id] = []

    reply = chatwai(message)

    chats[chat_id].append({"role": "user", "text": message})
    chats[chat_id].append({"role": "bot", "text": reply})

    save_chats(chats)

    return jsonify({"reply": reply})
@app.route("/history/<chat_id>")
def history(chat_id):
    chats = load_chats()
    return jsonify(chats.get(chat_id, []))

@app.route("/new_chat")
def new_chat():
    return jsonify({"chat_id": str(uuid4())})
if __name__ == "__main__":
    app.run(debug=True)

