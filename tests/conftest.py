import pytest

from selenium import webdriver

dc={
   "deviceName": "KYV7N15B14001804",
   "platformName": "Android",
   "app": "C:\\Users\\Vladimir\\Desktop\\app-debug.apk"}




@pytest.fixture(scope="session")
def driver_init_device_one(request):
    from appium import webdriver
    web_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dc)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def driver_init_device_two(request):
    from appium import webdriver
    web_driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', dc)
    yield web_driver
    web_driver.quit()


