# IG-Bot V 0.0.0
Instagram Bot for monitoring account information such as follower count, number of posts, max number of likes, a certain followed user's feed etc. The current version of the bot only supports Chrome users who've linked their Facebook with their Instagram account. Signing in is done through Facebook.

## Setup

Install python 3.7<
Install Selenium
Clone or download and unzip this repository

## Commands

1. Run the main.py script using python built-in interactive method
  + python -i main.py

2. When the Selenium Webdriver has loaded Chromium and you're finally logged into your account enter the following command in python's interactive shell
  + bot.get_follow_info()
  This command will get all users you follow and all users who follow you. The data is stored in a list. To see this run the following:
  + bot.following
  + bot.followers
3. A few other useful information can also be obtained such as:
  The user name (assuming you've logged in using your Facebook account, this info could be different from your login user name):
  + bot.get_username()
  Non-followers (users who you follow but don't follow you back)
  + bot.get_nonfollowers()
  Non-following users (users who follow you but you don't follow them back)
  + bot.get_nonfollowing()
  Number of followers:
  + bot.get_num_followers()
  Number of following users:
  + bot.get_num_following()
 
 ## Improvements
 
 This bot could be improved in many ways. For instance, finding a following user's most recent post, obtaining the total number of likes on all your posts, obtaining the total number of comments on all your posts, finding all blocked users, etc.... 
 Minor versions will be made in the future.
 
## Tasks

- [x] Get first features to work
- [x] Push my initial commits to GitHub
- [ ] Add additional features as described in **Improvements** section
- [ ] Go through test cases
- [ ] Fix any known bugs
  
 


