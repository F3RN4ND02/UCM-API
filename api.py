import requests
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

def start(url, headers, cookie):
    global val
    val = None
    print("Hi, Welcome to the Grandstream Networks UCM - API interaction\n**Made by FernandoM NA-LATAM Support**")
    while True:
            
            val = (input("What would you like to do? \nPress a to go to System Status. \nPress b to go to Extensions\nPress c to go to Trunks\n").lower())
            if val.lower() not in ("a", "b", "c", "d"):
                print("This is not a valid entry")
            else:
                break
    return val

val = start(url, headers,cookie)


while True:
    if val == "a":
        print("\*---------------System Status---------------*/")
        print("Please select a valid option")
        option=input("Select 1 to get SYSTEM STATUS\nSelect 2 to get SYSTEM GENERAL STATUS\n ")
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
            start(url, headers, cookie)
    if val == "b":
        print("\*---------------Extension---------------*/\nPlease select a valid option")
        option=input("Select 1 to get list the accounts \nSelect 2 to get UCM extensions\nSelect 3 to get SIP Account\n ")
        if option.lower() not in ("1", "2", "3"):
            print("This is not a valid entry for Extensions")
        if option == "1":
            print("List the Account(s)\n")
            listaccount = '{"request":{"action":"listAccount", "cookie":"' + str(cookie) + '", "sidx":"extension", "sord":"asc"}}'
            request_list_account = requests.post(url, headers=headers, data=listaccount, verify=False)
            # Formatting to JSON
            json_list_account = request_list_account.json()
            # Get the response in a variable
            response_list_account = json_list_account['response']
            # Get the status code into a variable
            codestatus = json_list_account['status']
            # Print the reponse
            print(response_list_account)
            # Print the status code
            print(codestatus)
            print(val)
        if option == "2":
            ext = '{"request":{"action":"listAccount", "cookie":"' + str(cookie) + '", "item_num": "30","options": "extension,account_type,fullname,status,addr", "page": "1", "sidx": "extension", "sord": "asc"}}'
            response4 = requests.post(url, headers=headers, data=ext, verify=False)
            rext = response4.json()
            pext = rext['response']
            codestatus = rext['status']
            print(codestatus)
            print(pext)
        if option == "3":
            extension = input("Would you like to get the SIP account of what extension? Please input\n if there is not a valid ext this will return an error\n")
            sipaccount = '{"request":{"action":"getSIPAccount", "cookie":"' + str(cookie) + '", "extension":"' + str(extension) + '" }}'
            request_sip_account = requests.post(url, headers=headers, data=sipaccount, verify=False)
            # Formatting to JSON
            json_sip_account = request_sip_account.json()
            # Get the response in a variable
            response_SIP_account = json_sip_account['response']
            # Get the status code into a variable
            codestatus = json_sip_account['status']
            # Print the reponse
            print(response_SIP_account)
            # Print the status code
            print(codestatus)
            print(val)
    if val == "c":
        print("\*---------------Trunk---------------*/\nPlease select a valid option")
        option=input("Select 1 to get the List of VoIP Trunks \nSelect 2 to get SIP Account\n ")
        if option.lower() not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "2", ):
            print("This is not a valid entry for Trunk Menu")
        if option == "1":
            listVoIPtrunk = '{"request":{"action":"listVoIPTrunk", "cookie":"' + str(cookie) + '", "options":"trunk_index,trunk_name,host,trunk_type,username,technology,ldap_sync_enable,trunks.out_of_service"}}'
            responsevoiptrunk = requests.post(url, headers=headers, data=listVoIPtrunk, verify=False)
            json_voip = responsevoiptrunk.json()
            rvoiptrunk = json_voip['response']
            codestatus = json_voip['status']
            print(codestatus)
            print(rvoiptrunk)
        if option == "2":
            print("You will be adding a new SIP Trunk")
            host = input("Please enter the host IP or Domain: ")
            trunk_name = input("Please enter the Trunk Name: ")
            trunk_type = input("Please enter if the trunk is peer or register, the full word: ")
            addsiptrunk = '{"request":{"action":"addSIPTrunk", "cookie":"' + str(cookie) + '", "host":"' + str(host) + '", "trunk name":"' + str(trunk_name) + '", "trunk type":"' + str(trunk_type) + '"}}'
            add_sip_trunk = requests.post(url, headers=headers, data=addsiptrunk, verify=False)
            # Formatting to JSON
            json_sip_trunk = add_sip_trunk.json()
            # Get the response in a variable
            response_siptrunk = json_sip_trunk['response']
            # Get the status code into a variable
            codestatus = json_sip_trunk['status']
            # Print the reponse
            print(response_siptrunk)
            # Print the status code
            print(codestatus)
            
            print(val)
    else:
        print("Would you like to make another request?")
    

        
    start(url, headers, cookie)
