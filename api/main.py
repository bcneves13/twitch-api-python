import requests


class ApiRequests():

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            'Client-ID': self.api_key,
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Authorization': 'Bearer ' + self.api_secret
        }
    def getRequest(self, endpoint, params={}):
        
        r = requests.get(endpoint, params, headers=self.headers)

        return r.json()