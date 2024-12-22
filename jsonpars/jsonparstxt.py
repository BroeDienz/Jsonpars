#parsing data jason

import requests

#url API
url = "https://dummyjson.com/posts"

#Get Request
response = requests.get("https://dummyjson.com/posts")

#convert to json format
parsed = response.json()

#convert  title data to txt file
with open("titles.txt", "w") as file:
    for posts in parsed["posts"]:
        file.write(posts["title"])
  
print("hasil ekspor data title")
    
#hitung jumlah Title yang ditampilkan

# jumlah_title =  len(parsed["posts"])
# print(f"jumlah title dari dummyjson adalah : {jumlah_title}")

