import json
import requests
import yaml

class inventory:

  def __init__(self, channel):
    self.channel = channel

  def _inventory(self):
    fire = []
    with open(r'inventory.yml') as file:
       documents = yaml.full_load(file)
    for item, doc in documents.items():
       inv = doc
#    z = "Devices: "
    text = f"Devices: {inv}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._inventory(),
            ],
        }
