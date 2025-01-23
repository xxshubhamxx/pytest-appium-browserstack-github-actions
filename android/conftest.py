# android/conftest.py
import pytest
from appium import webdriver

@pytest.fixture(scope='session')
def session_capabilities():
    return {
        "platformName": "Android",
        "deviceName": "Samsung Galaxy S22",
        "app": "bs://22cdfe397f4f6b8da43f37f6185ea47b711debf6",
        "automationName": "UiAutomator2"
    }

@pytest.fixture(scope='function')
def setWebdriver(request, session_capabilities):
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", session_capabilities)
    request.cls.driver = driver
    yield
    driver.quit()