from selenium.webdriver.common.by import By


class TradeElement:
    searchterm_loc = (By.CSS_SELECTOR, '.global-search-box > input:nth-child(2)')
    trade_page_loc= (By.CSS_SELECTOR, '.toggle')
    submit_btn=(By.CSS_SELECTOR, "div.instrument:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    CRO_loc = (By.XPATH, "//div[@class='e-tabs__nav-item'][text()='CRO']")
    XTZ_btn = (By.XPATH, "//span[@class='base'][text()='XTZ']")


