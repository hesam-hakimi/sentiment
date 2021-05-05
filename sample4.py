# gathering data from instagram
import requests
import csv
import io
from concurrent.futures import ThreadPoolExecutor
import time
import random
i = 0
id = 447188370
all_data = []


for offset in range(1, 1000000, 10):
    url = f"https://amp-api.apps.apple.com/v1/catalog/ca/apps/{id}/reviews?l=en-CA&offset={offset}&platform=web&additionalPlatforms=appletv%2Cipad%2Ciphone%2Cmac"
    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlU4UlRZVjVaRFMifQ.eyJpc3MiOiI3TktaMlZQNDhaIiwiaWF0IjoxNjE5NTU4MzA3LCJleHAiOjE2MjI1ODIzMDd9.XSvw9LqevrPYhN1FXar4OP6v87QXHbKp8jXymMtwDS7JU14PLil50Ol2IYs0uUwiUx43s-YZySR4ZkkJN069Yw',
        'Cookie': 'geo=CA'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    try:
        data = response.json()["data"]
    except Exception as e:
        print(response.text)
        print(offset)
        time.sleep(random.randint(0, 4))
        if i > 200:
            break
        continue

    for review in data:
        c = dict()
        c['id'] = review['id']
        c['type'] = review['type']
        c['review'] = review['attributes']['review']
        c['date'] = review['attributes']['date']
        c['rating'] = review['attributes']['rating']
        c['username'] = review['attributes']['userName']
        c['isEdited'] = review['attributes']['isEdited']
        c['title'] = review['attributes']['title']
        all_data.append(c)

    i += 1
    print(i)

with io.open('pintrest.csv', 'w', encoding='utf-8', newline='',) as f:
    header = ['id', 'type', 'review', 'date',
              'rating', 'username', 'isEdited', 'title']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for item in all_data:
        writer.writerow(item)
