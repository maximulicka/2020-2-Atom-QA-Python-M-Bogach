from ui.locators.basic_locators import AuthorizationPageLocators
from ui.pages.base_page import BasePage
import time
from selenium.webdriver import ActionChains

class AuthorizationPage(BasePage):
    locators = AuthorizationPageLocators()

    def create_company(self, url, _name, header, text, path_photo):
        self.click(self.locators.COMPANY_Bottom)
        self.click(self.locators.CREATE_COMPANY)
        self.click(self.locators.TRAFFIC)
        self.fill_field(self.locators.LINK, url)
        self.click(self.locators.TEASER)
        self.fill_field(self.locators.HEADER, header)
        self.fill_field(self.locators.TEXT, text)
        self.load_file(self.locators.LOAD_IMG, path_photo, self.locators.ADD_IMG)
        self.fill_field(self.locators.NAME_COMPANY, _name) #если эту строку вставить после self.click(self.locators.TEASER), то вылетит
        ActionChains(self.driver).move_to_element(self.find(self.locators.CREATE_COMPANY2)).perform()
        self.click(self.locators.CREATE_COMPANY2)

    def create_segment(self, _name):
        self.click(self.locators.AUDIENCE_Bottom)
        self.click(self.locators.CREATE_SEGMENT)
        self.click(self.locators.CHOOSE_SEGMENT)
        self.click(self.locators.MULTIPUL)
        self.click(self.locators.ADD_SEGMENT)
        self.fill_field(self.locators.NAME_SEGMENT, _name)
        self.click(self.locators.CREATE_SEGMENT)

        
    def delete_segment(self, segment_name):
        by, locator = self.locators.COMPANY_LOCATOR
        segment_adress = self.find((by, locator.format(segment_name)), timeout=7)
        segment = segment_adress.get_attribute('href').split('/')[-1]
        by, delete_locator = self.locators.DELETE_SEGMENT
        self.click((by, delete_locator.format(segment)), timeout=7)
        self.click(self.locators.CLICK_DELETE_SEGMENT)


    