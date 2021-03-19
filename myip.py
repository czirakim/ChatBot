import json
import requests


class myip:

  def __init__(self, channel):
    self.channel = channel

  def _status(self):
    api_url = 'http://ip.mtak.nl'
    response = requests.get(api_url)
    text = f"{response.text}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._status(),
            ],
        }
