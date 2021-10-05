
import tabulate
import requests
from requests.api import post
from tabulate import tabulate
from authfile import url, cookie, headers

# authfile

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
        table = [["1","System status"],["2","System General Status"]]
        header = ["Select", "Option"]
        print(tabulate(table, header, tablefmt="rst", colalign=("center",)))
        option=input("")
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
        table = [["1","List the accounts"],["2","UCM extensions"],["3","Edit Extensions"]]
        header = ["Select", "Option"]
        print(tabulate(table, header, tablefmt="rst", colalign=("center",)))
        option=input("")
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
            extension = input("Would you like to get the SIP account of what callforward? Please input\n if there is not a valid ext this will return an error\n")
            cfudt = input("CFU destination type\n")
            cfu = input("CFU\n if there is not a valid ext this will return an error\n")
            
            sipaccount = '{"request":{"action":"updateSIPAccount", "cookie":"' + str(cookie) + '","extension":"' + str(extension) + '","cfu":"' + str(cfu) + '"}}'
            #, "cfu":"' + str(cfu) + '"  "cfu_destination_type":"' + str(cfudt) + '" 
            request_sip_account = requests.post(url, headers=headers, data=sipaccount, verify=False)
            # Formatting to JSON
            json_sip_account = request_sip_account.json()
            # Get the response in a variable
            response_SIP_account = json_sip_account['response']
            # resxtension = json_sip_account['extension']
            
            # Get the status code into a variable
            codestatus = json_sip_account['status']
            # Print the reponse
            print(response_SIP_account)
            # Print the status code
            print(codestatus)
            print(val)
            
            
            
    if val == "c":
        print("\*---------------Trunk---------------*/\nPlease select a valid option")
        table = [["1","List VoiP trunks"],["2","Add SIP Trunk"],["3","Get SIP trunk"],["4","Update SIP trunk"],["5","Delete SIP trunk"],["6","List Analog trunk"],["7","Add Analog trunk"],["8","Get Analog trunk"],["9","Update Analog trunk"],["10","Delete Analog trunk"],["11","Add SLA trunk"],["12","Update SLA trunk"],["13","List Digital trunk"],["14","Add Digital trunk"],["15","Get Digital trunk"],["16","Update Digital trunk"],["17","Delete Digital trunk"]]
        header = ["Select", "Option"]
        print(tabulate(table, header, tablefmt="rst", colalign=("center",)))
        option=input("")
        if option.lower() not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17"):
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
            addsiptrunk = '{"request":{"action":"addSIPTrunk", "cookie":"' + str(cookie) + '", "host":"' + str(host) + '", "trunk_name":"' + str(trunk_name) + '", "trunk_type":"' + str(trunk_type) + '"}}'
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
            # Print the variable val (value)
            print(val)
        if option == "3":
            print("*--Get information from specific trunk--*")
            print("TO GET INFORMATION FROM A SPECIFIC TRUNK YOU WILL *ONLY* NEED ITS INDEX NUMBER, WE HAVE GOT THIS FOR YOU: \n")
            listVoIPtrunk = '{"request":{"action":"listVoIPTrunk", "cookie":"' + str(cookie) + '", "options":"trunk_index,trunk_name,host,trunk_type,username,technology,ldap_sync_enable,trunks.out_of_service"}}'
            responsevoiptrunk = requests.post(url, headers=headers, data=listVoIPtrunk, verify=False)
            json_voip = responsevoiptrunk.json()
            rvoiptrunk = json_voip['response']
            print(rvoiptrunk)
            trunk_index = input("Please enter the trunk index\n")
            getSIPTrunk = '{"request":{"action":"getSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '" }}'
            res_trunk_info = requests.post(url, headers=headers, data=getSIPTrunk, verify=False)
            json_trunk_info = res_trunk_info.json()
            trunkinfo = json_trunk_info['response']
            print(trunkinfo)
        if option == "4":
            print("*Update the SIP Trunk*")
            print("TO UPDATE A SPECIFIC TRUNK YOU WILL NEED ITS INDEX NUMBER, WE HAVE GOT THIS FOR YOU: \n")
            listVoIPtrunk = '{"request":{"action":"listVoIPTrunk", "cookie":"' + str(cookie) + '", "options":"trunk_index,trunk_name,host,trunk_type,username,technology,ldap_sync_enable,trunks.out_of_service"}}'
            responsevoiptrunk = requests.post(url, headers=headers, data=listVoIPtrunk, verify=False)
            json_voip = responsevoiptrunk.json()
            rvoiptrunk = json_voip['response']
            print(rvoiptrunk)
            trunk_index=input("Please ENTER the TRUNK INDEX NUMBER")
            print("What field would you like to update?\n")
            table = [["1","Update the supported Codecs"],["2","Allow calls without registration"],["3","Authenticate trunk"],["4","add an Auth ID"],["5","Auto record"],["6","Enable CC service"],["7","Select the maximum number of CCSS agents"],["8","The maximum number of CCSS agents that may be allocated to this channel"],["9","To enable CC service"],["10","Caller ID Name"],["11","Caller ID Number"],["12","Direct callback"],["13","DID Mode"],["14","Configures the mode for sending DTMF"],["15","Enable Heartbeat Detection"],["16","SRTP encryption mode"],["17","Enable fax intelligent routing"],["18","From domain"],["19","From user"],["20","Host"],["21","Keep Trunk CID"],["22","Keep Original CID"],["23","LDAP Dialed Prefix"],["24","LDAP Outbound Rule"],["25","Sync LDAP Enable"],["26","Sync LDAP Password"],["27","Sync LDAP Port"],["28","NAT"],["29","Need Registration"],["30","Limit max outgoings calls"],["31","Disable Trunk"],["32","Outbound proxy"],["33","PAI Header"],["34","Passthrough PAI Heade"],["35","Configure the frequency to send SIP OPTIONS"],["36","Remove OBP from Route"],["37","Password of register trunk"],["38","Send PPI Header"],["39","TEL URI"],["40","Configure the SIP Transport method"],["41","Trunk ID (name)"],["42","Configure how to set the PPI number"],["43","Configure how to set the PPI number"],["44","Configure the username"],["45","Enable fax intelligent routing"],["46","IPVT Mode"]]
            header = ["Select", "Option"]
            print(tabulate(table, header, tablefmt="rst", colalign=("center",)))
            print("What field would you like to update?\n")
            option=input("")
            if option.lower() not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46"):
                print("This is not a valid entry for Trunk Menu")
            if option == "1":
                print("Update the supported Codecs, multiples can be set (example: ulaw, alaw, gsm, g726, g729, ilbc, g722, g726aal2, adpcm, g723, h263, h263p, h264, h265, vp8, opus, rtx, mandatory")
                codec = input("Which codecs would you like to allow on this trunk (if the option does not match the example will return an error)\n")
                codecp = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "allow":"' + str(codec) + '"}}'
                resp_codec = requests.post(url, headers=headers, data=codecp, verify=False)
                json_codec = resp_codec.json()
                rcodec = json_codec['response']
                codestatus = json_codec['status']
                print(codestatus)
                print(rcodec)
            if option == "2": # This is to apply changes
                print("Allow calls without registration")
                print("Whether outgoing calls are allowed when registration failed no：Calls are not allowed when the registration fails. If no outgoing registration is set, this configuration item can be ignored.")
                allow = input("Please input only yes or no to change this\n")
                if allow.lower() not in ("yes", "no"):
                    print("This is not a valid entry for Allow calls without registration")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "allow_outgoing_calls_if_reg_failed":"' + str(allow) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
                
            if option == "3":
                print("Authenticate trunk")
                print("If enabled, UCM will respond to incoming calls with 401 message to authenticate the trunk.")
                allow = input("Please input only yes or no to change this\n")
                if allow.lower() not in ("yes", "no"):
                    print("This is not a valid entry for Authenticate trunk")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "auth_trunk":"' + str(allow) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
            if option == "4":
                print("Authenticate ID")
                print("This is the SIP service subscriber's ID used for authentication. If not configured, the Extension Number will be used for authentication")
                auth_id = input("Please input your Auth ID\n")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "authid":"' + str(auth_id) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
            if option == "5":
                print("Auto recording")
                generalinput = input("Please input your option if it is yes or no\n")
                if allow.lower() not in ("yes", "no"):
                    print("This is not a valid entry for Autorecording")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "auto_recording":"' + str(generalinput) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
            if option == "6":
                print("To enable CC service\nTo enable CC service Control together with cc_monitor_policy. CC service is enabled if both cc_agent_policy and cc_monitory_policy are native. It is disabled if both are set to never")
                generalinput = input("Please input your Auth ID\n")
                if generalinput() not in ("native", "never"):
                    print("This is not a valid entry for enable CC service")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "cc_agent_policy":"' + str(generalinput) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
            if option == "7":
                print("To enable CC max agents\nThe maximum number of CCSS agents that may be allocated to this channel. In other words, this number is the maximum number of CC requests this channel is allowed to make.")
                generalinput = input("Please input native or never\n")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "cc_max_agents":"' + str(generalinput) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)
            if option == "8":
                print("To enable CC max agents\nThe maximum number of CCSS agents that may be allocated to this channel. In other words, this number is the maximum number of CC requests this channel is allowed to make.")
                generalinput = input("Please input native or never\n")
                postt = '{"request":{"action":"updateSIPTrunk", "cookie":"' + str(cookie) + '", "trunk":"' + str(trunk_index) + '", "cc_max_agents":"' + str(generalinput) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postt, verify=False)
                # Formatting to JSON
                jsonresponse = format_to_json.json()
                # Get the response in a variable
                presponse = jsonresponse['response']
                # Get the status code into a variable
                codestatus = jsonresponse['status']
                # Print the reponse
                print(presponse)
                # Print the status code
                print(codestatus)
                # Print the variable val (value)
                print(val)   
    else:
        print("Would you like to make another request?")
    

        
    start(url, headers, cookie)
 
"""
This is the API Guide

https://www.grandstream.com/hubfs/Product_Documentation/UCM_API_Guide.pdf?hsLang=en
"""