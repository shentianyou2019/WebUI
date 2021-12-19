# -*- coding:utf-8 -*-
import os.path, sys
from configparser import ConfigParser
from selenium import webdriver
from Public.Log import Logger
from Config import setting
from Public.get_config import r_config
file_path=setting.CONFIG_DIR
browserName = r_config(file_path, "browserType", "browserName")
logger = Logger().get_logger()
# dir = os.path.dirname(os.path.abspath('.'))
# chrome_driver_path = dir + r'/Tools/chromedriver.exe'
# print(chrome_driver_path)
class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    # 注意相对路径获取方法
    print("**************:",dir)
    # chrome_driver_path = dir + r'/Tools/chromedriver.exe'
    # ie_driver_path = dir + r'/Tools/IEDriverServer.exe'
    chrome_driver_path = setting.CHROME_PATH
    ie_driver_path = setting.IE_PATH

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self,driver):
        config = ConfigParser()
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        print(browser)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
        # elif browser == "Chrome":
        #     driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        return driver

    # def quit_browser(self):
    #     logger.info("Now, Close and quit the browser.")
    #     self.driver.quit()
if __name__=="__main__":
    p=BrowserEngine("driver")
    p.open_browser(browserName)

