from selenium.webdriver.common.by import By

from pageObjects.posts import Posts


class Topics:
    def __init__(self, driver):
        self.driver = driver

    get_topic = (By.XPATH, "//div[@class='head']/a")

    def getTopics(self):
        return self.driver.find_elements(*Topics.get_topic)