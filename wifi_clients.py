import json
import requests


class wifi_clients:

  def __init__(self, channel):
    self.channel = channel

  def _status(self):
    api_url = 'http://192.168.88.8:9090/api/v1/query?query=mtxrWlRtabStrength{instance="192.168.88.1"}'
    response = requests.get(api_url)
    x=json.loads(response.text)
    m=x['data']['result']
    y=[]
    status=""
    for n in m:
      clientaddr = n['metric']['mtxrWlRtabAddr']
      signal = n['value'][1]
      if clientaddr == '3E:3F:69:04:D2:CE':
         client=clientaddr.replace("3E:3F:69:04:D2:CE","Pixel5G")
      elif clientaddr == '50:80:B5:51:33:1A':
         client=clientaddr.replace("50:80:B5:51:33:1A","Samsung Phone")
      elif clientaddr == '50:A0:15:7D:D2:47':
         client=clientaddr.replace("50:A0:15:7D:D2:47","Dell Work Laptop")
      elif clientaddr == '30:E4:45:1A:D3:C4':
         client=clientaddr.replace("30:E4:45:1A:D3:C4","Google TV")
      else:
        client=clientaddr
      result = {"client":client,"signal":signal}
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
