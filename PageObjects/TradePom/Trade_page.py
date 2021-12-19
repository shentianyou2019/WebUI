from Elements.trade_elements import TradeElement as loc
from Public.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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





