from langdetect import detect
from deep_translator import GoogleTranslator

def translate_to_english(text):
    lang = detect(text)
    if lang != 'en':
        translated = GoogleTranslator(source=lang, target='en').translate(text)
        return translated, lang
    return text, 'en'

def translate_from_english(text, target_lang):
    if target_lang != 'en':
        return GoogleTranslator(source='en', target=target_lang).translate(text)
    return text
