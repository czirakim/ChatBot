import json
import requests


class down_interfaces:

  def __init__(self, channel):
    self.channel = channel

  def _status(self):
    api_url = 'http://192.168.88.8:9090/api/v1/query?query=ifOperStatus==2'
    response = requests.get(api_url)
    x=json.loads(response.text)
    m=x['data']['result']
    y=[]
    status=""
    for n in m:
      ifname = n['metric']['ifName']
      ifstatus = n['value'][1]
      device = n['metric']['instance']
      status = ifstatus.replace("2","Down")
      result = {"Device":device,"interface":ifname,"status":status}
      y.append(result)
    z=json.dumps(y,indent=1)
    text = f"{z}"
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

  def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._status(),
            ],
        }
