import requests
# <a href="https://play.google.com/store/apps/details?id=com.instagram.android"><img src="https://www.gplay.ws/badge/?id=com.instagram.android"></a>
# [url=https://play.google.com/store/apps/details?id=com.instagram.android][img]https://www.gplay.ws/badge/?id=com.instagram.android[/img][/url]
# [![Badge](https://www.gplay.ws/badge/?id=com.instagram.android)](https://play.google.com/store/apps/details?id=com.instagram.android)
url = "https://gplaystore.p.rapidapi.com/applicationReviews"

querystring = {"id": "com.instagram.android", "lang": "en"}

headers = {
    'x-rapidapi-key': "e0561a5997mshb62c4853e851facp10df28jsnd0fb6fbb02cc",
    'x-rapidapi-host': "gplaystore.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


for item in response.content:
    print(item)
