import json

with open("followers.json") as f:
    dict_followers = json.load(f)

with open("following.json") as f:
    dict_following = json.load(f)

list_followers = []
dict_rel_followers = dict_followers["relationships_followers"]
for i in range(len(dict_rel_followers)):
    list_followers.append(dict_rel_followers[i]["string_list_data"][0]["value"])

list_following = []
dict_rel_followings = dict_following["relationships_following"]
for i in range(len(dict_rel_followings)):
    list_following.append(dict_rel_followings[i]["string_list_data"][0]["value"])

nonfollowers = [user for user in list_following if user not in list_followers]
nonfollowing = [user for user in list_followers if user not in list_following]

print(f"The list of people who you follow but they don't follow you back: {nonfollowers} \n")
print(f"The list of people who follow you but you don't follow them back: {nonfollowing} \n")