import re
import xlwt

INDEX = 0
file = xlwt.Workbook()
table = file.add_sheet('sheet',cell_overwrite_ok=True)
with open('../parents_children_wik_results_2.txt', 'r', encoding='utf-8')as fp:
    data_source = fp.read()

data_source = data_source.split('\n\n')


def handle_parents(parents):
    temp = []
    parents = parents.split(',', 1)[-1]
    parents = parents.split(',')
    for i in parents:
        if i.endswith(')'):
            pass
        else:
            res = re.findall(r"u.(.*)'", i)
            if res:
                temp.append(res.pop())
    return temp


def write_to_csv(son, parents):
    global INDEX
    for p in range(len(parents)):
        table.write(INDEX,0,son)
        table.write(INDEX, 1, parents[p])
        INDEX += 1

if __name__ == '__main__':
    for item in data_source:

        line = item.split('\n')

        son = line[-2]
        parents = line[-1]

        son = re.findall(r".*u'(.*)'",son)
        parents = handle_parents(parents)
        write_to_csv(son, parents)
        break
    file.save('002.xls')