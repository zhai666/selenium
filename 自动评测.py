import time

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://stu.1000phone.net/student.php/Public/login')
name = browser.find_element_by_xpath('//fieldset/label[@class="block clearfix"][1]/span[@class="block input-icon input-icon-right"]/input[@class="form-control"]')
name.send_keys(610124199509213692)
time.sleep(2)
passwd = browser.find_element_by_xpath('//fieldset/label[@class="block clearfix"][2]/span[@class="block input-icon input-icon-right"]/input[@class="form-control"]')
passwd.send_keys(213692)
time.sleep(2)
denglu = browser.find_element_by_xpath('//button[@class="width-100 pull-right btn btn-sm btn-primary"]')
denglu.click()
time.sleep(2)
pingjia = browser.find_element_by_xpath('//li[@class="active"]/ul[@class="submenu"]/li[7]/a')
pingjia.click()
time.sleep(2)
kaishipingjia = browser.find_element_by_xpath('//tbody/tr[1]/td[7]/a[@class="btn btn-xs btn-success"]')
kaishipingjia.click()
time.sleep(2)
xuanze = browser.find_elements_by_xpath('//table[@id="widget_content"]/tbody[@id="topic"]/tr/td[3]/label[1]')
for i in xuanze:
    i.click()
    time.sleep(2)
tedian = browser.find_element_by_xpath('//tbody[@id="topic"]/tr[14]/td[3]/textarea[@id="YIUrmG"]')
tedian.send_keys(u'无')
time.sleep(2)
gaijin = browser.find_element_by_xpath('//table[@id="widget_content"]/tbody[@id="topic"]/tr[15]/td[3]/textarea[@id="Nf8QDS"]')
gaijin.send_keys(u'无')
time.sleep(2)
tijiao = browser.find_element_by_xpath('//table[@id="widget_content"]/tbody[3]/tr/td/button[@id="addstudent"]')
tijiao.click()