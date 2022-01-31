import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    #write the code here
    french_text = 'Bonjour' if english_text is not None else None
    return french_text

def french_to_english(french_text):
    #write the code here
    english_text = 'Hello' if french_text is not None else None
    return english_text