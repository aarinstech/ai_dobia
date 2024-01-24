from googletrans import Translator


def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text

def translate_to_english(text):
    translator=Translator()
    translation=translator.translate(text, src='hi', dest='en')
    return translation.text

# hindi_text="Hello"
# english_text=translate_to_english(hindi_text)
# print(english_text)

# english_text="I am God"
# hindi_translation = translate_to_hindi(english_text)
# print(hindi_translation)


