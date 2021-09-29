from authfile import url, cookie, headers
import requests

 
def changes():
    global val
    val = None
    while True:
            val = (input("Are you sure you would like to apply changes?\nPlease enter only Y for Yes and N for No").lower())
            if val.lower() not in ("y", "n"):
                print("This is not a valid entry")
            if val == "y":
                postta = '{"request":{"action":"applyChanges", "cookie":"' + str(cookie) + '"}}'
                format_to_json = requests.post(url, headers=headers, data=postta, verify=False)
                jsonresponse = format_to_json.json()
                                        # Get the response in a variable
                presponse = jsonresponse['response']
                                        # Get the status code into a variable
                codestatus = jsonresponse['status']
                                        # Print the reponse
                print(presponse)
                print(codestatus)
                print("The changes has been applied")
                break
            if val == "n":
                print("The changes has not been applied")
                break
            else:
                continue
    return val

val = changes()