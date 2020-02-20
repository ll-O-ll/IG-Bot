from selenium import webdriver
from time import sleep

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
    
    def get_num_followers(self):
        followers = self.driver.find_element_by_xpath("//a[contains(@href, '/followers/')]")\
            .text
        return followers.split(" ")[0]

    def get_num_following(self):
        following = self.driver.find_element_by_xpath("//a[contains(@href, '/following/')]")\
            .text
        return following.split(" ")[0]

    def get_nonfollowers(self):
        nonfollowers = [user for user in self.following if user not in self.followers]
        return nonfollowers
        
    def get_nonfollowing(self):
        nonfollowing = [user for user in self.followers if user not in self.following]
        return nonfollowing

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

if __name__ == '__main__':
    input_file = "secrets.txt"
    with open(input_file, "r", encoding="utf8") as f:
        filecontent = f.readlines()
        i = 0
        for line in filecontent:
            filecontent[i] = line.strip("\n")
            i += 1
    f.close()
    bot = IGBot(filecontent[0], filecontent[1])
  




    