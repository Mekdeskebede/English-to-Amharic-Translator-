from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

def translate_to_amharic(english_sentence):
    translator = Translator()
    try:
        translation = translator.translate(english_sentence, src='en', dest='am')
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        try:
            english_sentence = request.form['english_sentence']
            amharic_translation = translate_to_amharic(english_sentence)

            if amharic_translation is not None:
                response = {
                    "english_sentence": english_sentence,
                    "amharic_translation": amharic_translation
                }
                return jsonify(response)
            else:
                return jsonify({"error": "Translation failed"})
        except KeyError:
            return jsonify({"error": "Missing 'english_sentence' in the request"})
    
    return jsonify({"error": "Invalid request method"})

if __name__ == "__main__":
    app.run(debug=True)
