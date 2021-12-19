import pytest
import os
import sys
from selenium import webdriver
from Public.Log import Logger
from Public.get_config import r_config
from Config import setting
browserName = r_config(setting.CONFIG_DIR, "browserType", "browserName")
print(browserName)
logger = Logger().get_logger()
from Public.browserengine import BrowserEngine
engine=BrowserEngine('driver')
driver = None


@pytest.fixture(scope='session')
def project_session_start():
    logger.info("==========开始 XX项目 执行测试===========")
    global driver
    # if driver:
    #     yield driver
    #driver = webdriver.Firefox()
    driver =engine.open_browser(browserName)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()
    logger.info("==========结束 XX项目 测试===========")


@pytest.fixture(scope='module')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    global driver
    # if driver:
    #     yield driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(0)
    yield driver
    driver.quit()
    logger.info("==========结束 XX模块 测试===========")


def pytest_configure(config):
    # 标签名集合
    marker_list = ['smoke', 'lucas']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)
