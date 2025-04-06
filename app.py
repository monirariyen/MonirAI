from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

# তোমার OpenAI API key এখানে বসাও
openai.api_key = "তোমার-OpenAI-API-KEY"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_msg = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_msg}],
            temperature=0.7
        )
        reply = response.choices[0].message['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"ভুল হয়েছে: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
