# parsing data jason from API to csv file

import requests
import csv

url = "https://dummyjson.com/posts"

skip = 0
limit = 30


def grab_data(skip, limit):
    response = requests.get(url, params={"skip": skip, "limit": limit})
    return response.json()


with open("dumjson_all_post1.csv", "w", newline="") as csvfile:
    fieldnames = ["title", "view", "userId"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    tota_data = requests.get(url).json()["total"]
    while skip < tota_data:
        data = grab_data(skip, limit)
        for post in data["posts"]:
            writer.writerow({"title": post["title"], "view": post["views"], "userId": post["userId"]})
        skip += limit
    
print("Hasil ekspor CSV") 


