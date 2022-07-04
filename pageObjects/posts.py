from selenium.webdriver.common.by import By


class Posts:
    def __init__(self, driver):
        self.driver = driver

    get_post = (By.XPATH, "//div[@class='text']")

    def getPosts(self):
         return self.driver.find_elements(*Posts.get_post)
