import xlrd#全部读取某条case所有的值存放在字典里面
from Config import setting
import os
jsonPath = os.path.join(setting.EXCEL_DATA,"content_vod.json")
class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = "D:/APIRun/conf/case.xls"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())

# curpath = os.path.dirname(os.path.realpath(__file__))
# testxlsx = TESTCASE_PATH
#
# # 复制case.xls文件到report下
# report_path = os.path.join(os.path.dirname(curpath), "report")
# reportxlsx = os.path.join(report_path, "result.xls")
# testdata = readexcel.ExcelUtil(testxlsx).dict_data()
# print(testdata)