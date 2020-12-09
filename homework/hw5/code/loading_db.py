import os
import re

from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


class Log:
    def __init__(self, log):
        self.mysql = MysqlOrmConnection(user='root', password='Barsa2016', db_name="log_file")
        self.builder = MysqlOrmBuilder(connection=self.mysql)
        self.log = log
        self.load_log()

    def load_log(self):
        with open(self.log) as file:
            reg_exp = r"^(\d{1,3}(?:\.\d{1,3}){3})\s+(\-)\s+(\-)\s+\[(.*)\]" \
                      r"\s+\"([A-Z]+)\s(\S+)\s(.+)\"\s(\d{3})\s(.*)\s\"(.*)\"\s\"(.*)\"\s\"(.*)\"$"
            for line in file:
                try:
                    request = list(re.match(reg_exp, line).groups())
                except AttributeError:
                    continue
                if request[8].isdigit():
                    request[8] = int(request[8])
                else:
                    request[8] = 0
                self.builder.add_row(
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


if __name__ == '__main__':
    Log('access.log')












