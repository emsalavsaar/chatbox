from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import List, Dict, Text, Any

class ActionProvideInfo(Action):
    def name(self) -> Text:
        return "action_provide_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This is a sample action response.")
        return []
