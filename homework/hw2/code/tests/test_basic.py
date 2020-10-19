import allure
import pytest
import time
import uuid
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pathlib import Path, PureWindowsPath
from tests.base import BaseCase
from tests.base import BaseCompany



class Test(BaseCase):

    @pytest.mark.skip(reason='no need')
    def test_authorization_pozitiff(self, authorization_page):
        authorization_pozitiff_page = authorization_page(login = 'maximulicka@mail.ru', passwd = 'Barsa2016')
        assert authorization_pozitiff_page.find(authorization_pozitiff_page.locators.PROFIL)


    #@pytest.mark.skip(reason='no need')
    def test_authorization_negatiff(self, authorization_page):
        authorization_negative_page = authorization_page(login = 'maximulicka@mail.ru', passwd = 'Barsa2015')
        assert 'Invalid login or password' in authorization_negative_page.driver.page_source

 
class TestCompany(BaseCompany):

    path_photo = PureWindowsPath(Path.cwd().joinpath('vk.png')).as_posix()

    @pytest.mark.skip(reason='no need')
    def test_create_company(self):
        link = "https://vk.com/max_bogaci"
        name = "VK"
        header = "Company"
        description = "Рекламная компания"
        self.authorization_page.create_company(link, name, header, description, self.path_photo)
        assert self.authorization_page.check_name(self.authorization_page.locators.COMPANY_LOCATOR, name)


class TestAudience(BaseCompany):

    @pytest.mark.skip(reason='no need')
    def test_create_segment(self):
        name = "Games"
        self.authorization_page.create_segment(name)
        assert self.authorization_page.check_name(self.authorization_page.locators.COMPANY_LOCATOR, name)

    @pytest.mark.skip(reason='no need')
    def test_delete_segment(self):
        name = str(uuid.uuid4())
        self.authorization_page.create_segment(name)
        self.authorization_page.delete_segment(name)
        time.sleep(5)
        assert not self.authorization_page.check_name(self.authorization_page.locators.COMPANY_LOCATOR, name)

    


    