import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
