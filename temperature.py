import json
import requests
from datetime import datetime
from datetime import timezone

class temperature:

  def __init__(self, channel):
    self.channel = channel

  def _status(self):
    dt = datetime.now()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    times = int(timestamp-600)
    api_url = 'https://api.logdna.com/v1/export?from=%i&to=%i&query=PiTemp' % (times,int(timestamp))
    headers = {"servicekey": "8c1e6b1d1f6544fb872e6b0dc849c66e"}
    response = requests.get(api_url,headers=headers)
    x=int(response.text[123:126])
    text = f"Pi Temperature: {x} C"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._status(),
            ],
        }
