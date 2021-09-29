from authfile import url, cookie, headers
from authfile import cookie
from authfile import headers
import requests
from requests.api import post
url = url
cookie = cookie
headers = headers

def applyChangesfunc(url, headers, cookie):
    q = input("Are you sure you would like to apply changes?\nPlease enter only Y for Yes and N for No")
    if q.lower() not in ("y", "n"):
        print("This is not a valid entry to Apply Changes")
    else:
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