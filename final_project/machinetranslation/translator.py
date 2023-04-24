import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def frenchToEnglish(french_text=None):
    '''
    This function translates text from French to English
    '''
    if french_text is None:
        return None
    
    english_text = language_translator.translate(text = french_text, model_id = 'fr-en')\
        .get_result().get("translations")[0]['translation']
    return english_text

def englishToFrench(english_text=None):
    '''
    This function translates text from English to French
    '''
    if english_text is None:
        return None

    french_text = language_translator.translate(text = english_text, model_id = 'en-fr')\
        .get_result().get("translations")[0]['translation']
    return french_text
