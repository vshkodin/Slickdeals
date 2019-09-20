import time
from appium.webdriver.common.touch_action import TouchAction
from random import randrange
from locator.Locators import locatorButtonScoreFilter,locatorTogglePriceAscending,locatorFieldStartRange,\
    locatorFieldEndRange,locatorButtonApplyFilter,locatorElementNum5NameInList,locatorElementNum5ScoreInList,\
    locatorButtonClearFilter


def method_test_case_one(self):
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    time.sleep(2)
    self.driver.find_element_by_xpath(locatorTogglePriceAscending).click()
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    for _ in range(5):
        cleanLsScore = []
        lsScore = []
        ls = []
        stopLoop = 0
        startScore = randrange(200)
        endScore = randrange(startScore, 1000)
        print(startScore, ' | ', endScore)
        time.sleep(1)
        time.sleep(1)
        self.driver.find_element_by_id(locatorButtonScoreFilter).click()
        time.sleep(1)
        self.driver.find_element_by_id(locatorFieldStartRange).click()
        time.sleep(1)
        self.driver.find_element_by_id(locatorFieldStartRange).clear()
        time.sleep(1)
        self.driver.find_element_by_id(locatorFieldStartRange).send_keys(str(startScore))
        time.sleep(2)
        self.driver.find_element_by_id(locatorFieldEndRange).click()
        time.sleep(1)
        self.driver.find_element_by_id(locatorFieldEndRange).clear()
        time.sleep(1)
        self.driver.find_element_by_id(locatorFieldEndRange).send_keys(str(endScore))
        time.sleep(1)
        self.driver.find_element_by_id(locatorButtonApplyFilter).click()
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
                elementName = (self.driver.find_element_by_xpath(locatorElementNum5NameInList).text)
                elemScore = (self.driver.find_element_by_xpath(
                    locatorElementNum5ScoreInList).text)
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
        print('cleanLsScore Score  from app : ', cleanLsScore)
        lsSorted = sorted(cleanLsScore)
        print(' cleanLsScore: SORTED : ', lsSorted)
        for i in range(len(cleanLsScore)):
            assert cleanLsScore[i] >= startScore
            assert cleanLsScore[i] <= endScore
            assert cleanLsScore[i] == lsSorted[i]
        print('Cool')
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    time.sleep(1)
    self.driver.find_element_by_id(locatorButtonClearFilter).click()
    time.sleep(1)
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    self.driver.find_element_by_id(locatorButtonApplyFilter).click()
    time.sleep(1)
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()
    self.driver.find_element_by_id(locatorButtonScoreFilter).click()