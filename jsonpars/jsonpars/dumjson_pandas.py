#dummy json csv whit pandas

import pandas as pd

df = pd.read_csv("dumjson_all_post1.csv")

unique_users = df["userId"].nunique()
print(f"jumlah unique user: {unique_users}","\n")

post_per_user = df["userId"].value_counts()
print(f"jumlah post per user: {post_per_user}")

user_lihat = df.groupby("userId")["view"].sum().reset_index()
user_lihat_terbanyak = user_lihat.loc[user_lihat["view"].idxmax()]
print("\nUser Dengan View terbayanyak :")
print(user_lihat_terbanyak)

# result_data = {
#     "Description" : ["Jumlah Unique User", "User Dengan View Terbanyak"] + list(post_per_user.index),
#     "Value" : [unique_users, F"User {user_lihat_terbanyak["userId"]}: {user_lihat_terbanyak["view"]} views"] + list(post_per_user.values)
# }
# result_df = pd.DataFrame(result_data)
# result_df.to_csv("hasil_analysis_pandas_dumjson.csv", index=False)
# print ("hasil analysis ke file csv")