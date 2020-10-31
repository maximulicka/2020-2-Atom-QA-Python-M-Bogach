from collections import defaultdict
import re
import json


with open("access.log") as file:
    list_column = []
    reg_exp = r"^(\d{1,3}(?:\.\d{1,3}){3})\s+(\-)\s+(\-)\s+\[(.*)\]" \
              r"\s+\"([A-Z]+)\s(\S+)\s(.+)\"\s(\d{3})\s(.*)\s\"(.*)\"\s\"(.*)\"\s\"(.*)\"$"
    for idx, item in enumerate(file):
        request = list(re.match(reg_exp, item).groups())
        if request[8].isdigit():
            request[8] = int(request[8])
        else:
            request[8] = 0
        list_column.append(request)


'#task1'
def length(x):
    return len(x)


log_len = length(list_column)


'#task2'
methods_dict = defaultdict(int)
for row in list_column:
    val = row[4]
    methods_dict[val] += 1


'#task3'
task3 = []
size_top = sorted(list_column, key=lambda row: int(row[8]), reverse=True)
for row in size_top[:10]:
    rows = (row[5], row[7], row[8])
    task3.append(rows)


'#task4'
task4 = defaultdict(int)
for line in list_column:
    if line[7][0] == '4':
        task4[line[0], line[5], line[7]] += 1
client_error = ((sorted(task4.items(), reverse=True, key=lambda x: x[1]))[:10])


'#task5'
task5 = []
server_error = sorted([row for row in list_column if row[7][0] == '5'],
                      key=lambda x: x[8], reverse=True)
for row in server_error[:10]:
    rows = (row[0], row[5], row[7], row[8])
    task5.append(rows)


result = {'log_len': log_len, 'methods': methods_dict,
          'size_top': task3, 'client_error': client_error,
          'server_error': task5}

with open('hw4.json', 'w') as f:
    json.dump(result, f, indent=4)
