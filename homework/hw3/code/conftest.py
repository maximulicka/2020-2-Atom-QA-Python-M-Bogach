import os
from dataclasses import dataclass

import allure
import pytest
import logging
from api.mytarget_client import MyTargetClient


@dataclass
class Settings:
    URL: str = None
    user: str = None
    password: str = None

@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings('https://target.my.com/', 'maximulicka@mail.ru', 'Barsa2016')
    return settings


@pytest.fixture(scope='function')
def mytarget_client(config):
    return MyTargetClient(config)


@pytest.fixture(scope='function')
def logger(request):
    """
        Фикстура для логирования. Не используется в тестах техноатома просто так, можно заиспользовать.
        В Интернетах полно документации и примеров, гуглится всё очень быстро.
    """

    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file = request.node.location[-1]

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    log = logging.getLogger('api_log')
    log.propogate = False
    log.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    # Для того чтобы аттачить логи в случае пофейленных тестов
    failed_count = request.session.testsfailed
    yield log
    if request.session.testsfailed > failed_count:
        with open(log_file, 'r') as f:
            allure.attach(f.read(), name=log.name, attachment_type=allure.attachment_type.TEXT)

    os.remove(log_file)
