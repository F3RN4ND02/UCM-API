import requests
from requests.api import post
import urllib3
import hashlib
urllib3.disable_warnings()

# The UCM url :port/api

# urlinput = input("Please enter the IP Address and port in this formar <IP>:<PORT>\n (No need to put https:// either /api)\n")
# url = 'https://' + str(urlinput) + '/api'

url = "https://172.16.1.77:8089/api" #Delete this

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Connection': 'close',
}

def auth(url, headers):
    
    data = '{"request": {"action":"challenge","user":"cdrapi","version":"1.0"}}'

    # First send the challenge to the UCM.

    response = requests.post(url, headers=headers, data=data, verify=False)

    # Get the challenge into variable.

    a = response.json()
    b = a['response']
    c = b['challenge']

    print("This is the challenge number: " + c)

    # Getting the challenge with the UCM Api Password with MD5
    # e = input("Please enter the UCM - API Password\n")
    e = "cdrapi123" # Delete this
    user = c+e
    h = hashlib.md5(user.encode())
    md = h.hexdigest()
    print("This is the Token: " + md)

    datas = '{"request":{"action":"login", "token":"' + str(md) + '", "url":"' + str(url) + '" , "user": "cdrapi"}}'

    #Send the token to get the Cookie

    response2 = requests.post(url, headers=headers, data=datas, verify=False)

    #Getting the cookie into a variable

    f = response2.json()
    g = f['response']
    cookie = g['cookie']

    print("This is the Cookie: " +cookie)

    return cookie

cookie = auth(url, headers)