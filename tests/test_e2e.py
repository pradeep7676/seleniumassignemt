import csv
import json

from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.posts import Posts
from pageObjects.topic import Topics
from utilities.BaseClass import FileManager, BaseClass


class TestExtractData(BaseClass):
    @pytest.mark.topic
    def test_topic(self):

        self.driver.implicitly_wait(5)


        topic = Topics(self.driver)

        topics_list = []
        #explicit wait
        self.wait_explicit(Topics.get_topic)
        topicsDetails = topic.getTopics()

        for topic1 in topicsDetails:
            topics_list.append(topic1.text)

        with FileManager('topicDetails.json', 'w') as f:
            json.dump(topics_list, f, indent=1)

        self.message_logging("all topics are succesfully fetched")

    @pytest.mark.posts
    def test_post(self):

        posts = Posts(self.driver)

        posts_list = []
        # explicit wait
        self.wait_explicit(Posts.get_post)
        postsDetails = posts.getPosts()

        for post1 in postsDetails:
            posts_list.append(post1.text)

        with FileManager('postsDetails.json', 'w') as f:
            json.dump(posts_list, f, indent=1)

        self.message_logging("all posts are succesfully fetched")






