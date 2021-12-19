# _*_ coding:utf-8 _*_
import xlrd
import os, sys
from Config import setting


class ReadExcel():
    """读取excel文件数据"""

    def __init__(self, fileName, SheetName="Sheet1"):
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name(SheetName)

        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_dictdata(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格是空数据!")
            return None

    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
                for i in listApiData:
                    return i

        else:
            print("表格是空数据!")
            return None


if __name__ == "__main__":
    successData = ReadExcel(setting.Login_EXCEL, "success_data").read_data()
    failData = ReadExcel(setting.Login_EXCEL, "error_data").read_data()
    successData1 = ReadExcel(setting.Login_EXCEL, "success_data").read_dictdata()
    #print(successData)
    print(failData)
    # print(successData1)
    # print(successData["name"])
    # list=[{'case_ID': 1.0, 'name': '登录功能-正常测试', 'username': 'admin', 'password': 'Admin$123456', 'code': 'admin', 'Msg': '基础设施监控'}]
    # for i in list:
    #    print(i)
    # print(str(successData))
