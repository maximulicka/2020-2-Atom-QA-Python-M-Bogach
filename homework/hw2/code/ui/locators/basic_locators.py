from selenium.webdriver.common.by import By


class BasePageLocators(object):
    COMPANY_Bottom = (By.XPATH, '//a[@href="/dashboard"]')
    AUDIENCE_Bottom = (By.XPATH, '//a[@href="/segments"]')

class AuthorizationPageLocators(BasePageLocators):
    ENTER_BOTTON1 = (By.XPATH, '//div[@class="responseHead-module-button-1BMAy4"]')
    LOGIN = (By.XPATH, '//input[@name="email"]')
    PASSWD = (By.XPATH, '//input[@type="password"]')
    ENTER_BOTTON2 = (By.XPATH, '//div[@class="authForm-module-button-2G6lZu"]')
    PROFIL = (By.XPATH, '//*[@href="/profile"]')

    # create company
    CREATE_COMPANY = (By.XPATH, '//*[@class = "button-module-textWrapper-3LNyYP" and text()="Создать кампанию"]')
    TRAFFIC = (By.XPATH, '//div[@class="column-list-item _traffic"]')
    LINK = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    NAME_COMPANY = (By.XPATH, '//div[@class = "input input_campaign-name input_with-close" and @cid = "view634"]//input[@type="text"]')
    TEASER = (By.XPATH, '//*[@id="149"]/span')
    HEADER = (By.XPATH, '//div[@class = "input input_banner-form input_title input_with-close"]//input')
    TEXT = (By.XPATH, '//*[@class = "textarea__elem js-form-element"]')
    LOAD_IMG = (By.XPATH, '//input[@type = "file" and @class = "input__inp input__inp_file js-form-element"]')
    ADD_IMG = (By.XPATH, '//input[@class = "image-cropper__save js-save" and @value = "Сохранить изображение"]')
    CREATE_COMPANY2 = (By.XPATH, '//div[@class = "button__text" and text() = "Создать кампанию"]')
    
    #шаблон для проверки компании/сегмента
    COMPANY_LOCATOR = (By.XPATH, '//a[@title="{}"]')

    #create segment
    CREATE_SEGMENT = (By.XPATH, '//div[@class = "button__text" and text()="Создать сегмент"]')
    CHOOSE_SEGMENT = (By.XPATH, '//div[text() = "Приложения и игры в соцсетях"]')
    MULTIPUL = (By.XPATH, '//div[@class = "adding-segments-source"]//input')
    ADD_SEGMENT = (By.XPATH, '//div[@class = "button__text" and text()="Добавить сегмент"]')
    NAME_SEGMENT = (By.XPATH, '//div[@class = "input input_create-segment-form"]//input')

    #delete segment
    DELETE_SEGMENT = (By.XPATH, '//div[contains(@data-test, "remove-{}")]/span')
    CLICK_DELETE_SEGMENT = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')


  
    
    









