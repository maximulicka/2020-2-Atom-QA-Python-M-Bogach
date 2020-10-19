import os

import pytest
from _pytest.fixtures import FixtureRequest

from ui.decorators import wait
from ui.pages.base_page import BasePage
from ui.pages.authorization_page import AuthorizationPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        # self.authorization_page: AuthorizationPage = request.getfixturevalue('authorization_page')(email="maximulicka@mail.ru", password="Barsa2016")
        # self.compain_page: CreateCompainPage = request.getfixturevalue('compain_page')
       
        #self.main_page: MainPage = request.getfixturevalue('main_page')

    def wait_download(self, file_name, timeout=30):

        def _check_download():
            for f in os.listdir(self.config['download_dir']):
                if f.endswith('.crdownload'):
                    return False

            if file_name in os.listdir(self.config['download_dir']):
                return True

            return False

        wait(method=_check_download, timeout=timeout)

class BaseCompany:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.authorization_page: AuthorizationPage = request.getfixturevalue('authorization_page')(login="maximulicka@mail.ru", passwd="Barsa2016")
        # self.compain_page: CreateCompainPage = request.getfixturevalue('compain_page')