from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['messageInput']
    translated_text = translator.translate(user_input, dest='en')
    return f"Translated text: {translated_text.text}"

if __name__ == "__main__":
    app.run(debug=True)
