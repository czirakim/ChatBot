import os
import logging
import yaml
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from get_interfaces_status import interfaces_status
from help import help
from inventory import inventory
from vars import firewalls
from down_interfaces import down_interfaces
from wifi_clients import wifi_clients
from hello import hello
from temperature import temperature

SLACK_EVENTS_TOKEN = "ae6682c4ac7b04a28942e70c92d8b32b"
SLACK_TOKEN = "xoxb-1876744761968-1861414359765-ryluh7pLM3g0J79Beh58UTv5"

# read inventory yml file
fire = []
with open(r'inventory.yml') as file:
    documents = yaml.full_load(file)


for item, doc in documents.items():
    fire = doc


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
#slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)
slack_events_adapter = SlackEventAdapter(SLACK_EVENTS_TOKEN, "/slack/events", app)

# Initialize a Web API client
#slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))
slack_web_client = WebClient(token=SLACK_TOKEN)

def interface(channel,m):
    interface_bot = interfaces_status(channel,m)
    message = interface_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)


def help_app(channel):
    help_bot = help(channel)
    message = help_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)
    
def inventory_app(channel):
    inventory_bot = inventory(channel)
    message = inventory_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)


def down_interfaces_app(channel):
    down_interfaces_bot = down_interfaces(channel)
    message = down_interfaces_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)

def wifi_clients_app(channel):
    wifi_clients_bot = wifi_clients(channel)
    message = wifi_clients_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)

def hello_app(channel):
    hello_bot = hello(channel)
    message = hello_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)

def temp_app(channel):
    temp_bot = temperature(channel)
    message = temp_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)    
    
# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.  
  
  # Check and see if the activation phrase was in the text of the message.

    if "help" in text.lower():
        channel_id = event.get("channel")
        return help_app(channel_id)

    if "interfaces status" in text.lower():
        channel_id = event.get("channel")
        for m in fire:
           if m in text.lower():
             return interface(channel_id,m)
           else:
             help_app(channel_id)

    if "inventory" in text.lower():
        channel_id = event.get("channel")
        return inventory_app(channel_id)

    if "interfaces down" in text.lower():
        channel_id = event.get("channel")
        return down_interfaces_app(channel_id)

    if "wifi clients" in text.lower():
        channel_id = event.get("channel")
        return wifi_clients_app(channel_id)

    if "hello" in text.lower():
        channel_id = event.get("channel")
        return hello_app(channel_id)

    if "pitemp" in text.lower():
        channel_id = event.get("channel")
        return temp_app(channel_id)

if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 6000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=6000)
