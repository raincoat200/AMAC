from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from time import sleep

def elem_play(var):
    var.click()
    sleep(3)
    browser.find_element_by_id("replaybtn").click()
    if browser.find_element_by_id("replaybtn").get_attribute("style").find("display: block")!=-1:
        browser.find_element_by_id("replaybtn").click()
    sleep(3)
    # time
    video = browser.find_element_by_class_name("CCH5playerContainer")
    ActionChains(browser).move_to_element(video).perform()
    time_text = browser.find_element_by_class_name("ccH5TimeTotal").text
    timenum = int(time_text.split(":")[0]) * 60 + int(time_text.split(":")[1])
    print(var.text, time_text, timenum, '秒')
    sleep(timenum + 3)
    try:
        browser.find_element_by_id("class_float").find_element_by_class_name("btn-close").click()
    except:
        pass

def info():
    while True:
        try:
            browser.find_element(By.XPATH,'//div[(@class="dw_stepbox" or @class="guide_box") and @style="display: block;"]/span').click()
        except:
            break
    try:
        data = browser.find_elements(By.XPATH, '//div[@class="guide_box"]/span')
        for i in data:
            if i.is_displayed():
                i.click()
    except:
        pass
    
def doing():
    # CURRENT ITEMS
    try:
        item = browser.find_element_by_xpath("//a[@class='article-li active cur']")
        elem_play(item)
    except:
        pass
    elems = browser.find_elements_by_class_name("art-wrap-li")
    for i in elems:
        i.text
    for i in elems:
        ActionChains(browser).move_to_element(i).perform()
        i.click()
        sleep(3)
        # LISTS
        item = i.find_element_by_xpath("//a[@class='article-li active']")
        elem_play(item)

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('https://peixun.amac.org.cn')

/* login mode*/
sleep(60)
doing()
