import imp


import requests

response = requests.get("https://gitlab.example.com/api/v4/users/nanuchi/projects")
my_project = response.json()

print(response.json)