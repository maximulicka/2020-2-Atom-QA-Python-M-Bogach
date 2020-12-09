from faker import Faker

from models.models import Base, LogTemplate
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection

fake = Faker(locale='ru_RU')


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine
        self.create_log()

    def create_log(self):
        if not self.engine.dialect.has_table(self.engine, 'lof_file'):
            Base.metadata.tables['lof_file'].create(self.engine)

    def add_row(self, ip, field1, field2, date, method, http,
                version, status_code, size, field3, field4, field5):

        log_row = LogTemplate(
            ip=ip,
            field1=field1,
            field2=field2,
            date=date,
            method=method,
            http=http,
            version=version,
            status_code=status_code,
            size=size,
            field3=field3,
            field4=field4,
            field5=field5,
        )

        # Сохраняем объект в сессии, открытой в connection
        self.connection.session.add(log_row)
        # Записываем созданную запись в базу
        self.connection.session.commit()
        # Возвращаем объект для работы из тестов
        return log_row

