import pytest,allure
import sys
import os



from Public.Log import Logger
from Public.getexcel import ReadExcel
from Public.get_config import r_config
from Config import setting

logger = Logger().get_logger()
search01_data = ReadExcel(setting.Trade_EXCEL, "search01").read_dictdata()
search02_data = ReadExcel(setting.Trade_EXCEL, "search02").read_dictdata()
print(search01_data)
@pytest.mark.smoke
@pytest.mark.lucas
@pytest.mark.usefixtures('start_session')
@pytest.mark.usefixtures('refresh_page')
class TestTrade:


    # 异常测试用例
    #@pytest.mark.skip(reason='跳过登录校验测试用例')
    @pytest.mark.parametrize('data', search01_data)
    @allure.story("XX测试用例")
    @allure.title("XX标题")
    @allure.step("XX步骤")
    @allure.description("这是XX系统-XX测试用例")
    @allure.severity(allure.severity_level.NORMAL)
    def test_trade_search01(self, data, start_session):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 正常测试用例：{0} ".format(data['name']))
        # 前置  访问登录页面
        # 步骤  输入用户名为空  密码 点击登录
        # 断言  登录中  提示：用户名或密码错误
        #logger.info('type ', type(data))
        start_session[1].search_01(data['searchterm'])
        logger.info("期望值：{0}".format(data['Msg']))
        logger.info("实际值：{0}".format(start_session[1].get_trade_Msg()))
        try:
            assert data['Msg'] == start_session[1].get_trade_Msg()
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].execute_screenshot("{0}-正常截图".format(data['name']))
        except:
            logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].execute_screenshot("{0}-异常截图".format(data['name']))
            raise

    # 正常用例
    @allure.story("XX测试用例")
    @allure.title("XX标题")
    @allure.step("XX步骤")
    @allure.description("这是XX系统-XX测试用例")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', search02_data)
    def test_trade_search02(self, data, start_session):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        # 前置  访问登录页面
        # 步骤  输入用户名为空  密码 点击登录
        # 断言  登录中  提示：用户名或密码错误
        # logger.info('type ', type(data))
        start_session[1].search_02()
        logger.info("期望值：{0}".format(data['Msg']))
        logger.info("实际值：{0}".format(start_session[1].get_trade_Msg()))
        try:
            assert data['Msg'] == start_session[1].get_trade_Msg()
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].execute_screenshot("{0}-正常截图".format(data['name']))
        except:
            logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].execute_screenshot("{0}-异常截图".format(data['name']))
            raise


if __name__ == '__main__':
    pytest.main(['-rs', 'test_trade.py'])

