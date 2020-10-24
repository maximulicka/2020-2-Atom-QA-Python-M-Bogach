import pytest

from api.mytarget_client import MyTargetClient
from conftest import Settings


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.config: Settings = config
        self.mytarget_client: MyTargetClient = request.getfixturevalue('mytarget_client')
