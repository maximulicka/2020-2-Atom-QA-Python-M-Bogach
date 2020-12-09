from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LogTemplate(Base):
    # В __tablename__ указывается имя таблицы, которую мы хотим создать
    __tablename__ = 'lof_file'
    # __table_args__ используется для установки кодировки в базе на utf8, т. к. мы записываем в нее кириллицу.
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    field1 = Column(Text, nullable=False)
    field2 = Column(Text, nullable=False)
    date = Column(Text, nullable=False)
    method = Column(Text, nullable=False)
    http = Column(Text, nullable=False)
    version = Column(Text, nullable=False)
    status_code = Column(Text, nullable=False)
    size = Column(Text, nullable=False)
    field3 = Column(Text, nullable=False)
    field4 = Column(Text, nullable=False)
    field5 = Column(Text, nullable=False)

    # Метод __repr__ используется для того, чтобы можно было сделать красивый вывод полей нашей модели
    # при обращении к ней из дебага или просто печати ее содердимого.
    def __repr__(self):
        return f"<log_file(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}'," \
               f"field1='{self.field1}'," \
               f"field2='{self.field2}'," \
               f"date='{self.date}'," \
               f"method='{self.method}', " \
               f"http='{self.http}', " \
               f"version='{self.version}'" \
               f"status_code='{self.status_code}'" \
               f"size='{self.size}'" \
               f"field3='{self.field3}'" \
               f"field4='{self.field4}'" \
               f"field5='{self.field5}'" \
               f")>"
