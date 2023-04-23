
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
# models = language_translator.list_models().get_result()
# print(json.dumps(models, indent=2))
def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(text = frenchText, model_id = 'fr-en')
    return englishText
def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(text = englishText, model_id = 'en-fr').get_result()
    return frenchText
z = englishToFrench("Hello")
print(z)