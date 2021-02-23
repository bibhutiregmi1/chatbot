1) rasa init --no-prompt


2) Make changes in files
in nlu.yml
- intent: corona_info(questions for this classifying as this intent?)
  examples: |
    - what is corona?
    - what is covid?
    - what is covid19?
    - tell me about covid19
    - information about covid-19


in stories.yml
- story: covid info
  steps:
  - intent: corona_info
  - action: utter_corona_info


in domain.yml
intents:
  - corona_info

responses:
  utter_corona_info:
  - text: "This is corona_info"


3) rasa train
4) rasa shell


## for action server
- in nlu.py create intent
  - intent: intent_good
  examples: |
    - on click button
    - click button


- in domain register intent and actions and wher eyou want the button to load
  - intent:
    - intent_good

  actions:
    - action_good

  responses:
  utter_greet:
  - text: "Hey! How are you?"
    buttons:
    - title: "I am good"
      payload: /intent_good

- in actions.py define actions
class ActionHelloClick(Action):

    def name(self) -> Text:
        return "action_good"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

- in stories.py
  - story: button click
    steps:
    - intent: intent_good
    - action: action_good


- add in endpoints.yml
  action_endpoint:
   url: "http://localhost:5055/webhook"


Run using terminal
- one for rasa core and one for rasa actions
  - rasa shell
  - rasa run actions


### For api support:
- instead of rasa shell run:
  - rasa run -m models --enable-api


## For database support:
in endpoints.yml, fill in the required info
###for sqlite:
tracker_store:
    type: SQL
    url: "sqlite:///./chatbot.db"
    db: "chatbot.db"
    username:
    password:

### for postgres
tracker_store:
    type: SQL
    url: ""
    dialect: "postgresql"
    db: "<db name here>"
    username: <username here>
    password: <admin>