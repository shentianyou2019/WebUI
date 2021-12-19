import time, datetime, os, sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Public.Log import Logger
from Public.get_config import r_config
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException
from Config import setting
logger = Logger().get_logger()


# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage(object):
    """
    基础类，用于界面对象类的继承
    """
    def __init__(self,selenium_driver,parent=None):
        self.driver = selenium_driver
        self.parent = parent
        self.timeout = 10

    def get_element(self,loc):
        """
        单个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("{0}界面中未能找到{1}元素".format(self,loc))

    def get_elements(self,loc):
        """
        多个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            logger.error("{0}界面中未能找到{1}元素".format(self,loc))

    def script(self,src):
        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        """
        return self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_key(self, loc, vaule, clear_first=True, click_first=True):
        try:
           # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.get_element(loc).click()
            if clear_first:
                self.get_element(loc).clear()
            self.get_element(loc).send_keys(vaule)
        except AttributeError:
            logger.error("%s 界面中未能找到 %s 元素" % (self, loc))
    #键盘事件
    def send_enterkey(self, loc,vaule, clear_first=True, click_first=True):
        try:
           # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.get_element(loc).click()
            if clear_first:
                self.get_element(loc).clear()
            self.get_element(loc).send_keys(vaule)
            self.get_element(loc).send_keys(Keys.ENTER)
        except AttributeError:
            logger.error("%s 界面中未能找到 %s 元素" % (self, loc))


    def click_element(self, loc):
        """
              :param loc: 传元素的属性值
              :return: 定位到的元素
              """
        try:
            #loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            self.get_element(loc).click()
        except AttributeError:
            logger.error("%s 界面中未能找到 %s 元素" % (self, loc))

    def get_element_text(self, loc):
        logger.info('获取页面元素:{0}'.format(loc))
        try:
            return self.get_element(loc).text
        except:
            logger.info('页面{0}元素的文本获取失败！！！'.format(loc))
            raise


    def switch_frame(self,loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:

            iframe=self.get_element(loc)
            return self.driver.switch_to_frame(iframe)
        except NoSuchFrameException as msg:
            logger.error("查找iframe异常-> {0}".format(msg))

    def quit_iframe(self):
        """退出当前iframe"""
        self.driver.switch_to_default_content()

        # 切换到默认窗口
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def switch_windows(self,loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            logger.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            logger.error("查找alert弹出框异常-> {0}".format(msg))

    # 切换不同页面窗口
    def switch_to_window_by_title(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break
            self.driver.switch_to.default_content()

    def execute_screenshot(self, doc):
        filePath = setting.IMAGES_DIR +'/'+'{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info('{0}截图成功，图片路径为: {0}'.format(doc, filePath))
        except:
            logger.info('{0}截图 失败'.format(doc))

    def window_scroll(self, locator):
        """窗口滚动"""
        try:

            move_locator = self.get_element(locator)
            yy = self.driver.execute_script("arguments[0].scrollIntoView();", move_locator)
            logger.info('----------------窗口滚动--------------------------')
            return yy
        except Exception as e:
            logger.info('{0},页面窗口滚动失败！！！'.format(e))
            raise

    def use_js(self, loc, vaule):
        """调用js"""
        try:
            js = 'document.querySelector({0}).value="{1}";'.format(loc, vaule)
            self.driver.execute_script(js)
            logger.info('successful，js contents is：%s' % js)
        except BaseException:
            logger.error('js error', exc_info=1)









