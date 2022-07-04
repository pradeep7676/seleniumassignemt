import csv

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        s = Service("F:\packages\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="F:\packages\geckodriver.exe")
        s = Service("F:\packages\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://www.geeksforgeeks.org/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)







