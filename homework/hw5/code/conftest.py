import pytest

from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user='root', password='saIMaYm5oA/Q', db_name='db_log')
