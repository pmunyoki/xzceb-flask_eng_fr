
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def frenchToEnglish(frenchText=None):
    '''
    This function translates text from French to English
    '''
    if frenchText is None:
        return None
    else:
        englishText = language_translator.translate(text = frenchText, model_id = 'fr-en')\
            .get_result().get("translations")[0]['translation']
        return englishText

def englishToFrench(englishText):
    '''
    This function translates text from English to French
    '''
    if englishText is None:
        return None
    else:
        frenchText = language_translator.translate(text = englishText, model_id = 'en-fr')\
            .get_result().get("translations")[0]['translation']
        return frenchText
