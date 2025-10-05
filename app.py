from flask import Flask, request, jsonify
from flask import render_template
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY_2"))

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
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a master debater, argue with the user intelligently and logically"},
                {"role":"user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)