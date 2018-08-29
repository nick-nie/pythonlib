#Example For Selenium via Python
#_*_ coding:UTF-8 _*_
 
__author__ = 'nick'
 
from selenium import webdriver
from selenium.common.exceptions import *
import time
 
class SomeTest(object):
        def __init__(self):
            pass
 
        def myfirsttest(self,myurl):
 
            'start url'
            browser=webdriver.Firefox()
            browser.get(myurl)
 
            'Start to Find a element'
            try:
                myemail=browser.find_element_by_id('user_login')
                mypass=browser.find_element_by_id('user_pass')
                myloginbutton=browser.find_element_by_id('wp-submit')
 
            except NoSuchElementException:
 
                assert 0,'找不到元素'
 
            else:
 
                myemail.send_keys('admin')
                mypass.send_keys('demo123')
                myloginbutton.click()
 
                time.sleep(2)
 
 
if __name__=='__main__':
 
    mytest=SomeTest()
    mytest.myfirsttest('http://demosite.center/wordpress/wp-login.php')
