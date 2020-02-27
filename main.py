from selenium import webdriver
from time import sleep
from secrets import username, password
# version 0.0.1
# note that sleep times will vary depending on machine/network speeds

class IGBot:

    def __init__(self, user, pword):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log in with Facebook')]").click()

        # login with username and password
        self.driver.find_element_by_xpath("//input[@name='email']")\
            .send_keys(user)
        self.driver.find_element_by_xpath("//input[@name='pass']")\
            .send_keys(pword)
        self.driver.find_element_by_xpath("//button[@name='login']").click()
        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.username = self.get_username()
        sleep(4)

    def get_username(self):
        return self.driver.find_element_by_xpath("//a[@class='gmFkV']").text       

    def get_nonfollowers(self):
        self.nonfollowers = [user for user in self.following if user not in self.followers]
        
    def get_nonfollowing(self):
        self.nonfollowing = [user for user in self.followers if user not in self.following]
        
    def get_follow_info(self):
        # 'suggestions for you' needs to be covered... now it's commented

        self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.username))\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following/')]")\
            .click()
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('argument[0].scrollIntoView()', sugs)
        sleep(4)
        # get following
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        scroll_ht, last_scroll_ht = 1, 0
        while scroll_ht != last_scroll_ht:
            last_scroll_ht = scroll_ht 
            sleep(1)
            scroll_ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box) 
        links = scroll_box.find_elements_by_tag_name("a")
        self.following = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        # get followers
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers/')]")\
            .click()
        sleep(4)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        scroll_ht, last_scroll_ht = 1, 0
        while scroll_ht != last_scroll_ht:
            last_scroll_ht = scroll_ht 
            sleep(1)
            scroll_ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box) 
        links = scroll_box.find_elements_by_tag_name("a")
        self.followers = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        self.get_nonfollowers()
        self.get_nonfollowing()
                    
    def save_user_info(self, output_file):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div").click()
        with open(output_file, "w", encoding="utf8") as f:
            f.write(self.get_username() + " profile information summary for today \U0001f603: " + "\n\n")
            f.write("   Number of followers: " + str(len(self.followers)) + "\n\n")
            f.write("   Number of users following: "+ str(len(self.following)) + "\n\n")

            f.write("   List of non-followers: " + "\n")
            for nonfollower in self.nonfollowers:
                f.write("       " + nonfollower + "\n")
            f.write("\n")
            f.write("   List of non-following: " + "\n")
            for nonfollowing in self.nonfollowing:
                f.write("       " + nonfollowing + "\n")
            f.write("\n")
            f.write("   List of followers: " + "\n")
            for follower in self.followers:
                f.write("       " + follower + "\n")
            f.write("\n")
            f.write("   List of following: " + "\n")
            for following in self.following:
                f.write("       " + following + "\n")
            f.write("\n\n")
            f.write("******************************** That's all for now \U0001f642 ********************************")
        f.close()

if __name__ == '__main__':
    bot = IGBot(username, password)  
  




    