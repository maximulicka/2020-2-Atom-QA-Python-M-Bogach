import pytest
import uuid

from tests.base import BaseCase


class TestMyTarget(BaseCase):

    @pytest.mark.API
    def test_authorization(self):
        assert self.mytarget_client.csrf_token is not None

    @pytest.mark.API
    def test_create_segment(self):
        name = str(uuid.uuid4())
        assert type(self.mytarget_client.create_segment(name)) == int

    @pytest.mark.API
    def test_delete_segment(self):
        name = str(uuid.uuid4())
        segment = self.mytarget_client.create_segment(name)
        self.mytarget_client.delete_segment(segment)
        assert not self.mytarget_client.get_audience(segment)
