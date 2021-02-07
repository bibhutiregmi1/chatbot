# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionGood(Action):

    def name(self) -> Text:
        return "action_good"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Why so good?")

        return []

class ActionBad(Action):

    def name(self) -> Text:
        return "action_bad"

    def call_api(self):
        url='https://sanuchatbot.herokuapp.com/webhooks/rest/webhook'
        myobj={
            "message":"Hi",
            "sender":"Bibhuti",
        }
        x=requests.post(url, json=myobj).json()
        text =x[0]['text']
        return text

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        get_response = self.call_api()
        dispatcher.utter_message(text=get_response)

        return []
