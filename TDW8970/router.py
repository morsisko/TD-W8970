import requests
import base64
from collections import defaultdict

class ADSLStats:
    def __init__(self, status_code, results):
        self.status_code = status_code
        self.downstreamCurrRate = int(results["downstreamCurrRate"])
        self.downstreamMaxRate = int(results["downstreamMaxRate"])
        self.upstreamCurrRate = int(results["upstreamCurrRate"])
        self.upstreamMaxRate = int(results["upstreamMaxRate"])
        self.downstreamNoiseMargin = int(results["downstreamNoiseMargin"]) / 10
        self.downstreamAttenuation = int(results["downstreamAttenuation"]) / 10
        self.upstreamNoiseMargin = int(results["upstreamNoiseMargin"]) / 10
        self.upstreamAttenuation = int(results["upstreamAttenuation"]) / 10
        self.downstreamPower = int(results["downstreamPower"]) / 10
        self.upstreamPower = int(results["upstreamPower"]) / 10


class Router:
    PAYLOAD = "[WAN_DSL_INTF_CFG#1,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n"
    URL = "http://{}/cgi?1&5"

    def __init__(self, username, password, host="192.168.1.1"):
        self.username = username
        self.password = password
        self.host = host
        self.token = "Basic " + self._generate_token(username, password)

        self.cookies = {"Authorization" : self.token}
        self.headers = {"Referer" : "http://{}/".format(self.host)}

    def _generate_token(self, username, password):
        toEncode = username + ":" + password
        return base64.b64encode(toEncode.encode()).decode()

    def _parse_response(self, response):
        splited = response.splitlines()
        content = defaultdict(int)

        for line in splited:
            equalPairs = line.split("=")

            if len(equalPairs) == 2:
                content[equalPairs[0]] = equalPairs[1]

        return content

    def get(self, timeout=10):
        r = requests.post(Router.URL.format(self.host), cookies=self.cookies, headers=self.headers, data=Router.PAYLOAD, timeout=timeout)
        return ADSLStats(r.status_code, self._parse_response(r.text))

    
