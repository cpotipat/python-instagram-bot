import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
TARGET_ACCOUNT = "hawaiitraveltips"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located((By.ID, "loginForm")))
        username = self.driver.find_element_by_name("username")
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "nav")))

    def find_followers(self):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        search_box.send_keys(TARGET_ACCOUNT)

        target_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')))
        target_account.click()

        followers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
        followers.click()

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
