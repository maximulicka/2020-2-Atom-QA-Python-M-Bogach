import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.authorization_page import AuthorizationPage

class UsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def authorization_page(driver):
    def authorization(login, passwd):
        
        page = AuthorizationPage(driver = driver)
        page.click(page.locators.ENTER_BOTTON1)
        page.fill_field(page.locators.LOGIN, login)
        page.fill_field(page.locators.PASSWD, passwd)
        page.click(page.locators.ENTER_BOTTON2, timeout= 5)

        return AuthorizationPage(driver=driver)
    return authorization


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']
    selenoid = config['selenoid']

    if browser == 'chrome':
        options = ChromeOptions()
        if selenoid:
            # http://127.0.0.1:4444/wd/hub/
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True, 'browserName': 'chrome'})

        else:
            options.add_argument("--window-size=800,600")

            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    driver.quit()
