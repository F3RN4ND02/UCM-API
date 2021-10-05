from authfile import *
import requests


def changes():
    global val
    val = None
    while True:
            q = (input("Are you sure you would like to apply changes?\nPlease enter only Y for Yes and N for No\n").lower())
            if q.lower() not in ("y", "n"):
                print("This is not a valid entry")
            if q == "y":
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
                
            if q == "n":
                print("NO changes has been made")
                break
            else:
                continue
    return q

q = changes()