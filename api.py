import requests
import urllib3
import hashlib
urllib3.disable_warnings()

# The UCM url :port/api

url = "https://172.16.1.77:8089/api"

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Connection': 'close',
}

data = '{"request": {"action":"challenge","user":"cdrapi","version":"1.0"}}'

# First send the challenge to the UCM.

response = requests.post(url, headers=headers, data=data, verify=False)

# Get the challenge into variable.

a = response.json()
b = a['response']
c = b['challenge']

print("This is the challenge number: " + c)

# Getting the challenge with the UCM Api Password with MD5
# e = input("cdrapi123")
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

def start():
    print("Hi, Welcome to the Grandstream Networks UCM - API interaction\n Made by Fernando")
while True:
        val = (input("What would you like to do? \nPress a to go to System Configuration. \nPress b to go to Extensions\n").lower())
        if val.lower() not in ("a", "b", "c", "d"):
            print("This is not a valid entry")
        else:
            break

if val == "a":
    print("\*---------------System Configuration---------------*/")
    print("Please select a valid option")
    option=input("Select 1 to get system status \nSelect 2 to get system general status \n ")
    if option.lower() not in ("1", "2"):
        print("This is not a valid entry for System Status")
        
    if option == "1":
        gss = '{"request":{"action":"getSystemStatus", "cookie":"' + str(cookie) + '"}}'
        response3 = requests.post(url, headers=headers, data=gss, verify=False)
        rgss = response3.json()
        gss = rgss['response']
        print(gss)
    if option == "2":
        gss = '{"request":{"action":"getSystemGeneralStatus", "cookie":"' + str(cookie) + '"}}'
        response3 = requests.post(url, headers=headers, data=gss, verify=False)
        rgss = response3.json()
        gss = rgss['response']
        print(gss)
    else:
        val=input("What would you like to do? \nPress a to go to System Configuration. \n").lower()
if val == "b":
    print("\*---------------Extension---------------*/\nPlease select a valid option")
    option=input("Select 1 to get the UCM extensions \nSelect 2 to get SIP Account\n ")
    if option.lower() not in ("1", "2"):
        print("This is not a valid entry for Extensions")
    if option == "1":
        ext = '{"request":{"action":"listAccount", "cookie":"' + str(cookie) + '", "item_num": "30","options": "extension,account_type,fullname,status,addr", "page": "1", "sidx": "extension", "sord": "asc"}}'
        response4 = requests.post(url, headers=headers, data=ext, verify=False)
        rext = response4.json()
        pext = rext['response']
        print(pext)
    if option == "2":
        extension = input("Would you like to get the SIP account of what extension? Please input\n if there is not a valid ext this will return an error\n")
        sipaccount = '{"request":{"action":"getSIPAccount", "cookie":"' + str(cookie) + '", "extension":"' + str(extension) + '" }}'
        request_sip_account = requests.post(url, headers=headers, data=sipaccount, verify=False)
        # Formatting to JSON
        json_sip_account = request_sip_account.json()
        # Get the response in a variable
        response_SIP_account = json_sip_account['response']
        returncodestatus = json_sip_account['status']
        print(response_SIP_account)
        print(returncodestatus)
        print(val)
else:
    print("This session has ended")
    
start()
