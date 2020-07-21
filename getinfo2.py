from selenium import webdriver
import time
import re



if __name__ == "__main__":
    driver=webdriver.Chrome()
    filename = 'course.txt'
    fo=open(filename,"w",encoding="utf-8")
    driver.get('https://i.sjtu.edu.cn/xtgl/login_slogin.html')
    driver.find_element_by_xpath('//*[@id="authJwglxtLoginURL"]').click()
    driver.find_element_by_xpath('//*[@id="user"]').send_keys('maohaotian')
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('maomao8816229')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="submit-button"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]').click()
    driver.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]/ul/li[3]/a').click()
    time.sleep(3)
    windows=driver.window_handles
    driver.switch_to_window(windows[1])
    time.sleep(1)
    the_bigger_chosen=['//*[@id="nav_tab"]/li[1]','//*[@id="nav_tab"]/li[2]','//*[@id="nav_tab"]/li[3]','//*[@id="nav_tab"]/li[4]','//*[@id="nav_tab"]/li[5]']
    for every_chosen in the_bigger_chosen:
        driver.find_element_by_xpath(every_chosen).click()
        time.sleep(5)
        loadmore=driver.find_element_by_xpath('//*[@id="more"]').get_attribute('style')
        while loadmore == "text-align: center; display: block;":
            driver.find_element_by_xpath('//*[@id="more"]/font/a').click()
            time.sleep(1)
            loadmore=loadmore=driver.find_element_by_xpath('//*[@id="more"]').get_attribute('style')
        now=driver.find_element_by_xpath('//*[@id="contentBox"]/div[2]')
        divs=now.find_elements_by_xpath('.//div[@class="panel panel-info"]')
        # print(len(divs))
        for div in divs:
            # time.sleep(1)
            if divs.index(div)!=0 :
                # div.find_element_by_xpath('.//div[1]/a').click()
                button=div.find_element_by_xpath('.//div[1]/a')
                driver.execute_script("$(arguments[0]).click()",button)
            time.sleep(1)
            allineed=div.find_element_by_xpath('.//div[@class="panel-heading kc_head"]/h3/span[1]').text
            nextineed=div.find_elements_by_xpath('.//div[@class="panel-body table-responsive"]/table/tbody/tr/td')
            allhead=div.find_elements_by_xpath('.//div[@class="panel-body table-responsive"]/table/thead/tr/th')
            fo.write(allineed)
            i=12
            time.sleep(1)
            while i<=18:
                oneinfo=allhead[i-11].text +":"+nextineed[i].text
                i=i+1
                fo.write(oneinfo)