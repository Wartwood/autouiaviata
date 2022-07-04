from base.seleniumbase import SeleniumBase
import time
from selenium.webdriver.common.keys import Keys

class BuyPopularTurkeyTickets(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__turkey_selector: str = '#app > div > div > div.container.mt-7 > div > div.mb-16 > div > div.relative.pt-18.p-6.bg-center.bg-no-repeat.bg-cover.rounded-md.relative.col-span-8 > div.glassmorphism.p-6.flex.flex-col.justify-between.rounded-md > div.flex.flex-col > button'
    def go_to_buy_tickets(self):
        time.sleep(3)
        go_to_turkey = self.is_present('css', self.__turkey_selector, 'Turkey button')
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        go_to_turkey.click()





