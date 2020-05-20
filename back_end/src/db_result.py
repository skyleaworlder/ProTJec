from collections import namedtuple
from . import glovar
from . import terminal_style
import traceback



'''
    输入参数
        record_names(tuple)
            记录的字段名
        records(tuple)
            记录元组，要求记录是可迭代的对象
'''
class DbResult(object):

    def __init__(self, record_names, records):
        self.__length = len(records)
        self.__Record = namedtuple('Record', record_names)
        self.__records = []
        try:
            for each_record in records:
                self.__records.append(self.__Record._make(each_record))
        except Exception as e:
            print('An error occurred when processing records:')
            traceback.print_exc()
        self.__records = tuple(self.__records)

        if glovar.DEBUG:
            terminal_style.fontBrightWhite()
            print('New Selection')
            terminal_style.reset()
            print('--------------------------------')
            terminal_style.fontBrightWhite()
            for record in self.__records:
                print(record)
            terminal_style.reset()
            print('--------------------------------')


    # 返回记录的数量
    def size(self):
        return self.__length

    # 返回 记录 与字段名匹配的 由 命名元组 组成的 元组
    def rawRecords(self):
        return self.__records

    # 返回 记录 与字段名匹配的 由 字典 组成的 元组
    def records(self):
        self.__records_dict = []
        for each_record in self.__records:
            self.__records_dict.append(dict(each_record._asdict()))
        self.__records_dict = tuple(self.__records_dict)
        return self.__records_dict


if __name__ == '__main__':
    DR = DbResult(
        ('name', 'id'),
        (
            ('Alice', '1851001'),
            ('Bob', '1851999'),
            ('Koishi', '1851514')
        )
    )
    print(DR.records())
