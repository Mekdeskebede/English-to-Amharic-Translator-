from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

def is_english(sentence):
    # Check if the sentence contains predominantly English letters
    return all(char.isascii() or char.isspace() for char in sentence)

def translate_to_opposite_language(sentence, source_lang):
    translator = Translator()
    try:
        
        # Determine the opposite language for translation
        opposite_language = opposite_language = 'am' if source_lang == 'en' else 'en'

        # Translate the sentence to the opposite language
        translation = translator.translate(sentence, src=source_lang, dest=opposite_language)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        try:
            input_sentence = request.form['sentence']
            source_lang = request.form['source_lang']
            translated_sentence = translate_to_opposite_language(input_sentence,source_lang)

            if translated_sentence is not None:
                if source_lang == "am":
                    response = {
                    "amharic_sentence": input_sentence,
                    "english_sentence": translated_sentence
                }
                else:
                    response = {
                        "amharic_sentence": translated_sentence,
                        "english_sentence": input_sentence
                    }
                return jsonify(response)
            else:
                return jsonify({"error": "Translation failed"})
        except KeyError:
            return jsonify({"error": "Missing 'sentence' or 'source_lang' in the request"})
    
    return jsonify({"error": "Invalid request method"})

if __name__ == "__main__":
    app.run(debug=True)
