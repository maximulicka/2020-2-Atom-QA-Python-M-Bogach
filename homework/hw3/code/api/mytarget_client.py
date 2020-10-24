from urllib.parse import urljoin
import requests
import json


class MyTargetClient:

    def __init__(self, config):
        self.base_url = config.URL

        self.session = requests.Session()
        self.csrf_token = None

        self.user = config.user
        self.password = config.password
        self.authorization()

    def _request(self, method, url=None, location=None, headers=None, data=None, json_=False):
        if location:
            url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, data=data)

        if json_:
            return response.json()
        return response

    def authorization(self):
        authorization_url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue':'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/',
        }

        response = self._request(method='POST', url=authorization_url, headers=headers, data=data)
        while response.status_code != 200:
            response = self._request(method='GET', url=response.headers.get('Location'))

        response = self._request(method='GET', location='csrf')
        self.csrf_token = response.headers.get('set-cookie', None).split(';')[0].split('=')[1] or None

    def create_segment(self, name):
        url = '''https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,
        relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,
        users,flags'''
        data = json.dumps({
            "name": name,
            "pass_condition": 1,
            "logicType": "or",
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        response = self._request(method='POST', url=url, headers=headers, data=data, json_=True)
        return response.get('id')

    def delete_segment(self, name):
        url = 'https://target.my.com/api/v2/remarketing/segments/{}.json'.format(name)
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        response = self._request(method='DELETE', url=url, headers=headers)
        return response.status_code
