import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_explicit(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def message_logging(self, message):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("../pytestAssignment/utilities/logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()