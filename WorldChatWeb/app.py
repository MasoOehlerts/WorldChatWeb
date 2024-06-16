from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        user_input = request.form['messageInput']
        translated_text = translator.translate(user_input, dest='en')
        return render_template('result.html', original=user_input, translated=translated_text.text)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

