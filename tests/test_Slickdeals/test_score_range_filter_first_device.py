import pytest
from appium import webdriver
from random import randint
import time, os
from appium.webdriver.common.touch_action import TouchAction
from random import randrange



class TestClass:

    @pytest.fixture(autouse=True)
    def setup(self, driver_init_device_one):
        self.driver = driver_init_device_one

    def test_first_device(self):
        self.session_meth()

    def session_meth(self):
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[3]').click()
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()

        for _ in range(5):
           cleanLsScore = []
           lsScore = []
           ls = []
           stopLoop = 0
           startScore = randrange(200)
           endScore = randrange(startScore, 1000)
           print(startScore, ' | ', endScore)
           #self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
           time.sleep(1)
           #self.driver.find_element_by_id('net.slickdeals.android.test:id/clear_filter').click()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/start_range').click()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/start_range').clear()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/start_range').send_keys(str(startScore))
           time.sleep(2)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/end_range').click()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/end_range').clear()
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/end_range').send_keys(str(endScore))
           time.sleep(1)
           self.driver.find_element_by_id('net.slickdeals.android.test:id/apply_filter').click()
           time.sleep(1)
           for i in range(1, 6):
               try:
                   time.sleep(1)
                   elemName = (self.driver.find_element_by_xpath(
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                       '/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/'
                       'android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[' + str(
                           i) + ']/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').text)
                   elemScore = (self.driver.find_element_by_xpath(
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[' + str(
                           i) + ']/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]').text)
                   time.sleep(1)
                   ls.append(elemName)
                   ls.append(elemScore)
               except:
                   break
           while True:
               try:
                   time.sleep(1)
                   elementName = (self.driver.find_element_by_xpath(
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').text)
                   elemScore = (self.driver.find_element_by_xpath(
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]').text)
                   actions = TouchAction(self.driver)
                   actions.press(x=381, y=520)
                   actions.move_to(x=536, y=491)
                   actions.release()
                   actions.perform()
                   if elementName not in ls:
                       ls.append(elementName)
                       ls.append(elemScore)
                       stopLoop = 0
                   else:
                       stopLoop += 1
                       if stopLoop == 7:
                           break
               except:
                   break
           for i in range(len(ls)):
               if i % 2 == 0:
                   lsScore.append(ls[i + 1])
           for i in lsScore:
               cleanLsScore.append(int(i))
           print('cleanLsScore Score : ', cleanLsScore)
           lsSorted = sorted(cleanLsScore)
           print(' cleanLsScore: SORTED ', lsSorted)
           for i in range(len(cleanLsScore)):
               assert cleanLsScore[i] >= startScore
               assert cleanLsScore[i] <= endScore
               assert cleanLsScore[i] == lsSorted[i]
           print('Cool')

        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        time.sleep(1)
        self.driver.find_element_by_id('net.slickdeals.android.test:id/clear_filter').click()
        time.sleep(1)
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        self.driver.find_element_by_id('net.slickdeals.android.test:id/apply_filter').click()
        time.sleep(1)
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()
        self.driver.find_element_by_id('net.slickdeals.android.test:id/score_filter').click()




