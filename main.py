from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import username, password
# version 0.0.1
# note that sleep times will vary depending on machine/network speeds

class IGBot:

    def __init__(self, user, pword):
        self.username = user
        self.password = pword
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(4)

        # login with username and password
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
            .send_keys(user)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pword)
        sleep(8)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(8)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(8)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        sleep(4)

    def get_username(self):
        return self.user

    def get_nonfollowers(self):
        self.nonfollowers = [user for user in self.following if user not in self.followers]
        
    def get_nonfollowing(self):
        self.nonfollowing = [user for user in self.followers if user not in self.following]
        
    def get_follow_info(self):

        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img".format(self.username))\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")\
            .click()
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
  




    