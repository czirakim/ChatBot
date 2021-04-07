import json
import requests

class whois:

  def __init__(self, channel,ip):
    self.channel = channel
    self.ip = ip

  def _status(self):
    api_url = 'https://api.bgpview.io/ip/' + self.ip
    response = requests.get(api_url)
    reply = json.loads(response.text)
    text = f"{json.dumps(reply,indent=4)}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._status(),
            ],
        }
