import pytest
from config import desiredCapabilitiesAppiumFirstddevice,desiredCapabilitiesAppiumSeconddevice,\
                    urlFirstAppiumDockerServer,urlSecondAppiumDockerServer


@pytest.fixture(params=["device1", "device2"], scope="session")
def driver_init(request):
    from appium import webdriver
    if request.param == "device1":
        web_driver = webdriver.Remote(urlFirstAppiumDockerServer, desiredCapabilitiesAppiumFirstddevice)
    if request.param == "device2":
        web_driver = webdriver.Remote(urlSecondAppiumDockerServer, desiredCapabilitiesAppiumSeconddevice)
    yield web_driver
    web_driver.quit()





