import requests
import json

# url = "https://app-stores.p.rapidapi.com/details"

# querystring = {"id": "com.snapchat.android",
#                "store": "google", "language": "en"}

# headers = {
#     'x-rapidapi-key': "e0561a5997mshb62c4853e851facp10df28jsnd0fb6fbb02cc",
#     'x-rapidapi-host': "app-stores.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# data = json.dumps(response.json())
# with open('detail.jdon', 'w', encoding='utf-8') as f:
#     f.write(data)


# url = "https://app-stores.p.rapidapi.com/reviews"

# querystring = {"id": "com.snapchat.android",
#                "store": "google", "language": "en"}

# headers = {
#     'x-rapidapi-key': "e0561a5997mshb62c4853e851facp10df28jsnd0fb6fbb02cc",
#     'x-rapidapi-host': "app-stores.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# data = response.content
# with open('reviews.json', 'w', encoding='utf-8') as f:
#     f.write(data)

import requests

url = "https://gplaystore.p.rapidapi.com/applicationReviews"

querystring = {"id": "com.instagram.android", "lang": "en"}

headers = {
    'x-rapidapi-key': "e0561a5997mshb62c4853e851facp10df28jsnd0fb6fbb02cc",
    'x-rapidapi-host': "gplaystore.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
with open('reviews.json', 'w', encoding='utf-8') as f:
    f.write(response.text)

# print(response.text)
