from awmc import *
from requests import *
import webbrowser
from tkinter import *
import json


def getlxusertoken(code):
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": "18f1b400-6caa-40a9-bbe7-087d828d61e9",
        "client_secret": "FK6ezK34BcrBjnVIReTOARMpk6Kq1IiN",
        "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
    }

    headers = {
        'Content-Type': "application/json"
    }

    data1=post('https://maimai.lxns.net/api/v0/oauth/token',headers=headers,data=json.dumps(payload))
    undata1=json.loads(data1.text)
    print(undata1)
    access_token=undata1['access_token']

    headers2 = {
        'Content-Type': "application/json",
        'Authorization': "Bearer "+access_token
    }

    data2=get('https://maimai.lxns.net/api/v0/user/token',headers=headers2)
    undata2=json.loads(data2.text)
    token=undata2['data']['token']
    return token