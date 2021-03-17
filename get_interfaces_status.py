import json
import requests


class interfaces_status:

  def __init__(self, channel,dev):
    self.channel = channel
    self.device = dev

  def _status(self,dev):
    api_url = 'http://192.168.1.8:9090/api/v1/query?query=ifOperStatus{instance="%s"}' % (dev)
    response = requests.get(api_url)
    x=json.loads(response.text)
    m=x['data']['result']
    y=[]
    c=""
    for n in m:
      a = n['metric']['ifName']
      b = n['value'][1]
      if b == '1':
         c = 'UP'
      elif b == '2':
         c = 'Down'
      result = {"interface":a,"status":c}
      y.append(result)
    z=json.dumps(y,indent=1)
    text = f"{z}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._status(self.device),
            ],
        }
