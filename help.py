import json
import requests


class help:

  def __init__(self, channel):
    self.channel = channel

  def _help(self):
    z = "Supported commands: inventory , interfaces status <device>, interfaces down, wifi clients, PiTemp, myip, whois <ip>"
    text = f"{z}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._help(),
            ],
        }
