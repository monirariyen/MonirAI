import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# OpenAI API Key
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "তুমি একজন সহায়ক বাংলা AI চ্যাটবট।"},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"ভুল হয়েছে: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
