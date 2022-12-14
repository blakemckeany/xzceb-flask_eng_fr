"""
    This module includes functions to translate English text to French
    and vice versa

    User: Blake McKeany
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-10',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """ Takes an English string and translates it to French """
    if(english_text == "" or english_text is None):
        return None

    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    """ Takes a French string and translates it to English """
    if(french_text == "" or french_text is None):
        return None

    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    return english_text["translations"][0]["translation"]

print(french_to_english(None))
print(english_to_french(None))