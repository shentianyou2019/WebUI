import pytest
import os
import sys
from time import sleep
from selenium import webdriver
from TestDatas.GobalDatas import gobal_datas as GD
from PageObjects.TradePom.Trade_page import TradePage
from Public.basepage import BasePage
from Public.Log import Logger
from Public.get_config import r_config
from Config import setting
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# if sys.platform == "win32":
#     conf_dir = os.path.join(BASE_DIR, 'Public/config/config.ini').replace('/', '\\')
# else:
#     conf_dir = os.path.join(BASE_DIR, 'Public/config/config.ini')
# log_dir = r_config(conf_dir, "log", "log_path")
log_dir = setting.LOG_DIR
logger = Logger().get_logger()

driver = None



@pytest.fixture(scope='class')
def start_module(project_module_start):
    '''
    每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
    :param project_module_start:  每个模块单独打开一次浏览器
    :return: driver lg
    '''
    logger.info("==========开始执行XX测试用例集===========")
    global driver
    driver = project_module_start
    driver.get(GD.web_login_url)
    lg =TradePage(driver)
    yield (driver, lg)
    logger.info("==========结束执行XX测试用例集===========")
    driver.quit()

@pytest.fixture(scope='session')
#@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver lg
    '''
    logger.info("==========开始执行XX测试用例集===========")
    global driver
    driver = project_session_start
    logger.info("----------------------------------------------------------------------------------" + str(driver))
    driver.get(GD.web_login_url)
    lg = TradePage(driver)
    yield (driver, lg)
    logger.info("==========结束执行XX测试用例集===========")


@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    sleep(3)
