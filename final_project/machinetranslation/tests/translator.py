import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-04-26',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """This is the function to translate english text into a french text
    """
    #write the code here
    french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()

    return french_text.get("translations")[0].get("translation")


def french_to_english(french_text):
    """This is the function to translate french text into a english text
    """
    #write the code here
    english_text = language_translator.translate(
        text = french_text,
        model_id = 'fr-en').get_result()

    return english_text.get("translations")[0].get("translation")

