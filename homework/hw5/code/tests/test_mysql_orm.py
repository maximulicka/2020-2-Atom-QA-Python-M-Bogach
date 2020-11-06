import pytest
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


class TestBd(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.mysql: MysqlOrmConnection = MysqlOrmConnection(user='root', password='Barsa2016', db_name="log_file")
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test_add_row(self):
        request = ['134.249.53.187', '-', '-', '27/May/2016:03:32:28 +0200', 'POST',
                    'http://almhuette-raith.at/administrator/index.php', 'HTTP/1.1', '200', '4498', "-", "-", "-"]
        columns = ["ip", "field1", "field2", "date", "method", "http", "version", "status_code", "size", "field3",
                   "field4", "field5"]
        row = self.builder.add_row(
            ip=request[0],
            field1=request[1],
            field2=request[2],
            date=request[3],
            method=request[4],
            http=request[5],
            version=request[6],
            status_code=request[7],
            size=request[8],
            field3=request[9],
            field4=request[10],
            field5=request[11],
        )

        is_true = True
        for key, value in dict(zip(columns, request)).items():
            if value != getattr(row, key):
                is_true = False
                break
        assert is_true


