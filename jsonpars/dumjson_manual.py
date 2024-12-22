# Olah data file csv Menggunakan python
import csv

# Membaca data dari file csv
data = []
with open("dumjson_all_post1.csv") as csvfile :
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

        
# Menghitung Jumlah Unique User
unique_users = set()
for row in data :
    unique_users.add(row["userId"])
print(f"Jumlah Unique User: {len(unique_users)}")

# Menghitung Jumlah Post per User
posts_per_user = {}
for row in data :
    user_id = row["userId"]
    if user_id in posts_per_user :
        posts_per_user[user_id] +=1
    else :
        posts_per_user[user_id] =1
sorted_posts_per_user = sorted(
    posts_per_user.items(),
    key = lambda item : item [1],
    reverse = True
)
print("\nJumlah Post per User:")
for user_id, count in sorted_posts_per_user:
    print(f"User {user_id}: {count} posts")
    
# Mengambil user dengan view terbanyak
views_per_user = {}
for row in data :
    user_id = row["userId"]
    views = int(row["view"])
    if user_id in views_per_user :
        views_per_user[user_id] += views
    else :
        views_per_user[user_id] = views

views_user_terbanyak = max(views_per_user, key=views_per_user.get)
max_views = views_per_user[views_user_terbanyak]
print("\n User Dengan Views Terbanyak Adalah :")
print(f"User Id  {views_user_terbanyak} : {max_views} views")