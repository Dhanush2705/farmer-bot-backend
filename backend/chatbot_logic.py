import json
from rapidfuzz import fuzz
from langdetect import detect
from deep_translator import GoogleTranslator, exceptions as dt_exceptions

# Load FAQ data
with open('faq_data.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

SUPPORTED_LANGUAGES = {
    'en': 'english',
    'te': 'telugu',
    'hi': 'hindi'
}

def translate_to_english(text):
    try:
        lang = detect(text)
        print(f"[DEBUG] Detected input language: {lang}")
    except Exception:
        lang = 'en'

    if lang not in SUPPORTED_LANGUAGES:
        lang = 'en'

    if lang != 'en':
        try:
            translated = GoogleTranslator(source=lang, target='en').translate(text)
            print(f"[DEBUG] Translated to English: {translated}")
            return translated, lang
        except dt_exceptions.TranslationNotFound:
            print("[ERROR] Translation to English failed")
            return text, 'en'
    return text, 'en'

def translate_from_english(text, target_lang):
    if target_lang != 'en' and target_lang in SUPPORTED_LANGUAGES:
        try:
            translated = GoogleTranslator(source='en', target=target_lang).translate(text)
            print(f"[DEBUG] Translated back to {target_lang}: {translated}")
            return translated
        except dt_exceptions.TranslationNotFound:
            print("[ERROR] Translation from English failed")
            return text
    return text

def get_bot_response(msg):
    # Detect and translate to English
    msg_translated, lang = translate_to_english(msg)
    msg_translated = msg_translated.lower()

    matched_responses = []

    for keyword in faq_data:
        score = fuzz.partial_ratio(keyword.lower(), msg_translated)
        if score >= 70:
            matched_responses.append(faq_data[keyword])

    if matched_responses:
        response = " ".join(matched_responses)
    else:
        response = "I'm not sure about that. Could you please rephrase or ask something else?"

    final_response = translate_from_english(response, lang)
    return final_response
