import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from utilities.ConfigUtility import ConfigReader


@pytest.fixture(scope="session")
def get_driver(request):
    appium_service = AppiumService()
    appium_service.start()
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", ConfigReader.getDesiredCapabilities())
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield  # acts as teardown
    driver.quit()
    appium_service.stop()

