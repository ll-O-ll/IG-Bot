# IG-Bot V 0.0.0
Instagram Bot for monitoring account information such as follower count, number of posts, max number of likes, a certain followed user's feed etc. The current version of the bot only supports Chrome users who've linked their Facebook with their Instagram account. Therefore, signing into your IG account can only be done through Facebook.

## Setup

+ Install python 3.7<
+ Download and install Selenium Chrome Webdriver [here](https://chromedriver.chromium.org/getting-started). Choose the right program to install according to your computer's operating system. *Make sure the chromedriver.exe executable file is in your system's and user's **Path** environment variable.*
+ Install Selenium using the following command:
```cmd
pip install selenium
```
+ Clone or download and unzip this repository
+ Enter your Instagram's username or email (if logging in through Facebook) and password in the [secrets.txt](./secrets.txt) file. First line must be username and second must be password. Make sure no additional tabs/spaces are added on each line and that characters on both lines are exclusively for the username and password.
+ Run commands and have fun!
## Commands

1. Run the main.py script using python built-in interactive method
  ```python
  python -i main.py
  ```

2. When the Selenium Webdriver has loaded Chromium and you're finally logged into your account enter the following command in python's interactive shell
  ```python 
  bot.get_follow_info()
  ```
  This command will get all users you follow and all users who follow you. The data is stored in a list. To see this run the following:
  ```python
  bot.following
  ```
  ```python
  bot.followers
  ```
3. In order to save your user information in an text document invoke the save_user_info() method with the name of the text file you want to save your user information:
    ```python
        bot.save_user_info("{text-file-name}.txt")
    ```
    This file will have information retrieved from various other methods. Individual info can be obtained also. See step **4**.

4. A few other useful information can also be obtained such as:
  The username (assuming you've logged in using your Facebook account, this info could be different from your login username):
  ```python 
  bot.username
  ```
  Non-followers (users who you follow but don't follow you back)
  ```python
  bot.nonfollowers
  ```
  Non-following users (users who follow you but you don't follow them back)
  ```python
  bot.nonfollowing
  ```
  Number of followers:
  ```python
  bot.num_followers
  ```
  Number of following users:
  ```python
  bot.num_following
  ```


 
 ## Improvements
 
 This bot could be improved in many ways. For instance, finding a following user's most recent post, obtaining the total number of likes on all your posts, obtaining the total number of comments on all your posts, finding all blocked users, etc.... 
 Minor versions will be made in the future.
 
## Tasks

- [x] Get first features to work
- [x] Push my initial commits to GitHub
- [ ] Add additional features as described in **Improvements** section
- [ ] Go through test cases
- [ ] Fix any known bugs
  
