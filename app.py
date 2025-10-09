from flask import Flask, request, jsonify
from flask import render_template
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/trynow")
def trynow():
    return render_template("trynow.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "you are a master debater, argue with the user intelligently and logically. use 50-120 words per argument."},
                {"role":"user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
