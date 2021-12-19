# WebUI
这是一个关于python的WebUI自动化测试的项目，pytest测试框架，Python+PageObject+Pytest

实现页面元素、页面对象及业务、测试数据分离

项目结构：说明


            |-- Testcases                       --------------------- 测试用例模块
            |-- Public                     --------------------- 公共函数
            |-- Result                     --------------------- 测试报告
            |-- Config                     --------------------- 配置文件
            |-- Elements                     --------------------- 元素定位
            |-- OutPuts                     --------------------- 输出
            |   |-- image                   --------------------- 截图
            |   |-- log                     --------------------- 日志
            |-- PageObjects                 ---------------------- 业务流程
            |   |-- IndexPage               ---------------------- 主页模块的页面对象
            |   |   |-- index_page.py
            |   |   |-- __init__.py
            |   |-- __init__.py
            |-- README.md
            |--ExcelDatas                   ---------------------- 测试数据
               
        
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       

以下是简单说明：


-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------

测试用例:参数的正常和异常用例


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


-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
 Locators：
        #页面的元素
        

class TradeElement:
    searchterm_loc = (By.CSS_SELECTOR, '.global-search-box > input:nth-child(2)')
    trade_page_loc= (By.CSS_SELECTOR, '.toggle')
    submit_btn=(By.CSS_SELECTOR, "div.instrument:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    CRO_loc = (By.XPATH, "//div[@class='e-tabs__nav-item'][text()='CRO']")
    XTZ_btn = (By.XPATH, "//span[@class='base'][text()='XTZ']")
            
 -------------------------------------------------------------------------------------------------------------------------------------
 -------------------------------------------------------------------------------------------------------------------------------------
 PageObjects：
      # 业务功能流程
      
  class TradePage(BasePage):


    def search_01(self, searchterm):
        doc = '输入搜索功能1'
        self.send_key(loc.searchterm_loc, searchterm)
        self.click_element(loc.submit_btn)


    def search_02(self):
        doc = '输入搜索功能2'
        self.click_element(loc.CRO_loc)
        self.click_element(loc.XTZ_btn)

    def get_trade_Msg(self):
        return self.get_element_text(loc.trade_page_loc)
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
ExcelDatas
     # 测试数据
    
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
