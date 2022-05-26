
import requests

response = requests.get("https://www.hrberry.com").status_code
if response == 200:
    print(f" {response}: Endpoint is working fine")
else:
    print (f'{response} : Something went wrong')